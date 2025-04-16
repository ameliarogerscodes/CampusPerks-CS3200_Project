from faker import Faker
from faker.providers import DynamicProvider
import random

cities_provider = DynamicProvider(
     provider_name="cities",
     elements=["Boston", "New York", "Chicago", "Miami", "San Francisco"],
)

colleges_provider = DynamicProvider(
     provider_name="colleges",
     elements=["Northeastern", "Fordham", "Northwestern", "UMiami", "UCBerkeley"],
)

states_provider = DynamicProvider(
     provider_name="states",
     elements=["Massachusetts", "New York", "Illinois", "Florida", "California"],
)

street_address_provider = DynamicProvider(
     provider_name="street_addresses",
     elements=["458 Huntington Ave", "14 Baker St", "199 High St", "15 Fruit St", "12 Summit Pl"],
)

zipcode_provider = DynamicProvider(
     provider_name="zipcodes",
     elements=["01950", "02110", "90210", "11111", "77777"],
)

store_name_provider = DynamicProvider(
     provider_name="stores",
     elements=["Wollastons", "Panera", "Aroma Joes", "Star Market", "Target"],
)

club_name_provider = DynamicProvider(
     provider_name="clubs",
     elements=["Society of Women in Tech", "Badminton Club", "Trivia Club", "Phi Delta Theta", "Film Club"],
)

colleges1 = ["Northeastern", "Fordham", "Northwestern", "UMiami", "UCBerkeley"]
colleges2 = ["Northeastern", "Fordham", "Northwestern", "UMiami", "UCBerkeley"]
price_ranges = ['$', '$$', '$$$']
hours = ['7:00am-12:00am', '10:00am-5:00pm', '12:00pm-9:00pm', '11:00am-11:00pm']
categories = ['convenience', 'grocery', 'food', 'clothing']
items = ['clothing', 'coffee', 'books', 'produce', 'furniature']
sDates = ['2025-04-14', '2025-03-20', '2025-03-30', '2025-02-18']
eDates = ['2025-04-15', '2025-05-05', '2025-06-01', '2025-05-10']
codes = ['BIGSALE', 'BUYBUYBUY', 'SALECODE', 'REDEEMCODE', 'SPRINGSALE']
birthdates = ['2000-04-15', '2001-05-05', '2002-06-01', '2003-05-10', '1999-09-12', '2005-11-11']
all_usernames = []
admin_users = []

fake = Faker()
fake.add_provider(cities_provider)
fake.add_provider(colleges_provider)
fake.add_provider(states_provider)
fake.add_provider(street_address_provider)
fake.add_provider(zipcode_provider)
fake.add_provider(store_name_provider)
fake.add_provider(club_name_provider)



location_rows = 5  
college_rows = 5
club_rows = 5
store_rows = 5
discount_rows = 10
user_rows = 10
saved_discount_rows = 10
admin_rows = 2

