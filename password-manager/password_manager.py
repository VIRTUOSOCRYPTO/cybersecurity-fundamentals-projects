import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

users = {}

def register(username, password):
    users[username] = hash_password(password)

def login(username, password):
    if users.get(username) == hash_password(password):
        print("Login successful")
    else:
        print("Invalid credentials")

register("admin", "secure123")
login("admin", "secure123")

