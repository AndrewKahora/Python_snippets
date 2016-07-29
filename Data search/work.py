import csv
with open('MOCK_DATA.csv') as csvfile:
    idnumber = raw_input("Please enter your ID: ")  # Keying in the id number "
    data_reader = csv.reader(csvfile, delimiter=',')
    for row in data_reader:
        if idnumber == row[0]:
            print row[1] + ' ' + row[2] + ' '+ row[3]
            break
        else:
            pass


