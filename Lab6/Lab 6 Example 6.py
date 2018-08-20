def process_scores(f):
    number_of_students = 1
    total = 0
    highest_scorer = f.readline().strip().split(",")
    highest_scorer[1] = int(highest_scorer[1])
    total = total + highest_scorer[1]
    lowest_scorer = highest_scorer
    for i in f:
        details = i.strip().split(",")
        details[1] = int(details[1])
        total += details[1]
        number_of_students += 1
        if details[1] > highest_scorer[1]:
            highest_scorer = details
        elif details[1] < lowest_scorer[1]:
            lowest_scorer = details
    return highest_scorer[0], lowest_scorer[0], float(total) / number_of_students

f = open("Scores.txt","r")
print(process_scores(f))
f.close()
