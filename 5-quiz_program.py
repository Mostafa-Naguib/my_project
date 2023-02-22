import csv

file = open("quiz.csv", "r")
reader = csv.DictReader(file)
next(reader)
print("Now we're going to ask you some question about computer science...")
score = 0
length = 0
for row in reader:
    length += 1
    ans = input(row["question"]).title().strip()
    if ans == row["answer"].title():
        print("Correct")
        score += 1
    else:
        print("Wrong")
        print(row["answer"])
print(f"Your score is {score} out of {length}")
file.close()
