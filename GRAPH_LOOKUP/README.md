# GRAPH_LOOKUP

## Summary

Example showing how to use $graphLookup or $lookup to join documents across 2
collections and optionally perform deletions on created array elements

## Steps

1. Run 01_generate_graph_data.py to generate the 2 collections (WARNING: This
will delete the collections if they already exist)
2. Connect to your MongoDB instance via Compass or mongosh and use the
demo-graph-lookup database
3. Copy the aggregation pipeline from 02a_products_instruments_graph_lookup.js
and run it against the graph-products collection, this will $out results into a
3rd collection, graph-mat-view
4. (Optional) Run 03_delete_from_array.py to delete matching elements from the
instruments array in the graph-mat-view collection

## Notes

Compare 02b_products_instruments_lookup.js to see the equivalent $lookup syntax

## Documentation

[$graphLookup](https://www.mongodb.com/docs/manual/reference/operator/aggregation/graphLookup/)  

[$lookup](https://www.mongodb.com/docs/manual/reference/operator/aggregation/lookup/)  

[$pull](https://www.mongodb.com/docs/manual/reference/operator/update/pull/)