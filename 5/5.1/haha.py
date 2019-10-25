import json

print(json.dumps([["B" for i in range(19)] if j < 15 else ["W" for i in range(19)] for j in range(19)]))