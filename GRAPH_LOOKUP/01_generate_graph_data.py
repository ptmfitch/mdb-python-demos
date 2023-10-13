# Generates 2 collections of related products and instruments
# 1. Products with id and timestamp
# 2. Instruments with id, product_id, timestamp, and active boolean
# See 02a_products_instruments_graph_lookup.js for how to join
# WARNING Deletes old graph-products and graph-instruments collections

import random
import string
from datetime import datetime
from pymongo import MongoClient

CONNECTION_STRING = 'mongodb+srv://<username>:<password>@<hostname>/test'
DATABASE = 'demo-graph-lookup'

# Min and max instruments per product
MIN_INST = 5
MAX_INST = 15

print("Connecting to MongoDB Atlas cluster")

connection = MongoClient(CONNECTION_STRING)
database = connection[DATABASE]

print("Dropping old graph collections")

database.drop_collection('graph-products')
database.drop_collection('graph-instruments')

print("Creating new graph collections")

products_col = database['graph-products']
instruments_col = database['graph-instruments']

print("Creating new product_id index")

# Create an index on the field we will join on
instruments_col.create_index("product_id")


# Generate a list of all possible strings from AAA to ZZZ
def generate_all_3_letter_strings():
    letters = string.ascii_uppercase
    all_strings = []

    for first_letter in letters:
        for second_letter in letters:
            for third_letter in letters:
                three_letter_string = first_letter + second_letter + third_letter
                all_strings.append(three_letter_string)

    return all_strings


def generate_product(product_id):
  return {
    '_id': product_id,
    'created_date': datetime.now()
  }


def generate_instrument(product_id):
  return {
    'product_id': product_id,
    'active': random.choice([True, False]),
    'created_date': datetime.now()
  }


print("Generating products")

products = [generate_product(p) for p in generate_all_3_letter_strings()]

print("Generating instruments")

instruments = []
for product in products:
  # Create between a min and a max no. of instruments per product
  for _ in range(random.choice(range(MIN_INST, MAX_INST))):
    instruments.append(generate_instrument(product['_id']))

print("Inserting products")

products_col.insert_many(products)

print("Inserting instruments")

instruments_col.insert_many(instruments)

print("Done")
