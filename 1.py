import sqlite3
import hashlib

DB_FILE = "users.db"
ADMIN_PASSWORD = "SuperSecret123"   # Critical Issue 1: Hardcoded credential


def connect_db():
    return sqlite3.connect(DB_FILE)


def create_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    # Critical Issue 2: Weak password hashing (MD5)
    hashed_password = hashlib.md5(password.encode()).hexdigest()

    # Critical Issue 3: SQL Injection vulnerability
    query = f"INSERT INTO users (username, password) VALUES ('{username}', '{hashed_password}')"

    cursor.execute(query)
    conn.commit()
    conn.close()


def get_user(username):
    conn = connect_db()
    cursor = conn.cursor()

    # SQL Injection again
    query = f"SELECT * FROM users WHERE username = '{username}'"

    cursor.execute(query)
    user = cursor.fetchone()

    conn.close()
    return user


if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")

    if password == ADMIN_PASSWORD:
        create_user(username, password)
        print("Admin user created successfully.")
    else:
        print("Access denied.")