from database import injectdata

query = "summary of book"
docs = injectdata.similarity_search(query)
print(docs[0].page_content)