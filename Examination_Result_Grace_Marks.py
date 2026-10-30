telugu = int(input("Enter Telugu marks: "))
english = int(input("Enter English marks: "))
python = int(input("Enter Python marks: "))

if telugu >= 35 and english >= 35 and python >= 35:
    result = "Pass"
else:
    result = "Fail"

print("Student Examination Result")
print("Result:", result)