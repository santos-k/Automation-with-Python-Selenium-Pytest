def validate_login(username, password):

    if type(username) == str and type(password) == str:
        if username == "admin" and password == "admin123":
            print("Login Success")

        else:
            raise ValueError("Login denied, username or password maybe wrong.")

    else:
        raise ValueError("Username and password should be string.")

