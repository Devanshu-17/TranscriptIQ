# # pip install --upgrade --force-reinstall azure-ai-textanalytics
# from azure.core.credentials import AzureKeyCredential
# from azure.ai.textanalytics import (
#         TextAnalyticsClient,
#         RecognizeEntitiesAction,
#         RecognizePiiEntitiesAction,
#     )
# from dotenv import load_dotenv
# import streamlit as st
# # load_dotenv()
# # key1 = os.getenv('key1')
# # key2 = os.getenv('key2')
# # endpoint = os.getenv('endpoint')
# key1 = st.secrets["key1"]
# key2 = st.secrets["key2"]
# endpoint = st.secrets["endpoint"]



# # Authenticate the client using your key and endpoint 
# def authenticate_client():
#     ta_credential = AzureKeyCredential(key1)
#     text_analytics_client = TextAnalyticsClient(
#             endpoint=endpoint, 
#             credential=ta_credential)
#     return text_analytics_client


# def sample_extractive_summarization(document):
#     client = authenticate_client()
#     summary = []
#     poller = client.begin_extract_summary(document)
#     extract_summary_results = poller.result()
#     for result in extract_summary_results:
#         if result.is_error is True:
#             print("...Is an error with code '{}' and message '{}'".format(result.error.code, result.error.message))
#         else :
#             summary.append("\n".join([sentence.text for sentence in result.sentences]))
#     return "\n".join(summary)



# def sample_abstractive_summarization(document):
#     client = authenticate_client()
#     summary = []
#     poller = client.begin_abstract_summary(document)
#     abstract_summary_results = poller.result()
#     # summary.contexts
#     for result in abstract_summary_results:
#         if result.is_error is True:
#             print("...Is an error with code '{}' and message '{}'".format(result.error.code, result.error.message))
#         else :
#             summary.append("\n".join([summary.text for summary in result.summaries]))
#     return "\n".join(summary)


# def sample_annotated_text(document):
#     client = authenticate_client()
#     poller = client.begin_analyze_actions(
#             document,
#             display_name="Sample Text Recognize",
#             actions=[
#                 RecognizeEntitiesAction(),
#                 RecognizePiiEntitiesAction(),
#             ],
#         )
#     document_results = poller.result()
#     score_min = 0.5
#     sort_by_start_order = lambda tuple: tuple[0]

#     ner = [sorted(list(set([(entity.offset,entity.offset+entity.length,entity.category,entity.confidence_score) for result in action_results if result.is_error is False for entity in result.entities if (entity.confidence_score > score_min)])), key=sort_by_start_order) for action_results in document_results]
#     filtered_ner = [[tup[:-1] for tup in texte_ner if tup[3] == max([t[3] for t in texte_ner if t[0] == tup[0] or t[1] == tup[1] or ((t[1] > tup[1]) and (t[0] < tup[0])) or ((t[1] < tup[1]) and (t[0] > tup[0]))])] for texte_ner in ner]
    
#     return filtered_ner
    

# def sample_recognize_to_annotated_text(document):
#     filtered_ner = sample_annotated_text(document)
#     res =[]
#     for idx_texte,texte in enumerate(document):
#         position=0
#         for (start,stop,category) in filtered_ner[idx_texte]:
#             if texte[position:start] !='':
#                 res.append((texte[position:start], ''))
#             res.append((texte[start:stop], category))
#             position = stop
#         res.append((texte[stop:], ''))
#         res.append(('\n',''))
#     return res[:-1]




# def sample_recognize(document):
#     client = authenticate_client()
#     poller = client.begin_analyze_actions(
#             document,
#             display_name="Sample Text Recognize",
#             actions=[
#                 RecognizeEntitiesAction(),
#                 RecognizePiiEntitiesAction(),
#             ],
#         )
#     document_results = poller.result()
#     score_min = 0.5
#     sort_by_start_order = lambda tuple: tuple[0]

#     ner = [sorted(list(set([(entity.offset,entity.offset+entity.length,entity.category,entity.text,entity.confidence_score) for result in action_results if result.is_error is False for entity in result.entities if (entity.confidence_score > score_min)])), key=sort_by_start_order) for action_results in document_results]
    
