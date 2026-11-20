# HARD

# 7. Student Remarks
score = 85

match score:
    case n if n >= 90:
        print("Outstanding")
    case n if n >= 80:
        print("Very Good")
    case n if n >= 75:
        print("Passed")
    case n if n >= 0:
        print("Failed")
    case _:
        print("Invalid score")