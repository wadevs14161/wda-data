# Azure Text Analytics
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
import configparser

#Config Parser
config = configparser.ConfigParser()
config.read('.config.ini')

#Config Azure Analytics
credential = AzureKeyCredential(config['AzureLanguage']['API_KEY'])

def azure_sentiment(user_input):
    text_analytics_client = TextAnalyticsClient(
        endpoint=config['AzureLanguage']['END_POINT'], 
        credential=credential)
    documents = [user_input]
    response = text_analytics_client.analyze_sentiment(
        documents, 
        show_opinion_mining=True,
        language="zh-hant")
    print(response)
    docs = [doc for doc in response if not doc.is_error]
    for idx, doc in enumerate(docs):
        print(f"Document text : {documents[idx]}")
        print(f"Overall sentiment : {doc.sentiment}")

    return docs[0].sentiment


if __name__ == "__main__":
    user_input = "習近平, 我幹你娘"
    azure_sentiment(user_input)