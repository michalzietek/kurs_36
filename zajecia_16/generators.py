users = [{
        "name": "Jan",
        "age": 20,
        "email": "jan.kowalski@gmail.com",
        "address": "Warszawa, Polska",
        "zip_code": "00-001",
        "city": "Warszawa",
        "country": "Polska",
    },
    {
        "name": "Anna",
        "age": 25,
        "email": "anna.nowak@gmail.com",
        "address": "Kraków, Polska",
        "zip_code": "31-001",
        "city": "Kraków",
        "country": "Polska",
    }
]

def address_parser_for_users(users):
    parsed_users = []
    for user in users:
        parsed_users.append({
            "name": user.get("name"),
            "age": user.get("age"),
            "email": user.get("email"),
            "full_address": user.get("address") + ", " + user.get("zip_code") + " " + user.get("city") + ", " + user.get("country")
        })
    return parsed_users

# users_in_our_system = address_parser_for_users(users)
# print(type(users_in_our_system))
# print(users_in_our_system)
# print(type(users_in_our_system))
# user_1 = address_parser_for_users(users)
# print(user_1)
# user_2 = address_parser_for_users(users)
# print(user_2)

# adam = users[0]
# anna = users[1]

def address_parser_for_users_generator(users):
    for user in users:
        yield {
            "name": user.get("name"),
            "age": user.get("age"),
            "email": user.get("email"),
            "full_address": user.get("address") + ", " + user.get("zip_code") + " " + user.get("city") + ", " + user.get("country")
        }

generator = address_parser_for_users_generator(users)
# print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))
for user in generator:
    print(user)