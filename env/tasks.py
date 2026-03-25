def get_tasks():
    return [
        {
            "name": "easy",
            "description": "Classify email correctly",
            "required_fields": ["classification"]
        },
        {
            "name": "medium",
            "description": "Classify and assign priority",
            "required_fields": ["classification", "priority"]
        },
        {
            "name": "hard",
            "description": "Full email response task",
            "required_fields": ["classification", "priority", "response"]
        }
    ]