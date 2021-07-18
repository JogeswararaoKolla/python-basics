# using Dictionaries to represent an objects
contacts = {
    "num_of_students": 2,
    "students": [  # List of dictionaries objects
        {"name": "Jogeswararao Kolla", "email": "Joges@example.com"},
        {"name": "Humisha Kolla", "email": "Humisha@example.com"},
    ]
}

for student in contacts['students']:
    print(student)  # print student dictonaries objects
    print(student["email"])
