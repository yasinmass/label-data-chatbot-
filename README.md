🧠 Label-Data Chatbot (RAG-based AI Assistant)

A Flask-based intelligent chatbot that answers user questions strictly from labeled data using Google Gemini (Generative AI).
This project follows a Retrieval-Augmented Generation (RAG) approach to ensure accurate, context-grounded responses.

📌 Project Overview

This chatbot is designed to:

Answer questions only using predefined Q&A data

Avoid hallucinations from the AI model

Provide reliable responses for domain-specific datasets

The system loads labeled data from a CSV file and uses it as context for the Gemini model.

⚙️ Tech Stack

Backend: Flask (Python)

AI Model: Google Gemini (gemini-2.5-flash)

Data Source: CSV-based labeled Q&A

Frontend: HTML (Jinja templates)

Deployment Ready: Procfile included

🧩 Architecture (How it Works)

User enters a question via the web interface

Flask backend receives the query

Labeled Q&A data is loaded from CSV

Context is constructed from the dataset

Gemini model answers only using that context

If no relevant answer exists → chatbot responds safely

📂 Project Structure
label-data-chatbot-/
│
├── app.py                 # Main Flask application
├── QA for chatbot.csv     # Labeled Q&A dataset
├── requirements.txt       # Python dependencies
├── Procfile               # Deployment configuration
├── README.md              # Project documentation
└── templates/
    └── index.html         # Chat UI

🚀 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yasinmass/label-data-chatbot-.git
cd label-data-chatbot-

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Environment Variable

Create a .env file:

GOOGLE_API_KEY=your_gemini_api_key

▶️ Run the Application
python app.py


Open browser:

http://127.0.0.1:5000

🔐 Key Features

✅ Context-aware responses

✅ No hallucinated answers

✅ Simple CSV-based knowledge update

✅ Easy deployment

✅ Beginner-friendly codebase

🧪 Example Use Case

User Question:

What is machine learning?

Chatbot Behavior:

Searches labeled dataset

Responds only if answer exists

Otherwise returns:
“No relevant Q&A found.”

🌍 Deployment

This project is deployment-ready and can be hosted on:

Render

Railway

Heroku

Any Flask-supported platform

👤 Author

Mohammed Yasin
GitHub: @yasinmass

📜 License

This project is open-source and free to use for learning and development purposes.

⭐ If you find this useful, give the repo a star!
