
experience = 2
languages = ["python", "typescript", "javascript", "java"]
concractType = "b2b"

if experience >= 2 and "python" and "java" in languages:
    print("Warunek 1 spelniony") 
    if concractType == "b2b" or "employment":
        print("Warunek 2 spelniony")
else:
    print("Oba warunki nie sa spelnione")