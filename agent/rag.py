import json

def get_pricing_info():
    with open("data/knowledge.json", "r") as f:
        data = json.load(f)
    return data["pricing"]