#     filtered_ner = [[tup[:-1] for tup in texte_ner if tup[4] == max([t[4] for t in texte_ner if t[0] == tup[0] or t[1] == tup[1] or ((t[1] > tup[1]) and (t[0] < tup[0])) or ((t[1] < tup[1]) and (t[0] > tup[0]))])] for texte_ner in ner]
#     return filtered_ner


# def list_to_dict(document):
#     var_dict = {}
#     var = sample_recognize(document)
#     for sublist in var:
#         for tuple_item in sublist:
#             entity_type = tuple_item[2]
#             entity_value = tuple_item[3]
            
#             if entity_type in var_dict:
#                 var_dict[entity_type].append(entity_value)
#             else:
#                 var_dict[entity_type] = [entity_value]
#     return var_dict
    

######################################################################################################
# Above section is for Azure Text Analytics API
# Following section is for Cohere API using Clarifai
######################################################################################################


from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2

def summarize_with_cohere(text):
    # Cohere credentials and model details
    PAT = '5ec7ba9db93d49af8fd2275ef6dc9af7'  
    USER_ID = 'cohere'
    APP_ID = 'summarize'
    MODEL_ID = 'cohere-summarize'
    MODEL_VERSION_ID = 'bc1d5f9cc2834571b1322f572aca2305'


    channel = ClarifaiChannel.get_grpc_channel()
    stub = service_pb2_grpc.V2Stub(channel)

    metadata = (('authorization', 'Key ' + PAT),)

    # Create the input for Cohere summarization
    input_data = resources_pb2.Input(
        data=resources_pb2.Data(
            text=resources_pb2.Text(
                raw=text
            )
        )
    )

    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            user_app_id=resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID),
            model_id=MODEL_ID,
            version_id=MODEL_VERSION_ID,
            inputs=[input_data]
        ),
        metadata=metadata
    )

    if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        raise Exception(f"Post model outputs failed, status: {post_model_outputs_response.status.description}")

    # Extract the summary from Cohere response
    summary = post_model_outputs_response.outputs[0].data.text.raw
    return summary

# Example usage
document = 'A wiki (/wki/ i WIK-ee) is an online hypertext publication collaboratively edited and managed by its own audience, using a web browser. A typical wiki contains multiple pages for the subjects or scope of the project, and could be either open to the public or limited to use within an organization for maintaining its internal knowledge base. Wikis are enabled by wiki software, otherwise known as wiki engines. A wiki engine, being a form of a content management system, differs from other web-based systems such as blog software, in that the content is created without any defined owner or leader, and wikis have little inherent structure, allowing structure to emerge according to the needs of the users.[1] Wiki engines usually allow content to be written using a simplified markup language and sometimes edited with the help of a rich-text editor.[2] There are dozens of different wiki engines in use, both standalone and part of other software, such as bug tracking systems. Some wiki engines are free and open-source, whereas others are proprietary. Some permit control over different functions (levels of access); for example, editing rights may permit changing, adding, or removing material. Others may permit access without enforcing access control. Further rules may be imposed to organize content. There are hundreds of thousands of wikis in use, both public and private, including wikis functioning as knowledge management resources, note-taking tools, community websites, and intranets. Ward Cunningham, the developer of the first wiki software, WikiWikiWeb, originally described wiki as "the simplest online database that could possibly work".[3] "Wiki" (pronounced [wiki][note 1]) is a Hawaiian word meaning "quick".[4][5][6] The online encyclopedia project Wikipedia is the most popular wiki-based website, and is one of the most widely viewed sites in the world, having been ranked in the top twenty since 2007.[7] Wikipedia is not a single wiki but rather a collection of hundreds of wikis, with each one pertaining to a specific language. The English-language Wikipedia has the largest collection of articles: as of July 2023, it has over 6 million articles.'
summary = summarize_with_cohere(document)
print("Summary:\n", summary)


# Example Output

# Summary:
#  - A wiki is an online, collaboratively edited, and managed hypertext publication.
# - A wiki engine is a form of content management system that enables the easy creation and editing of interlinked web pages.
# - Ward Cunningham, the developer of the first wiki software, described wiki as "the simplest online database that could possibly work".
# - "Wiki" is a Hawaiian word meaning "quick".
# - The online encyclopedia project Wikipedia is the most popular wiki-based website.
# - Wikipedia is a collection of hundreds of wikis, with each one pertaining to a specific language.
# - The English-language Wikipedia has the largest collection of articles.
