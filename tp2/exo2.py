classDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# Name of students
classDict["class"]["student"]["name"]

# Mike grade physics replaced by 89
classDict["class"]["student"]["marks"]["physics"] = 89

# Mike average grade added to class
students = classDict["class"]["student"]
classDict["class"]["student"]["average"] = sum(m for m in students["marks"].values()) / len(students["marks"])

# making a list of student for simplier understadning and also adding new entries
classDict["class"]["student"] = [classDict["class"]["student"]]

students = classDict["class"]["student"]


# Adding new student
classDict["class"]["student"].append({"name": "Ted"})
classDict["class"]["student"][1]["marks"]= {"physics":34, 'history' :99}
# Average of said students
classDict["class"]["student"][1]["average"] = sum(students[1]["marks"].values()) / len(students[1]["marks"])

# Average of all class
classDict["class"]["average_grade"] = sum(stud["average"] for stud in students) / len(students)

print(classDict)
