import streamlit as st
import requests
from PIL import Image



data = {}


summarization_llms = ["sshleifer/distilbart-cnn-12-6","google/pegasus-xsum","marianna13/flan-t5-base-summarization","facebook/bart-large-cnn"]

qa_llms = ["deepset/electra-base-squad2","timpal0l/mdeberta-v3-base-squad2","distilbert-base-uncased-distilled-squad","deepset/roberta-base-squad2"]


def run():

    st.title("QA + Summarization from LLMs")

    selected_task = st.selectbox("Select a task", ["Summarization", "QA"])

    image = st.file_uploader("Upload your image",type=['jpeg','jpg'])

    # data['task'] = st.text_input("Provide the task to be performed..")

    if selected_task == "QA":
        data['question'] = st.text_input("Please enter your question..")
    

    if selected_task == "Summarization":
        selected_llm = st.selectbox("Select a LLM for summarization", summarization_llms)
    elif selected_task == "QA":
        selected_llm = st.selectbox("Select a LLM for QA", qa_llms)
    

    if st.button("Execute"):

        data['llm'] = selected_llm
        data['task'] = selected_task

        # if data['task'] == "summarization" or data['task'] == "Summarization":
        if selected_task == "Summarization" :
            files = {"image": (image.name, image, image)}
            response = requests.post("http://localhost:8000/summarization",data = data,files = files)
            prediction = response.json()
            # prediction = prediction[0]['summary_text']

            st.success(f"The summary of the text is : {prediction}")
        
        # elif data['task'] == "question-answer" or data['task'] == "QA" :
        elif selected_task == "QA" :
            files = {"image": (image.name, image, image)}
            response = requests.post("http://localhost:8000/qa",data = data,files = files)
            prediction = response.json()
            # prediction = prediction['answer']

            st.success(f"The answer is : {prediction}")

        else :
            st.error('Enter the correct task.')


if __name__ == '__main__':
    run()
    
