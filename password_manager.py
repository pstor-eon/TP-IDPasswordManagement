

import sqlite3
import hashlib
import sys
from getpass import getpass
from cryptography.fernet import Fernet

# 암호화 키 생성
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# 데이터베이스 연결
conn = sqlite3.connect('password_manager.db')
c = conn.cursor()

# 테이블 생성
c.execute('''CREATE TABLE IF NOT EXISTS user (username TEXT, password_hash TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS accounts (username TEXT, website TEXT, account_username TEXT, password_hash TEXT)''')

def register_user(username, password, confirm_password):
    username_hash = hashlib.sha256(username.encode()).hexdigest()
    c.execute("SELECT * FROM user WHERE username=?", (username_hash,))
    result = c.fetchone()

    if result:
        print("이미 등록된 사용자 이름입니다. 다른 아이디로 시도하거나 종료하세요.")
        return

    if password == confirm_password:
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        try:
            c.execute("INSERT INTO user (username, password_hash) VALUES (?, ?)", (username_hash, password_hash))
            conn.commit()
            print(f"사용자 {username} 등록이 완료되었습니다.")
        except sqlite3.Error as e:
            print(f"사용자 등록 중 오류가 발생했습니다: {e}")
    else:
        print("비밀번호가 일치하지 않습니다. 다시 시도해주세요.")

def login_user(username, password):
    username_hash = hashlib.sha256(username.encode()).hexdigest()
    c.execute("SELECT * FROM user WHERE username=?", (username_hash,))
    result = c.fetchone()

    if result:
        password_hash = result[1]
        input_password_hash = hashlib.sha256(password.encode()).hexdigest()

        if password_hash == input_password_hash:
            print("로그인에 성공하였습니다.")
            return True
        else:
            print("비밀번호가 올바르지 않습니다.")
            return False
    else:
        print("사용자 이름을 찾을 수 없습니다.")
        return False
