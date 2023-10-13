# Deletes the last element from the instruments array using $pull and a filter
# on _id
# Run 02a_products_instruments_graph_lookup.js first to create the
# graph-mat-view collection

from pymongo import MongoClient

CONNECTION_STRING = 'mongodb+srv://<username>:<password>@<hostname>/test'
DATABASE = 'demo-graph-lookup'

print("Connecting to MongoDB Atlas cluster")

connection = MongoClient(CONNECTION_STRING)
database = connection[DATABASE]

collection = database['graph-mat-view']

example_doc = collection.find_one({})

id_to_delete = ""
print("Instrument ids before deletion")
for instrument in example_doc['instruments']:
  print(instrument['_id'])
  id_to_delete = instrument['_id']

result = collection.update_one(
  {"_id": example_doc["_id"]},
  # Can be expanded to match multiple fields per array element
  {"$pull": {"instruments": {"_id": id_to_delete}}}
)

example_doc = collection.find_one({})

print("Instrument ids after deletion")
for instrument in example_doc['instruments']:
  print(instrument['_id'])
