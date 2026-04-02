from cryptography.fernet import Fernet
import os

if not os.path.exists("secret.key"):
    with open("secret.key", "wb") as f:
        f.write(Fernet.generate_key())

with open("secret.key", "rb") as f:
    cipher_suite = Fernet(f.read())

class User:
    def __init__(self, username: str, password: str, role: str):
        self.username = username
        self.password = password
        self.role = role  

    def check_password(self, password: str) -> bool:
        return self.password == password

USERS = {
    "kasir": User("kasir", "123", "Kasir"),
    "admin": User("admin", "123", "Administrator"),
    "owner": User("owner", "123", "Owner")
}

def login():
    print("\n🔐 === LOGIN SISTEM TOKO SWALAYAN ===")
    username = input("Username: ").strip().lower()
    password = input("Password: ").strip()

    if username in USERS and USERS[username].check_password(password):
        user = USERS[username]
        print(f"✅ Login berhasil! Selamat datang, {user.role.upper()} {user.username.upper()}")
        return user
    else:
        print("❌ Username atau password salah!")
        return None