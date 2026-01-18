
import subprocess
import sqlite3

def unsafe_command(user_input):
    subprocess.call(user_input, shell=True)

def insecure_db():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = '%s'" % input("Name: "))
