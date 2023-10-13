[
  {
    $match: {
      _id: "MDB",
    },
  },
  {
    $graphLookup: {
      from: "graph-instruments",
      startWith: "$_id",
      connectFromField: "product_id",
      connectToField: "product_id",
      as: "instruments",
      maxDepth: 1,
      depthField: "d",
      restrictSearchWithMatch: { active: false, },
    },
  },
  {
    $out: "graph-mat-view",
  }
]