# path for project: "database-files/faker.sql"
# personal path: "C:/Users/Emma/Documents/faker-stuff-output.sql"
with open("faker.sql", "w") as f:
    print("✅ Writing to:", f.name)
    f.write("USE campusPerks_db;\n")

    # add locations
    for i in range(1, location_rows + 1):
        f.write("INSERT INTO location (locationId, streetAddress, city, state, country, zipcode)\nVALUES ")
        strAdd = fake.street_addresses().replace("'", "''")
        city = fake.cities().replace("'", "''")
        state = fake.states().replace("'", "''")
        zipcode = fake.zipcodes().replace("'", "''")
        
        line = f"({i}, '{strAdd}', '{city}', '{state}', 'USA', '{zipcode}')"
        print(line)
        if i < location_rows:
            line += ",\n"
        else:
            line += ";\n"
        f.write(line)

    # add colleges
    for i in range(1, college_rows + 1):
        f.write("INSERT INTO college (collegeName, locationId, noOfStores, noOfUsers, domain)\nVALUES ")
        cn = random.choice(colleges1)
        colleges1.remove(cn)
        lId = random.randint(1, location_rows)
        noOfStores = 0
        noOfUsers = 0
        domain = "@" + cn.replace("''", "") + ".edu"
        
        line = f"('{cn}', {lId}, {noOfStores}, {noOfUsers}, '{domain}')"
        print(line)
        if i < college_rows:
            line += ",\n"
        else:
            line += ";\n"
        f.write(line)
        
    # add stores
    for i in range(1, store_rows + 1):
        f.write("INSERT INTO store (storeId, name, locationId, priceRange, noOfDiscounts," +
                "hoursOfOperations, category, phoneNo, website, starRating, delivery, ageRestricted," +
                "totalSales, noOfOrders, college, clubId)\nVALUES ")
        name = fake.stores().replace("'", "''")
        lId2 = random.randint(1, location_rows)
        pr = random.choice(price_ranges)
        ho = random.choice(hours)
        cat = random.choice(categories)
        phone = fake.phone_number().replace("'", "''")
        web = fake.domain_name()
        rate = random.randint(1, 5)
        de = random.randint(0, 1)
        ar = random.randint(0, 1)
        ts = random.randint(0, 20000)
        no = random.randint(0, 500)
        col = fake.colleges().replace("'", "''")
        
        line = f"({i}, '{name}', {lId2}, '{pr}', 0, '{ho}', '{cat}', '{phone}', '{web}', {rate}, {de}, {ar}, {ts}, {no}, '{col}', NULL)"
        print(line)
        if i < store_rows:
            line += ",\n"
        else:
            line += ";\n"
        f.write(line)    
    
        
    # add clubs
    for i in range(1, club_rows + 1):
        f.write("INSERT INTO club (clubId, name, college, storeId, numberOfUsers)\nVALUES ")
        name = fake.clubs().replace("'", "''")
        college = random.choice(colleges2)
        colleges2.remove(college)
        
        line = f"({i}, '{name}', '{college}', NULL, 0)"
        print(line)
        if i < club_rows:
            line += ",\n"
        else:
            line += ";\n"
        f.write(line)
    
    
    # add discounts
    for i in range(1, discount_rows + 1):
        f.write("INSERT INTO discount (discountId, storeId, code, percentOff, item, startDate," + 
                " endDate, ageRestricted, minPurchase, bdayDiscount)\nVALUES ")
        stId = random.randint(1, store_rows)
        code = random.choice(codes)
        pOff = random.randint(1, 99)
        item = random.choice(items)
        sDate = random.choice(sDates)
        eDate = random.choice(eDates)
        ageR = random.randint(0, 1)
        minP = random.randint(0, 100)
        bday = random.randint(0, 1)
        
        
        line = f"({i}, {stId}, '{code}', {pOff}, '{item}', '{sDate}', '{eDate}', {ageR}, {minP}, {bday})"
        print(line)
        if i < discount_rows:
            line += ",\n"
        else:
            line += ";\n"
        f.write(line)

    
    # add users 
    for i in range(1, user_rows + 1):
        f.write("INSERT INTO user (username, firstName, lastName, password, college, email, phoneNo, birthdate, " +
                " age, discountsUsed, clubId) VALUES ")
        firstName = fake.first_name().replace("'", "''")
        lastName = fake.last_name().replace("'", "''")
        username = firstName.replace("''", "") + lastName.replace("''", "") + str(random.randint(0, 200))
        all_usernames.append(username)
        password = fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
        cg = fake.colleges().replace("'", "''")
        em = username.replace("''", "") + "@" + cg.replace("''", "") + ".edu"
        phn = fake.phone_number().replace("'", "''")
        birdat = random.choice(birthdates)
        age = random.randint(18, 30)
        cluId = random.randint(1, club_rows)
        
        line = f"('{username}', '{firstName}', '{lastName}', '{password}', '{cg}', '{em}', '{phn}', '{birdat}', {age}, {cluId})"
        print(line)
        if i < user_rows:
            line += ",\n"
        else:
            line += ";\n"
        f.write(line)
        

    # add saved discounts
    for i in range(1, saved_discount_rows + 1):
        f.write("INSERT INTO discount_used (username, discountId)\nVALUES ")
        us = random.choice(all_usernames)
        disId = random.randint(1, discount_rows)
        
        line = f"('{us}', {disId})"
        print(line)
        if i < saved_discount_rows:
            line += ",\n"
        else:
            line += ";\n"
        f.write(line)

     # add admin
    for i in range(1, admin_rows + 1):
        f.write("INSERT INTO admin (username, firstName, lastName, password, email, phoneNo, " +
                " supportUser, supportClub, supportStore)\nVALUES")
        fn = fake.first_name().replace("'", "''")
        ln = fake.last_name().replace("'", "''")
        usern = fn.replace("''", "") + ln.replace("''", "") + str(random.randint(0, 200))
        admin_users.append(usern)
        pw = fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
        eml = usern.replace("''", "") + "@gmail.com"
        phnn = fake.phone_number().replace("'", "''")
        sUser = random.choice(all_usernames)
        sClub = random.randint(1, club_rows)
        sStore = random.randint(1, store_rows)
        
        line = f"('{usern}', '{fn}', '{ln}', '{pw}', '{eml}', '{phnn}', '{sUser}', {sClub}, {sStore})"
        print(line)
        if i < admin_rows:
            line += ",\n"
        else:
            line += ";\n"
        f.write(line)
    