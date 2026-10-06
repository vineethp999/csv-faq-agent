from __future__ import annotations

from typing import Any

import pandas as pd


SYSTEM_PROMPT = """
You are a strict CSV-only answer assistant.
Use only the information present in the uploaded CSV data.
Do not use general knowledge, assumptions, or outside facts.
If the answer is not explicitly present in the data, say: "I could not find this information in the uploaded files."
Use clear, concise, customer-ready English.
"""


def answer_question(data: pd.DataFrame, question: str) -> str:
    """Answer a natural-language question from a single DataFrame."""
    normalized_question = question.strip()
    if not normalized_question:
        return "I could not find this information in the uploaded files."

    if data.empty:
        return "I could not find this information in the uploaded files."

    lowered = normalized_question.lower()
    columns = [str(column).lower() for column in data.columns]

    for column in data.columns:
        values = data[column].astype(str).str.lower().tolist()
        if any(lowered in value for value in values if isinstance(value, str)):
            sample = data[column].astype(str).tolist()
            match = [row for row in data.itertuples(index=False) if str(getattr(row, column)).lower() in lowered or lowered in str(getattr(row, column)).lower()]
            if match:
                return f"From the uploaded data, {column} includes a matching record: {match[0]}."

    for column in data.columns:
        if "question" in str(column).lower() or "faq" in str(column).lower() or "policy" in str(column).lower() or "answer" in str(column).lower() or "description" in str(column).lower():
            text_values = data[column].astype(str)
            for value in text_values:
                if isinstance(value, str) and len(value) > 0:
                    if lowered in value.lower():
                        return value

    for column in data.columns:
        if any(keyword in str(column).lower() for keyword in ["price", "cost", "rate", "limit", "hours", "stock", "population", "count", "total"]):
            numeric_series = pd.to_numeric(data[column], errors="coerce")
            if numeric_series.notna().any():
                if any(keyword in lowered for keyword in ["average", "avg", "mean"]):
                    avg = numeric_series.mean()
                    return f"The average value in the uploaded data is {avg}."
                if any(keyword in lowered for keyword in ["total", "sum"]):
                    total = numeric_series.sum()
                    return f"The total from the uploaded data is {total}."

    return "I could not find this information in the uploaded files."
