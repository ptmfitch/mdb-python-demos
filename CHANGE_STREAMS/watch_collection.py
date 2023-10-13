# Watch for changes to the demo-change-streams.streaming collection

from pymongo import MongoClient

CONNECTION_STRING = 'mongodb+srv://<username>:<password>@<hostname>/test'
DATABASE = 'demo-change-streams'

print("Connecting to MongoDB Atlas cluster")

connection = MongoClient(CONNECTION_STRING)
database = connection[DATABASE]

collection = database['streaming']

print("Watching collection")

with collection.watch() as stream:
  for change in stream:
      print(change)
