import bcrypt

if __name__ == '__main__':
    password1 = b"mdpsimon"
    password2 = b"mdppaul"

    hashed_password1 = bcrypt.hashpw(password1, bcrypt.gensalt())
    hashed_password2 = bcrypt.hashpw(password2, bcrypt.gensalt())

    print(hashed_password1)
    print(hashed_password2)
