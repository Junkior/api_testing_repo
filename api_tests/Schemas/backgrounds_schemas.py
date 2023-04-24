background_schema = {
 "type": "object",
  "properties": {
    "count": {
      "type": "integer"
    },
    "results": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "index": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "index",
            "name",
            "url"
          ]
        }
      ]
    }
  },
  "required": [
    "count",
    "results"
  ]
}


background_schema_negative = {
"type": "object",
  "properties": {
    "error": {
      "type": "string"
    }
  },
  "required": [
    "error"
  ]
}