from argon2 import PasswordHasher


ph = PasswordHasher()


def hash_password(password):
    return ph.hash(password)


def verify_password(password_hash, password):
    try:
        return ph.verify(password_hash, password)
    except:
        return False
