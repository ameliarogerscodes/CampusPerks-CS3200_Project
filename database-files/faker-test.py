from faker import Faker

fake = Faker()
num_rows = 5  # how many fake rows you want

with open("database-files/faker.sql", "w") as f:
    f.write("USE 'schema-name'\n")
    for i in range(1, num_rows + 1):
        f.write("INSERT INTO 'users' ('id', 'name', 'email', 'address') VALUES ")
        name = fake.name().replace("'", "''")  # escape single quotes
        email = fake.email()
        address = fake.address().replace("\n", ", ").replace("'", "''")
        
        line = f"({i}, '{name}', '{email}', '{address}')"
        print(line)
        if i < num_rows:
            line += ",\n"
        else:
            line += ";\n"
        f.write(line)

