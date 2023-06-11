class UsernameNotUniqueError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class UnderageUserError(Exception):
    pass

class InvalidEmailError(Exception):
    pass

class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

def add_user_to_directory(user_data):
    user_directory = []

    for data in user_data:
        try:
            username, email, age = data

            if not is_unique_username(user_directory, username):
                raise UsernameNotUniqueError("Username is not unique: " + username)

            if not is_positive_integer(age):
                raise InvalidAgeError("Invalid age: " + str(age))

            if int(age) < 16:
                raise UnderageUserError("User is under 16: " + username)

            if not is_valid_email(email):
                raise InvalidEmailError("Invalid email: " + email)

            user = User(username, email, age)
            user_directory.append(user)
            print("User added to directory:", user.username)

        except UsernameNotUniqueError as e:
            print("Error:", str(e))

        except InvalidAgeError as e:
            print("Error:", str(e))

        except UnderageUserError as e:
            print("Error:", str(e))

        except InvalidEmailError as e:
            print("Error:", str(e))

def is_unique_username(user_directory, username):
    for user in user_directory:
        if user.username == username:
            return False
    return True

def is_positive_integer(age):
    try:
        age = int(age)
        if age > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def is_valid_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

user_data = [
    ("Atanu Nayak", "nayak.primary@gmail.com", "20"),
    ("Soumyajit Naskar", "soumyajit@algolisted.com", "15"),
    ("Atanu Nayak", "nayak.primary@gmail.com", "-10"),
    ("Tuhin Saha", "saha@algolisted.com", "25"),
    ("Soumyajit Naskar", "soumyajit@algolisted.com", "30"),
    ("Shruti Ghosh", "gf@nayak.com", "14"),
    ("Tuhin Saha", "saha@algolisted.com", "18"),
    ("Shreya Sahoo", "gf@nayak.com", "25"),
]

add_user_to_directory(user_data)
