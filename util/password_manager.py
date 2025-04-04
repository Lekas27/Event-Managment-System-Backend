from passlib.context import CryptContext

class PasswordManager:
    def __init__(self, schemes=["argon2"], deprecated="auto"):
        self.pwd_context = CryptContext(schemes=schemes, deprecated=deprecated)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)
