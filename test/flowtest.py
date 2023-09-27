import sparke

client = sparke.PersistentClient("d:\\test")
# list all collections
# list = client.list_collections()
# print(list)
# # make a new collection
# collection = client.create_collection("testname1")

# get an existing collection
collection = client.get_collection("testname1")

# # get a collection or create if it doesn't exist already
# collection = client.get_or_create_collection("testname")

# delete a collection
# client.delete_collection("testname")

# add new items to a collection
# either one at a time

#create a 1536 dimension vector
embeddingvestor = [0.1]*1536

# collection.add(
#     embeddings=embeddingvestor,
#     metadatas={"uri": "img9.png", "style": "style1"},
#     documents="doc1000101",
#     ids="uri9",
# )
# or many, up to 100k+!
# collection.add(
#     embeddings=[[1.5, 2.9, 3.4], [9.8, 2.3, 2.9]],
#     metadatas=[{"style": "style1"}, {"style": "style2"}],
#     ids=["uri9", "uri10"],
# )
# collection.add(
#     documents=["doc1000101", "doc288822"],
#     metadatas=[{"style": "style1"}, {"style": "style2"}],
#     ids=["uri9", "uri10"],
# )

# do nearest neighbor search to find similar embeddings or documents, supports filtering
response = collection.query(
    query_embeddings=embeddingvestor,
    n_results=2,
    # where={"style": "style2"}
)

print(response)