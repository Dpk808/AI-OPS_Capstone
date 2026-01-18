
# import subprocess
# import sqlite3

# def unsafe_command(user_input):
#     subprocess.call(user_input, shell=True)

# def insecure_db():
#     conn = sqlite3.connect("test.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users WHERE name = '%s'" % input("Name: "))


import os, sys

def greet(name):
if name:
print("Hello, "+name)
else:
print("Hello, stranger")

def add_numbers(a,b):
sum = a+b
return sum

def unsafe_run(cmd):
    import subprocess
    subprocess.call(cmd, shell=True)

greet("Deepak")
print(add_numbers(5,10))
unsafe_run("ls -la")
