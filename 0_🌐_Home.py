import streamlit as st
from io import BytesIO


result = BytesIO()

st.set_page_config(
                   page_title='TranscriptIQ',
                   page_icon='✨'
                )


st.header('TranscriptIQ')

st.markdown("""
TranscriptIQ allows you to talk ask questions any youtube video or video you upload. Under the hood it uses the latest AI technology to transcribe the audio and then search for the answer to your question in the transcript.
            
### Features 
* **Transcribe** any youtube video or video you upload
* **Search** for any question in the transcript
* **Highlight** the answer in the transcript
* **Chat** LLM powered AI to answer all your questions. 

You can check the source code at this [github repository](https://github.com/Devanshu-17/TranscriptIQ)

            
### How to use 
* Either upload a video or paste a youtube link
* Let the AI do the magic ask questions get answers, understand videos better. 
""")


st.markdown("""

----
### About the project
This project was developed as the part of LLM hackathon arranged by Streamlit. If any queries don't hesitate to reach out and raise an  issue in a repo :) .  
The project was created by [Devanshu](https://github.com/Devanshu-17), [Somesh](https://github.com/someshfengde).

""")
