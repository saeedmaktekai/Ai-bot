#import all required libraries 
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFDirectoryLoader
from dotenv import load_dotenv
load_dotenv()
#for splitting text into chunk 
from langchain_text_splitters import CharacterTextSplitter
#load openai embeddings because we are not using local embeddings
from langchain_openai import OpenAIEmbeddings
#get an environment variable 
import os
import chromadb
openai_api_key=os.getenv("OPENAI_API_KEY")

embeddings=OpenAIEmbeddings(openai_api_key=openai_api_key,model="text-embedding-3-large")
def injectdata(path):
   # load the document and split it into chunks
   loader = PyPDFDirectoryLoader("/Users/saeedanwar/Desktop/Ai-bot/data/")
   documents = loader.load()
   text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
   docs = text_splitter.split_documents(documents)
   new_client = chromadb.EphemeralClient()
   data = openai_lc_client = Chroma.from_documents(
   docs, embeddings, client=new_client, collection_name="openai_collection"
   )
   Chroma.from_documents(docs, embeddings, persist_directory="./chroma_db_openai")
   return data





directorypath="/Users/saeedanwar/Desktop/Ai-bot/data/"

data=injectdata(directorypath)
# query = "summary"
# docs = openai_lc_client.similarity_search(query)
# print(docs[0].page_content)

