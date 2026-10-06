# CSV FAQ Agent - Implementation Plan

## 1. Objective
Build a small Streamlit web application called Hello Agent that allows support agents to upload one or more CSV files, ask natural-language questions, and receive answers based only on the uploaded data. The app must not rely on general world knowledge and must clearly state when the requested information is not found in the uploaded files.

## 2. Scope
This project includes:
- CSV file upload and validation
- Preview of uploaded CSV files
- Data preparation with Pandas
- Question answering grounded in uploaded tabular data
- A simple web UI using Streamlit
- Safe answer behavior that refuses unsupported general knowledge

This project does not include:
- Vector database indexing
- Persistent user accounts or storage
- Complex multi-agent orchestration
- Production-grade authentication

## 3. User Stories
### 3.1 Support agent
As a support agent, I want to upload policy and FAQ CSV files so that I can quickly answer customer questions from the latest data.

### 3.2 Customer support user
As a user, I want to type a natural-language question so that I can get a clear answer without manually searching the tables.

### 3.3 Product manager
As a product manager, I want to test whether documentation is clear and consistent by asking questions against uploaded policy files.

### 3.4 Operations user
As an operations user, I want quick factual answers from uploaded CSVs so I can respond while speaking with customers.

## 4. Functional Requirements

### 4.1 File upload
- The app must accept one or many CSV files from the local machine.
- Each uploaded file should be parsed as a Pandas DataFrame.
- The app should display a small preview of each file, including the first few rows.
- Uploaded files should be stored in memory for the current session.

### 4.2 Question input
- The user can enter a natural-language question in a text box.
- Example questions include:
  - What is the return policy for electronics?
  - What does the extended warranty cover?
  - What are the visiting hours in the hospital?
  - What is the API rate limit for the free plan?

### 4.3 Answer generation
- The model should read the loaded CSV data and identify the most relevant row or rows.
- For textual questions, the answer should come from fields such as Question, Answer, Policy, Description, or similar relevant columns.
- For numeric questions, the app may compute totals, averages, or other derived values if the data supports them.
- The final answer should be written in clear English, suitable for sharing in a customer email or chat message.
- The answer should include values directly from the CSV data when available.

### 4.4 Data-only rule
- The system must not answer using general world knowledge.
- If the requested answer cannot be found in the uploaded files, the system must say so clearly.
- The fallback response should be something like: "I could not find this information in the uploaded files."
- The model should be instructed to only answer from the provided CSV content.

### 4.5 Simple UI
- The interface should be clean and straightforward.
- A first-time user should understand how to upload files and ask a question without reading long instructions.
- The page should show the file upload area, question input box, and response area clearly.

## 5. Non-Functional Requirements
- The app should feel responsive on small test CSV files.
- Code should stay easy to read and change.
- The answer behavior must be consistent and safe.
- The model temperature should be low to reduce creative or unsupported answers.
- The app should favor correctness over broad reasoning.

## 6. Minimum Expected Behavior
The app must:
1. Accept multiple CSV uploads.
2. Convert each CSV into a Pandas DataFrame.
3. Create a LangChain agent using the uploaded DataFrames.
4. Build a system prompt that forces the model to stay grounded in the uploaded data.
5. Pass the user question and system prompt to the agent.
6. Display the answer clearly in the Streamlit UI.

## 7. Proposed Technical Architecture

### 7.1 Frontend
- Streamlit app with a simple layout: upload widget, file preview section, question input, submit button, and answer display.
- Minimal styling to keep the interface clean and easy to use.

### 7.2 Backend
- Python application entry point using Streamlit.
- CSV upload handler that reads files using Pandas.
- DataFrame collection service that stores all uploaded tables in memory.
- Agent orchestration layer that passes the question plus data context to the LLM.

### 7.3 LLM integration
- Use OpenAI chat model, such as GPT-4o mini.
- Use a low-temperature setting.
- Use a strong system prompt instructing the model to:
  - use only the uploaded CSV content
  - return direct evidence from the data
  - refuse to answer based on outside knowledge
  - say clearly when information is missing

### 7.4 Data-handling approach
- Read every uploaded CSV into a DataFrame.
- Keep source file names and preview rows visible to the user.
- For the LLM, expose the data in a structured way so the model can reason over actual values instead of guessing.

## 8. Implementation Plan

### Step 1: Project setup
- Create a Python project structure.
- Add requirements for Streamlit, Pandas, LangChain, and OpenAI.
- Create a basic app entry file, such as app.py.

### Step 2: CSV ingestion
- Build file upload handling for one or more CSVs.
- Read each file with Pandas.
- Validate file format and handle malformed CSV files gracefully.
- Generate a preview of each file, limited to a small number of rows.

### Step 3: Data context preparation
- Keep a list of uploaded DataFrames with names.
- Summarize each table for the agent, including column names and a sample of row values.
- Ensure the system prompt makes it clear that only uploaded content is allowed.

### Step 4: Grounded answer logic
- Pass the user question and data context to a LangChain DataFrame agent or equivalent approach.
- Bind the model to strict instructions: no outside knowledge, no assumptions.
- If no relevant data matches, return a clear fallback answer.

### Step 5: UI and user flow
- Build the upload section.
- Build the ask-question form.
- Render the answer in a clear response container.
- Add simple helper text for users.

### Step 6: Validation
Test the app with sample CSVs and questions such as:
- What is the return policy for electronics?
- What does the extended warranty cover?
- What are the visiting hours in the hospital?
- What is the API rate limit for the free plan?
- What is the policy for a missing or unsupported item?

Validate that:
- answers come from CSV values
- unsupported items return a clear “not found” response
- no invented facts appear

## 9. Example System Prompt
Use a system prompt similar to the following:

You are an answer assistant for uploaded CSV files. Your job is to answer user questions using only the data in the uploaded tables. Do not use general knowledge or assumptions. If the answer is not explicitly present in the CSV data, say: "I could not find this information in the uploaded files." Use exact values from the data when possible. Prefer clean, customer-ready English responses.

## 10. Risks and Constraints
- The LLM may still try to generalize if not tightly constrained.
- CSVs may contain inconsistent column names, so column detection must be tolerant.
- Unsupported questions should not produce speculative answers.
- The app should avoid excessive complexity to keep the project small and predictable.

## 11. Acceptance Criteria
The implementation is considered successful when all of the following are true:
- Users can upload multiple CSV files.
- Each uploaded file is displayed as a preview.
- A natural-language question can be submitted through the UI.
- The answer is based on actual values from the uploaded CSV content.
- The app clearly states when information is missing from the uploaded files.
- The response is safe, predictable, and easy to copy into customer communication.

## 12. Deliverables
- Streamlit app entry file
- CSV upload and parsing logic
- DataFrame agent logic with grounded prompting
- UI for upload, question input, and answer output
- README with setup instructions and OpenAI API key configuration
