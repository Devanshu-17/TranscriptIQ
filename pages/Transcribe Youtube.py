import streamlit as st
import os
from datetime import datetime
from moviepy.editor import VideoFileClip
from myfunctions.my_functions import current_directory, create_folder_and_directories, download_youtube, rename_videos, mp4_to_mp3, transcribe_mp3, download_youtube1, get_video_info
from myfunctions.my_summarization_functions import summarize_with_cohere
from myfunctions.my_summarization_functions import ner_spacy, get_graph
from io import BytesIO
from annotated_text import annotated_text
import pandas as pd
import plotly.express as px
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import streamlit_scrollable_textbox as stx
import pyecharts.options as opts
from pyecharts.charts import Bar3D
from collections import Counter
from pyecharts.charts import WordCloud
from pyecharts.charts import Gauge

result = BytesIO()

st.set_page_config(layout="wide",
                   page_title='Transcribe YouTube Video',
                   page_icon=':video_camera:')

# make any grid with a function
def make_grid(cols,rows):
    grid = [0]*cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid

with st.sidebar:
    st.image('images/Robot_whisper2.jpg')

st.header('Transcribe YouTube Video :video_camera:')



current_directory(3)



#if youtube_button:

try:
  # check if the key exists in session state
  _ = st.session_state.keep_graphics
except AttributeError:
  # otherwise set it to false
  st.session_state.keep_graphics = False


# Specify the YouTube video URL
video_url = st.text_input('Youtube link', 'https://www.youtube.com/watch?v=8Zx04h24uBs&ab_channel=LexClips')
youtube_button = st.button('Transcribe')

