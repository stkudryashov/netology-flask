
ADVERTISEMENT_CREATE = {
    "type": "object",
    "properties": {
        "title": {
            "type": "string"
        },
        "description": {
            "type": "string"
        },
        "user_id": {
            "type": "integer"
        },
    },
    "required": ["title", "description", "user_id"]
}
