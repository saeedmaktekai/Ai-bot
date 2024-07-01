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
from fastapi import FastAPI
app = FastAPI

embeddings=OpenAIEmbeddings(openai_api_key=openai_api_key,model="text-embedding-3-large")
def injectdata(path):
   # load the document and split it into chunks
   loader = PyPDFDirectoryLoader(path)
   documents = loader.load()
   text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
   docs = text_splitter.split_documents(documents)
   new_client = chromadb.EphemeralClient()
   data = openai_lc_client = Chroma.from_documents(
   docs, embeddings, client=new_client, collection_name="openai_collection"
   )
   Chroma.from_documents(docs, embeddings, persist_directory="./db")
   return docs 

@app.post("/upload/")





def retreiveembedding(query):
   db3 = Chroma(persist_directory="./chroma_db_openai", embedding_function=embeddings)
   docs = db3.similarity_search(query)
   return docs
def lookforsimilaritysearch(query):
   # load from disk
   data = Chroma(persist_directory="./chroma_db_openai", embedding_function=embeddings)
   data.similarity_search(query)
   return data


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)




