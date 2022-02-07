import csv

students = open("student_scores.csv", "r")

outfile = open("student_avg.csv", "w")

student_file = csv.reader(students, delimiter=",")

for record in student_file:

    s1 = int(record[1])
    s2 = int(record[2])
    s3 = int(record[3])

    avg = round((s1 + s2 + s3) / 3, 2)

    avg = str(avg)
    outfile.write(record[0] + "'s Average: " + avg + "\n")
outfile.close()
