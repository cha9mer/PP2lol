import json
import re

def resolve_query(data, query):
    parts = re.findall(r'\w+|\[\d+\]', query)
    current = data
    for part in parts:
        if part.startswith('['):
            index = int(part[1:-1])
            if isinstance(current, list) and 0 <= index < len(current):
                current = current[index]
            else:
                return "NOT_FOUND"
        else:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return "NOT_FOUND"
    return json.dumps(current, separators=(',', ':'))

data = json.loads(input())
q = int(input())

for _ in range(q):
    query = input()
    print(resolve_query(data, query))