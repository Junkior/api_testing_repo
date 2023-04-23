ability_scores_schema = {
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
        },
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
        },
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
        },
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
        },
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
        },
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

ability_scores_charisma_schema = {
"type": "object",
  "properties": {
    "index": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "full_name": {
      "type": "string"
    },
    "desc": {
      "type": "array",
      "items": [
        {
          "type": "string"
        },
        {
          "type": "string"
        }
      ]
    },
    "skills": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "index": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "name",
            "index",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "index": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "name",
            "index",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "index": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "name",
            "index",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "index": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "name",
            "index",
            "url"
          ]
        }
      ]
    },
    "url": {
      "type": "string"
    }
  },
  "required": [
    "index",
    "name",
    "full_name",
    "desc",
    "skills",
    "url"
  ]
}