if youtube_button or st.session_state.keep_graphics:
    info = get_video_info(video_url)
    st.markdown(f"#### {info['title']}")

    grid_video = make_grid(1,6)

    with grid_video[0][0]:
         st.markdown(f"""
                     Views
                     #### {info['views']}
                     """)
    with grid_video[0][1]:
         st.markdown(f"""
                     Length
                     #### {info['length']} sec.
                     """)
    with grid_video[0][2]:
        st.markdown(f"""
                    Author
                    #### {info['author']}
                    """)
    with grid_video[0][3]:
        st.markdown(f"""
                    video id
                    #### {info['video_id']}
                    """)
    with grid_video[0][4]:
        
        st.markdown(f"""
                    Publish date
                    #### {datetime.strftime(info['publish_date'], "%Y-%m-%d")}
                    """)
    with grid_video[0][5]:
        st.image(info['thumbnail_url'])


    if info['age_restricted']:
        st.warning('This video is age restricted. The application will stop at this point.', icon="⚠️")
    else :
        mp4_directory, mp3_directory, txt_directory = create_folder_and_directories()
        duration = info['length']

        with st.spinner("Download Youtube as MP4"):

            try:
                video_extension = download_youtube(video_url, mp4_directory)

            except:
                with st.spinner("Please wait, the application is currently unable to download the video in MP4 format. It is currently attempting to download the video in WebM format instead. This process may take some time. Thank you for your patience."):
                    video_extension,duration= download_youtube1(video_url, mp4_directory)
                    # duration= download_youtube1(video_url, mp4_directory)


            rename_videos(mp4_directory)
            video_mp4 = os.path.join(mp4_directory, f"video.{video_extension}")
            # video_mp4 = os.path.join(mp4_directory, "video.webm")

        # Check the duration of the video in seconds
        if duration < 180 :# 3 minutes
                
                with st.spinner("Convert MP4 to MP3"):
            
                    
                    mp4_to_mp3(mp4_directory, video_extension, mp3_directory )
                    

                    
                
                col1, col2 = st.columns(2)   

                        

                
                col2.audio(f"{mp3_directory}/my_audio.mp3")
                
                with st.spinner("Transcribe YouTube Video ... "):
                        
                        result = transcribe_mp3(mp3_directory, "my_audio") 
        
                        txt_path = f"{txt_directory}/output.txt" 
        
                        # Open the file in write mode
                        with open(txt_path, 'w') as file:
                            # Write the data to the file
                            file.write(result['text'])

                WebVTT = "WEBVTT"
                with col1:
                    st.info(f"Detected language: {result['language']}")


                    
                    for segment in result['segments']:
                        start = round(float(segment['start']),2)
                        end = round(float(segment['end']),2)
                        text = segment['text']
                        WebVTT += f""" \n[{start} : {end}] : {text}"""
                    

                    user_text = st.text_area("The Complete Text",result['text'], height=450)
                
                with st.expander("WebVTT"):
                        st.text_area("Format Web Video Text Tracks (WebVTT)", WebVTT, height=200)

                    

                col2.video(video_url)
                                                                                
                #st.download_button('Download text as csv', result['text'])
                st.download_button(
                        label=f"Download as txt",
                        data=result['text'],
                        file_name=f'Transcribe YouTube Video {datetime.now()}.txt',
                        mime='text/plain'
                    )
        

        else:
                
                st.warning(f'The duration of the video exceeds 3 minutes ({round(duration/60,2)} minutes). To handle this, the application will divide the video into multiple 3-minute segments and convert each segment into an MP3 file. ', icon="⚠️")
                col1, col2 = st.columns(2)

                        
                video = VideoFileClip(video_mp4)
                #duration = video.duration

                # Calculate the number of 3-minute segments
                num_segments = int(duration // 180) + 1
                result_text = ''
                WebVTT = "WEBVTT"
                for i in range(num_segments):
                    
                        # Set the start and end times for the segment
                        start_time = i * 180  # 3 minutes
                        end_time = min((i + 1) * 180, duration)  # 3 minutes or remainder of the video
                        with st.spinner(f"Please wait ..."):
                            # Extract the segment and convert to MP3
                            segment = video.subclip(start_time, end_time)
                            output_filename = f"{mp3_directory}/segment_{i + 1}.mp3"
                            segment.audio.write_audiofile(output_filename)

                            col2.audio(f"{mp3_directory}/segment_{i + 1}.mp3")


                        with st.spinner(f"Transcribe from : {round(start_time/60,2)} min. to {round(end_time/60,2)} min."):
                            result = transcribe_mp3(mp3_directory, f"segment_{i + 1}")
                        col1.write(f"Transcribe from : {round(start_time/60,2)} min. to {round(end_time/60,2)} min. : OK")
                        for segment in result['segments']:
                            start = round(float(segment['start']),2)
                            end = round(float(segment['end']),2)
                            text = segment['text']
                            #col1.markdown(f"""[{start} : {end}] : {text}""")
                            WebVTT += f""" \n[{start} : {end}] : {text}"""


                        result_text = result_text + result['text'] + " "

                with col1:
                    st.info(f"Detected language: {result['language']}")
                    
                

                video.close()
                col2.video(video_url)


                #concatenated_text = concatenate_txt_files(txt_directory)
                #st.download_button('Download text as csv', concatenated_text)
                result = result_text

                txt_path = f"{txt_directory}/output.txt" 
        
                # Open the file in write mode
                with open(txt_path, 'w') as file:
                    # Write the data to the file
                    file.write(result)

                user_text = col1.text_area("The Complete Text",result, height=450)
                with st.expander("WebVTT"):
                        st.text_area("Format Web Video Text Tracks (WebVTT)", WebVTT, height=200)
        
                col1.download_button(
                            label=f"Download as txt",
                            data=result,
                            file_name=f'Transcribe YouTube Video {datetime.now()}.txt',
                            mime='text/plain'
                        )


        txt_path = f"{txt_directory}/output.txt" 
        file = open(txt_path, "r")
        # Read the contents of the file
        file_contents = file.read()

        # Close the file
        file.close()
        
        # st.text_area("The Summarized Text",sample_extractive_summarization([file_contents]), height=400)
        # #st.text_area("The Summarized Text",file_contents, height=400)
        # st.write()

        st.markdown("---")
        st.markdown("### Text summarization ")



        
        with st.spinner("Summarization ..."):
                extractive_summarization = summarize_with_cohere(file_contents)
        st.text_area("Summary: ", extractive_summarization)
        
        st.markdown("---")
        


        st.markdown("""### 🇳 🇪 🇷 (Named Entity Recognition)""")
        st.write("Named Entity Recognition (NER) is a natural language processing (NLP) task that involves identifying and classifying named entities within text into predefined categories. These entities can include names of people, organizations, locations, dates, quantities, and more as you can see in the photo.")
        st.image("images/NER.png")
        
        # Change it to use your custom NER function
      
        with st.spinner("NER (Named Entity Recognition) ..."):
                ner_entities = ner_spacy(file_contents)
                annotated_text(*[(ent.text, ent.label_) for ent in ner_entities])

        # Update this section to use the custom NER results and generate the graph
        
        with st.spinner("Generating and displaying the graph..."):
                save_path = 'output.html'  # Set the path where you want to save the graph
                get_graph(file_contents, save_path)
                st.subheader("Graph - NPM Dependencies")
                st.components.v1.html(open(save_path, 'r').read(), height=600, width=900)

        # Perform Named Entity Recognition (NER) and extract entities
        with st.spinner("Generating and displaying the word cloud..."):
            ner_entities = ner_spacy(file_contents)

        # Extract named entities and their counts
        ner_entity_counts = Counter([ent.text for ent in ner_entities])

        # Create a list of tuples containing (entity, count) for word cloud
        words = [(entity, count) for entity, count in ner_entity_counts.items()]

       # Create the word cloud
        wordcloud = (
            WordCloud()
            .add(
                "",
                words,
                word_size_range=[20, 100],
                textstyle_opts=opts.TextStyleOpts(font_family="cursive"),
            )
            .set_global_opts(title_opts=opts.TitleOpts(title=""))
        )

        # Save the word cloud as an HTML file
        wordcloud.render("wordcloud_ner.html")

        # Display the word cloud using Streamlit
        st.subheader("Word Cloud")
        with open("wordcloud_ner.html", "r") as f:
            html = f.read()
        st.components.v1.html(html, height=600, width=900)




        st.markdown("---")
        st.markdown("""### Sentiment Analysis 😃 😶 😡 """)
        st.write("""
        The `compound score` typically ranges from -1 to +1, where -1 indicates extremely negative sentiment, +1 indicates extremely positive sentiment, and 0 represents neutral sentiment.
            """)

        analyser = SentimentIntensityAnalyzer()
        score = analyser.polarity_scores(file_contents)
        polarity_vader = score['compound']

        mygrid2 = make_grid(1,3)
        with mygrid2[0][1]:
            st.markdown(f"##### Compound Score = {polarity_vader}")

        if polarity_vader > 0:
            st.write("The sentiment of this text is likely to be positive")
        elif polarity_vader == 0 :
            st.write("The sentiment of this text is likely to be neutral")
        else:
            st.write("The sentiment of this text is likely to be negative")
            
        # fig = plot_sentiment(polarity_vader)
        # # Display the plot in Streamlit
        # st.pyplot(fig)

# Create the gauge chart with different color segments
        gauge_chart = (
            Gauge()
            .add(
                "Sentiment",
                [("Sentiment", polarity_vader * 100)],
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(
                        color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=30
                    )
                ),
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Sentiment Gauge"),
                legend_opts=opts.LegendOpts(is_show=False),
            )
        )

        # Save the gauge chart as an HTML file
        gauge_chart.render("gauge_chart_color.html")

        # Read the HTML file and display its content using Streamlit
        with open("gauge_chart_color.html", "r") as f:
            gauge_html_color = f.read()
        st.components.v1.html(gauge_html_color, height=500, width=800)

    for i in range(20):
        st.write("")

    st.markdown("""
    ----
    **Contact** :

    Made with :heart: for Streamlit LLM Hackathon
    """)
