import sparke

client = sparke.PersistentClient("d:\\test")
# list all collections
list = client.list_collections()
print(list)
# make a new collection
collection = client.create_collection("testname")

# get an existing collection
collection = client.get_collection("testname")

# get a collection or create if it doesn't exist already
collection = client.get_or_create_collection("testname")

# delete a collection
client.delete_collection("testname")