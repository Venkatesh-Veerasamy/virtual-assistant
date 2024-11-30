import sqlite3
from datetime import datetime, timedelta

# Connect to the database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Define the users to be inserted
users = [
    {
        'email': 'venkat@gmail.com',
        'unique_key': '1234',
        'valid_from': datetime.now().strftime('%Y-%m-%d'),
        'expire_on': (datetime.now() + timedelta(days=4)).strftime('%Y-%m-%d')
    },
    {
        'email': 'user2@example.com',
        'unique_key': '5678',
        'valid_from': datetime.now().strftime('%Y-%m-%d'),
        'expire_on': (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
    },
    {
        'email': 'expired_user@example.com',
        'unique_key': '9999',
        'valid_from': (datetime.now() - timedelta(days=10)).strftime('%Y-%m-%d'),
        'expire_on': (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d')  # Expired user
    },
    {
        'email': 'user3@gmail.com',
        'unique_key': '1122',
        'valid_from': datetime.now().strftime('%Y-%m-%d'),
        'expire_on': (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d')
    },
    {
        'email': 'str@gmail.com',
        'unique_key': '4849',
        'valid_from': datetime.now().strftime('%Y-%m-%d'),
        'expire_on': (datetime.now() + timedelta(days=6)).strftime('%Y-%m-%d')
    },
    {
        'email': 'user5@yahoo.com',
        'unique_key': '5566',
        'valid_from': datetime.now().strftime('%Y-%m-%d'),
        'expire_on': (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
    },
    {
        'email': 'user6@hotmail.com',
        'unique_key': '7788',
        'valid_from': datetime.now().strftime('%Y-%m-%d'),
        'expire_on': (datetime.now() + timedelta(days=9)).strftime('%Y-%m-%d')
    },
    {
        'email': 'user7@gmail.com',
        'unique_key': '9911',
        'valid_from': datetime.now().strftime('%Y-%m-%d'),
        'expire_on': (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d')
    },
    {
        'email': 'user8@example.com',
        'unique_key': '1010',
        'valid_from': datetime.now().strftime('%Y-%m-%d'),
        'expire_on': (datetime.now() + timedelta(days=8)).strftime('%Y-%m-%d')
    },
    {
        'email': 'user9@domain.com',
        'unique_key': '2020',
        'valid_from': datetime.now().strftime('%Y-%m-%d'),
        'expire_on': (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
    }
    ,
    {
        'email': 'simbu@gmail.com',
        'unique_key': '2024',
        'valid_from': datetime.now().strftime('%Y-%m-%d'),
        'expire_on': (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
    }
]

# Insert users into the database
for user in users:
    # Check if the email already exists
    c.execute("SELECT * FROM users WHERE email = ?", (user['email'],))
    existing_user = c.fetchone()

    if existing_user:
        print(f"User with email '{user['email']}' already exists. Skipping insertion.")
    else:
        c.execute('''
            INSERT INTO users (email, unique_key, valid_from, expire_on)
            VALUES (?, ?, ?, ?)
        ''', (user['email'], user['unique_key'], user['valid_from'], user['expire_on']))
        print(f"User '{user['email']}' inserted successfully.")

# Commit and close the connection
conn.commit()
conn.close()
