import random
import sqlite3
import string
import time
import configs as cnf


def generate_token(id, need_save=True):
    part1 = str(hash(time.time()))
    part1 = part1.replace("1", "a").replace("2", "b").replace("3", "c").replace("4", "d").replace("5", "e")
    part1 = part1.replace("6", "f").replace("7", "g").replace("8", "h").replace("9", "i")
    part2 = "".join(random.choices(string.digits + string.ascii_lowercase, k=15))
    token = "s.ch." + part1 + "." + part2

    if need_save:
        write_token(id, token, int(time.time()))
    return token


def registry(email: str, password: str, username: str, phone: str = None, avatar: bytearray = None):
    connection = sqlite3.connect("general_database.db")
    cursor = connection.cursor()
    cursor.execute('''insert into Auth (Email, Password) VALUES (?, ?)''', (email, password))
    connection.commit()
    id = cursor.execute('''select * from Auth where Email = (?) and Password=(?)''', (email, password)).fetchone()
    id = id[0]
    # takes first column (id) from new row
    cursor.execute('''insert into General_info (UserId, Username, Email, Phone, Password, Avatar) 
    VALUES (?, ?, ?, ?, ?, ?)''', (id, username, email, phone, password, avatar))
    connection.commit()


if __name__ == "__main__":
    registry('testmail5', '0000', 'bleb')
    print(result)
