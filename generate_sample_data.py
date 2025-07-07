import csv

# Read data from users.csv
users_data = []
with open('users.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        users_data.append(tuple(row))

# Read data from passwords.csv
passwords_data = []
with open('passwords.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        passwords_data.append(row[0])


# Write data to users.txt
with open('users.txt', 'w') as file:
    for user_data in users_data:
        file.write(','.join(user_data) + '\n')

# Write data to passwords.txt
with open('passwords.txt', 'w') as file:
    for password in passwords_data:
        file.write(password + '\n')


print("Data from CSV files has been written to text files successfully.")
