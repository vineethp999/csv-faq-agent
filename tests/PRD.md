Business Requirement :

Build a small web app that works as a CSV FAQ Agent
● The user can upload one or more CSV files
● The user can ask a question in normal language
● The AI reads the data in those CSV files and replies using real values from the tables
Important points
● The answer must come from the CSV content
● The model should not answer from general world knowledge
● If the answer is not in the data, it should say that clearly

We want a simple internal tool called Hello Agent.
Support agents should be able to
● Upload the latest CSV files for policies and FAQs
● Type a natural language question
● Get a clear answer that they can copy paste into an email or chat
This tool will reduce time spent searching in documents and will improve answer consistency.

Target users
● Customer support agents
● Product managers who want to test how clear their policy text is
● Operations staff who need quick answers while talking to customers on phone or chat

Data Sources:
● ecommerce_faqs.csv - frequently asked questions for an online store
● credit_card_terms.csv - terms and conditions for credit cards
● hospital_policy.csv - hospital rules for visits, records, and other items
● saas_docs.csv - features, limits, and support details for a software as a service
product

Functional requirements :
Your app should cover the following points.
1. File upload
○ The user can upload one or many CSV files from their local machine
○ The app shows a small preview of each file, for example the first few rows
2. Question input
○ The user can type a question in a text box in normal language
○ Example questions
■ What is the return policy for electronics
■ What does the extended warranty cover
■ What are the visiting hours in the hospital
■ What is the API rate limit for the free plan
3. Answer generation
○ The AI must read the CSV data and find the most relevant row or rows
○ For text questions it should return the key piece of text, for example from the
Answer or Policy column
○ For numeric questions it should compute totals or averages if needed
○ The answer should be in clear English, ready to share with a customer
4. Data only rule
○ The AI must not guess from general knowledge
○ If it cannot find a matching answer in the CSV data, it should say something like
■ I could not find this information in the uploaded files

5. Simple user interface
○ The interface should be simple and clean
○ A first time user should understand what to do without reading long instructions

Non functional expectations :
This is a small warm up project, so expectations are simple
● The app should feel responsive on small test CSV files
● The code should be easy to read and change
● The behavior should be predictable and safe
○ No random creative answers
○ The model should mostly keep temperature low and follow rules

Minimum expected behavior :
Your app should
● Accept multiple CSV uploads
● Convert each CSV into a Pandas data frame
● Create a LangChain agent that can work with these data frames
● Build a system prompt that forces the model to use the data only
● Pass the user question plus the system prompt into the agent
● Display the answer clearly in the Streamlit app

Tools and libraries :
● Python
● Streamlit for the web app
● Pandas for reading and working with CSV files
● LangChain for building a data frame agent
● OpenAI chat model, for example gpt 4o mini
● A valid OpenAI API key
Note: no need for a vector DB