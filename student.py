students = [
    {"Name": "Riya", "Roll No": 101, "Course": "B.Sc Computer Science"},
    {"Name": "Arjun", "Roll No": 102, "Course": "B.Com"},
]
print("--- Student Details ---")
for s in students:
    print(f"Name: {s['Name']}, Roll No: {s['Roll No']}, Course: {s['Course']}")