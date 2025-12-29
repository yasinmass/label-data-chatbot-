



from flask import Flask,request,render_template
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os

#Caling loading api key

load_dotenv()

app=Flask(__name__) #application starts from here ( starting point of flask)

#configure api call model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))   #GOOGLE_API_KEY is variable name in thr .env file
model=genai.GenerativeModel("gemini-2.5-flash")

question_answer=pd.read_csv("QA for chatbot.csv")
#text to context
context_text =""
for _,row in question_answer.iterrows():
    context_text +=f"Q: {row['question']}\nA:{row['answer']}\n\n"

def ask_gemini(query):
    prompt =f"""
you are a D&A assistance.
Answer only using the context below
if the answer is not present, say : No relevant Q&A Found

context:
{context_text}

question: {query}
"""
    response=model.generate_content(prompt)
    return response.text.strip()


#route function

@app.route("/",methods=["GET","POST"])
def home():
    answer=""
    if request.method=="POST":
        query=request.form['query']
        answer=ask_gemini(query)
    return render_template("index.html",answer=answer)

if __name__ =="__main__":
    app.run()




#terminal prompt type for reference 

# print("Q A chat bot")
# print("Enter exit grt terminate")

# while True:
#     user_input=input("you :")
#     if user_input.lower()=="exit":
#         print("good bye")
#         break
#     answer=ask_gemini(user_input)
#     print(f"{answer}\n")