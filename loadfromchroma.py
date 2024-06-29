from database import injectdata
from database import retreiveembedding
# path="/Users/saeedanwar/Desktop/Ai-bot/data"
# injectdata(path)

query="who is marjan "
smsearch=retreiveembedding(query)
print(smsearch)
# print(type(smsearch))



