# Cursor pagination in MongoDB using batch_size to read data in chunks
# Set skip to the offset, i.e. page_index x page_size
# Set batch_size to the page_size, i.e. no. items you want to return per page
# This example uses data from the GRAPH_LOOKUP demo

from pymongo import MongoClient

CONNECTION_STRING = 'mongodb+srv://<username>:<password>@<hostname>/test'
DATABASE = 'demo-graph-lookup'

print("Connecting to MongoDB Atlas cluster")

connection = MongoClient(CONNECTION_STRING)
database = connection[DATABASE]

collection = database['graph-products']

page_size = 10

results = collection.find({}, batch_size=page_size)

# See https://stackoverflow.com/questions/54815892/pymongo-cursor-batch-size
def yield_rows(cursor, chunk_size):
    chunk = []
    for i, row in enumerate(cursor):
        if i % chunk_size == 0 and i > 0:
            yield chunk
            del chunk[:]
        chunk.append(row)
    yield chunk

chunks = yield_rows(results, page_size)
for chunk in chunks:
    # do processing here
    pass
