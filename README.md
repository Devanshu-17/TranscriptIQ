# TranscriptIQ
TranscriptIQ is a project that enables users to transcribe YouTube videos and perform various NLP (Natural Language Processing) tasks, chat with youtube video and many more on the transcribed text. 

## Deployed app link: 
### https://transcript-iq.streamlit.app/

## Implementation video 


https://github.com/Devanshu-17/TranscriptIQ/assets/42097653/c018a440-c613-4cfa-8440-edb5bc07bb26



## Directory Structure
```
./
├── LICENSE
├── README.md
├── app.py
├── images
│   ├── AI.jpg
│   ├── NER.png
│   ├── Robot_whisper1.jpg
│   ├── Robot_whisper2.jpg
│   ├── Robot_whisper3.jpg
│   ├── expander.png
│   ├── mp3_2_text.png
│   ├── resum.png
│   └── youtube2text.png
├── myfunctions
│   ├── __pycache__
│   ├── my_functions.py
│   └── my_summarization_functions.py
├── packages.txt
├── pages
│   ├── Chat.py
│   ├── Transcribe Youtube.py
│   └── static
└── requirements.txt

6 directories, 18 files
```

## Functionality
The main functionality of TranscriptIQ is provided by the `transcribe_youtube.py` script. It uses the Streamlit library to create a user interface for transcribing YouTube videos and performing NLP tasks. Here is a brief overview of the functionality provided by the script:

- Retrieve YouTube video information (title, author, views, duration, etc.)
- Download YouTube videos as MP4 format
- Convert MP4 videos to MP3 audio files
- Transcribe MP3 audio files to text using speech-to-text technology
- Perform text summarization using the Cohere API
- Perform Named Entity Recognition (NER) using the Spacy library
- Generate graphs based on NER results
- Perform sentiment analysis using the VADER library
- Display word clouds based on NER results

## Usage
To use TranscriptIQ, you can run the `app.py` script. This will start the Streamlit app and you can interact with it to transcribe YouTube videos and perform NLP tasks on the transcribed text.

Note: Before running the script, make sure you have installed all the required packages listed in `requirements.txt`.

```python
streamlit run app.py
```



## Credits
TranscriptIQ was developed as part of the Streamlit LLM Hackathon. The project was created by [Devanshu](https://github.com/Devanshu-17), [Somesh](https://github.com/someshfengde).
