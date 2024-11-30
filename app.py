import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize the database
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            unique_key TEXT NOT NULL,
            valid_from DATE NOT NULL,
            expire_on DATE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    if 'email' in session:
        return redirect(url_for('virtual_assistant'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        unique_key = request.form['unique_key']

        # Check user details in the database
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email = ? AND unique_key = ?", (email, unique_key))
        user = c.fetchone()
        conn.close()

        if user:
            valid_from, expire_on = user[3], user[4]
            today = datetime.now().date()

            if today > datetime.strptime(expire_on, '%Y-%m-%d').date():
                flash('Your license has expired. Please contact support.', 'error')
                return redirect(url_for('login'))
            else:
                session['email'] = email
                return redirect(url_for('virtual_assistant'))
        else:
            flash('Invalid credentials. Please try again.', 'error')

    return render_template('login.html')

@app.route('/virtual_assistant')
def virtual_assistant():
    if 'email' in session:
        # Check expiration date
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT expire_on FROM users WHERE email = ?", (session['email'],))
        expire_on = c.fetchone()[0]
        conn.close()

        if datetime.now().date() > datetime.strptime(expire_on, '%Y-%m-%d').date():
            flash('Your license has expired. You are logged out.', 'error')
            session.pop('email', None)
            return redirect(url_for('login'))

        return render_template('index.html')  # Virtual assistant page
    return redirect(url_for('login'))

@app.route('/license', methods=['GET', 'POST'])
def license_page():
    if 'email' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        email = session['email']
        unique_id = request.form['unique_id']
        valid_from = request.form['valid_from']
        expire_on = request.form['expire_on']
        
        license_key = f"{unique_id}-{valid_from.replace('-', '')}-{expire_on.replace('-', '')}"
        
        # Store the license details in the database
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('''
            UPDATE users 
            SET valid_from = ?, expire_on = ?
            WHERE email = ? AND unique_key = ?
        ''', (valid_from, expire_on, email, unique_id))
        conn.commit()
        conn.close()
        
        return render_template('license.html', response={
            'license_key': license_key,
            'unique_id': unique_id,
            'valid_from': valid_from,
            'expire_on': expire_on
        })
    
    return render_template('license.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5002)
