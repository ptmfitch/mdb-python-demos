# Simple pagination in MongoDB using skip and limit
# Set skip to the offset, i.e. page_index x page_size
# Set limit to the page_size, i.e. no. items you want to return per page
# This example uses data from the GRAPH_LOOKUP demo

from pymongo import MongoClient

CONNECTION_STRING = 'mongodb+srv://<username>:<password>@<hostname>/test'
DATABASE = 'demo-graph-lookup'

print("Connecting to MongoDB Atlas cluster")

connection = MongoClient(CONNECTION_STRING)
database = connection[DATABASE]

collection = database['graph-products']

page_size = 10
skip = 0

# Print the first 3 pages
for page_index in range(0, 3):
  print(f"Page {page_index + 1}:")
  results = collection.find({}, skip=skip, limit=page_size)
  # Add a breakpoint here to page through results
  for r in results:
    print(r)
  print()
  skip += page_size
