from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


ph = PasswordHasher()


def hash_password(password):
    return ph.hash(password)


def verify_password(password_hash, password):
    try:
        return ph.verify(password_hash, password)
    except VerifyMismatchError:
        return False
