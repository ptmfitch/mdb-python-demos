[
  {
    $match: {
      _id: "MDB",
    },
  },
  {
    $lookup: {
      from: "graph-instruments",
      let: { pid: "$_id", },
      pipeline: [ { $match: {
        $expr: { $and: [
          { $eq: ["$product_id", "$$pid"], },
          { $eq: ["$active", false], },
        ], },
      }, }, ],
      as: "instruments",
    },
  },
  {
    $out: "graph-mat-view",
  },
]