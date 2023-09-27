import sys
import os

import pinecone

from llama_index import VectorStoreIndex,SimpleDirectoryReader
from llama_index.vector_stores import PineconeVectorStore
from llama_index.storage.storage_context import StorageContext

from llama_index.embeddings import OpenAIEmbedding


from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # This loads the .env file in the root directory of the project

api_key = os.environ['PINECONE_API_KEY']

# Get the API key from the environment variable
import openai
openai.api_key = os.environ['OPENAI_API_KEY']

embed_model = OpenAIEmbedding()
pinecone.init(api_key=api_key,environment="asia-southeast1-gcp-free")
# pinecone.create_index("baoxian", dimension=1536, metric="euclidean", pod_type="p1")
pinecone_index = pinecone.Index("baoxian")

documents = SimpleDirectoryReader(input_dir="D:\\test\\sparke\\word\\").load_data()

vector_store = PineconeVectorStore(pinecone_index=pinecone_index)

storage_content = StorageContext.from_defaults(vector_store=vector_store)

index = VectorStoreIndex.from_documents(documents,storage_context=storage_content)


queryembed = embed_model.get_query_embedding("阿富汗的政治风险有哪些？")

response = pinecone_index.query(
  vector=queryembed,
  top_k=3,
  include_values=True
)

print(response)
# query_engine = index.as_query_engine()
# response = query_engine.query("")