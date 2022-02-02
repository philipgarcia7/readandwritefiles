import csv

customers = open("customers.csv", "r")

outfile = open("customer_country.csv", "w")

customer_file = csv.reader(customers, delimiter=",")

# to skip a line if the file contains a header record
n = -1
for record in customer_file:
    outfile.write(record[1] + "," + record[2] + "," + record[4] + "\n")
    n += 1
print("Customer Count:", n)
outfile.close()
