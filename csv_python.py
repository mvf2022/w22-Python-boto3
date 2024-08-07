import csv 

with open("test.csv", 'w',newline='') as f:
    writer = csv.writer(f)
    HEADER=['Name', 'Cell', 'Profession', 'Email']
    writer.writerow(HEADER)
    writer.writerow(['brandon', '555 555 5555', 'DevOps Engineer', 'hjasfgdfghc@gmail.com'])