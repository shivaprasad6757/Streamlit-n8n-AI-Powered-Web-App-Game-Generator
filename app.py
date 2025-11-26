import streamlit as st
import requests
import subprocess

st.title("AI-Powered Web App/Game Generator")

prompt = st.text_area("Please enter the prompt to create a APP/Game", placeholder = "Give your game name")

url = "https://shivan8n12.app.n8n.cloud/webhook-test/e12cf07c-abac-46cb-8bf7-e98bafe651c2"

if st.button("Generate APP"):
    if prompt :
        response = requests.post(url = url, json = {"prompt" : prompt})

        if response.status_code == 200:
            st.write("success")

            with open("app_code.py","w") as file :
                file.write(response.json()["output"].strip("```python"))
                
            subprocess.run(["python","app_code.py"])
            
        else :
            st.write(f"ERROR : {response.status_code}")