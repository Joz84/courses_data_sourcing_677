import csv

### READ

with open('data/addresses.csv') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    for row in reader:
        print(row[2])

with open('data/biostats.csv') as csvfile:
    reader = csv.DictReader(csvfile, skipinitialspace=True)
    for row in reader:
        print(row['Name'], row['Sex'], int(row['Age']))
        

### WRITE
     
beatles = [
    { 'first_name': 'John', 'last_name': 'lennon', 'instrument': 'guitar'},
    { 'first_name': 'Ringo', 'last_name': 'Starr', 'instrument': 'drums'}
]

headers = beatles[0].keys()
headers = ['first_name', 'last_name','instrument']
with open('data/beatles.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    # writer.writerow({ 'first_name': 'John', 'last_name': 'lennon', 'instrument': 'guitar'})
    # writer.writerow({ 'first_name': 'Ringo', 'last_name': 'Starr', 'instrument': 'drums'})
    for beatle in beatles:
          writer.writerow(beatle)
    