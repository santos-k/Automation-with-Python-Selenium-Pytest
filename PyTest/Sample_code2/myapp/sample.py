def validate_age(age):
    if type(age) == int:
        if age < 0:
            raise ValueError(f"Age cannot be less then zero. Received {age}")
        elif 0 <= age < 100:
            print("Hello!")
        else:
            raise ValueError("Please check age once")
    else:
        raise ValueError(f"Age should be a real number only. Received {type(age)}")




