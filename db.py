import json
import os

FILE = "data.json"

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def add_record(name, age, city):
    data = load()
    data.append({"name": name, "age": age, "city": city})
    save(data)
    print("✅ Record added!")

def view_records():
    data = load()

    if not data:
        print("No records found.")
        return

    print("\n📋 Records\n")
    for i, item in enumerate(data, start=1):
        print(f"{i}. {item['name']} | {item['age']} | {item['city']}")

def search_records(keyword):
    data = load()
    keyword = keyword.lower()

    results = [
        item for item in data
        if keyword in item['name'].lower()
        or keyword in item['city'].lower()
    ]

    if not results:
        print("No matching records found.")
        return

    print("\n🔍 Results\n")
    for item in results:
        print(f"- {item['name']} ({item['city']})")
