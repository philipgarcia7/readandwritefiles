import csv

students = open("student_scores.csv", "r")

outfile = open("student_avg.csv", "w")

customer_file = csv.reader(customers, delimiter=",")
