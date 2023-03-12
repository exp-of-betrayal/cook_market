import random
import sqlite3
import string
import time
from functools import wraps
from configuration import database as db


def db_handle(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        connection = sqlite3.connect(db.filename)
        cursor = connection.cursor()
        try:
            f(*args, **kwargs, cursor=cursor)
        except sqlite3.Error as error:
            print(f"'\033[96m'|{f.__name__}| SQL error -> ", error, "\033[95m")
        except BaseException as error:
            print(f"'\033[96m'|{f.__name__}| Python error -> ", error, "\033[95m")
        connection.commit()
        cursor.close()
        connection.close()
    return wrapper


def generate_token(id, need_save=True):
    part1 = str(hash(time.time()))
    part1 = part1.replace("1", "a").replace("2", "b").replace("3", "c").replace("4", "d").replace("5", "e")
    part1 = part1.replace("6", "f").replace("7", "g").replace("8", "h").replace("9", "i")
    part2 = "".join(random.choices(string.digits + string.ascii_lowercase, k=15))
    token = "s.ch." + part1 + "." + part2

    if need_save:
        write_token(id, token, int(time.time()))
    return token


@db_handle
def registry(email: str, password: str, username: str, phone: str = None, avatar: bytearray = None, cursor=None):

    cursor.execute('''insert into Auth (Email, Password) VALUES (?, ?)''', (email, password))
    id = cursor.execute('''select * from Auth where Email = (?) and Password=(?)''', (email, password)).fetchone()
    id = id[0]
    cursor.execute('''insert into General_info (UserId, Username, Email, Phone, Password, Avatar) 
    VALUES (?, ?, ?, ?, ?, ?)''', (id, username, email, phone, password, avatar))
