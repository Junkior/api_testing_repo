ability_scores_schema_positive = {
    "type": "object",
    "properties": {
        "count": {"type": "integer"},
        "results": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "index": {"type": "string"},
                    "name": {"type": "string"},
                    "url": {"type": "string"}
                },
                "required": ["index", "name", "url"]
            }
        }
    },
    "required": ["count", "results"]
}

ability_scores_schema_negative = {
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


