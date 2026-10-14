# Best-so-far pattern: keep a "champion" and replace it when something beats it.
# Compare the SCORES inside the dictionaries, never the whole dictionaries.
students = [
    {"name": "Ali", "score": 85},
    {"name": "Sara", "score": 92},
    {"name": "Omar", "score": 67},
]

best = students[0]
for student in students:
    if student["score"] > best["score"]:
        best = student
print(best["name"])
    
        
