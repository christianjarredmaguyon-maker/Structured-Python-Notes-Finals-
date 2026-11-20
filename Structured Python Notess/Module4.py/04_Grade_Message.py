# INTERMEDIATE

# 4. Grade Message
grade = "A"

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case _:
        print("Invalid grade")