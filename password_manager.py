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


def add_account(username, website, account_username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    encrypted_username = cipher_suite.encrypt(username.encode())
    c.execute("INSERT INTO accounts (username, website, account_username, password_hash) VALUES (?, ?, ?, ?)",
              (encrypted_username, website, account_username, password_hash))
    conn.commit()
    print(f"{website}에 대한 계정 정보가 추가되었습니다.")


def find_account(username, website):
    encrypted_username = cipher_suite.encrypt(username.encode())
    c.execute("SELECT * FROM accounts WHERE username=? AND website=?", (encrypted_username, website))
    result = c.fetchone()

    if result:
        account_username = result[2]
        password_hash = result[3]
        password = cipher_suite.decrypt(password_hash.encode()).decode()

        print(f"사이트 이름: {website}")
        print(f"사용자 이름: {account_username}")
        print(f"비밀번호: {password}")
    else:
        print(f"{website}에 대한 계정 정보를 찾을 수 없습니다.")


def delete_account(username, website):
    encrypted_username = cipher_suite.encrypt(username.encode())
    c.execute("DELETE FROM accounts WHERE username=? AND website=?", (encrypted_username, website))
    if c.rowcount == 0:
        print(f"{website}에 대한 계정 정보를 찾을 수 없습니다.")
    else:
        conn.commit()
        print(f"{website}에 대한 계정 정보가 삭제되었습니다.")

def list_accounts(username):
    encrypted_username = cipher_suite.encrypt(username.encode())
    c.execute("SELECT DISTINCT website FROM accounts WHERE username=?", (encrypted_username,))
    results = c.fetchall()

    if len(results) == 0:
        print("저장된 계정 정보가 없습니다.")
    else:
        print("저장된 계정 정보의 사이트 이름 목록입니다:")
        for result in results:
            print(result[0])

def logged_in_menu(username):
    while True:
        print("1. 추가")
        print("2. 찾기")
        print("3. 삭제")
        print("4. 리스트")
        print("5. 로그아웃")
        sys.stdout.flush()
        action = input("무엇을 하시겠습니까? (1/2/3/4/5): ")
        if action == "1":
            website = input("사이트 이름을 입력하세요: ")
            account_username = input("아이디를 입력하세요: ")
            password = getpass("비밀번호를 입력하세요: ")
            add_account(username, website, account_username, password)

        elif action == "2":
            website = input("어떤 사이트의 계정 정보를 찾으시겠습니까? ")
            find_account(username, website)

        elif action == "3":
            website = input("어떤 사이트의 계정 정보를 삭제하시겠습니까? ")
            delete_account(username, website)

        elif action == "4":
            list_accounts(username)

        elif action == "5":
            print("로그아웃합니다.")
            break

        else:
            print("올바른 입력이 아닙니다 다시 시도해주세요.")
            if name == "main":
                while True:
                    print("1. 사용자 등록")
            print("2. 로그인")
            print("3. 종료")
            sys.stdout.flush()
            action = input("무엇을 하시겠습니까? (1/2/3): ")

            if action == "1":
                username = input("사용자 이름을 입력하세요: ")
                password = getpass("비밀번호를 입력하세요: ")
                confirm_password = getpass("비밀번호를 다시 입력하세요: ")
                register_user(username, password, confirm_password)

            elif action == "2":
                username = input("사용자 이름을 입력하세요: ")
                password = getpass("비밀번호를 입력하세요: ")
                if login_user(username, password):
                    print("로그인에 성공하였습니다.")
                    logged_in_menu(username)
                else:
                    print("로그인에 실패하였습니다.")

            elif action == "3":
                print("프로그램을 종료합니다.")
                conn.close()
                print("프로그램이 정상적으로 종료되었습니다.")
                sys.exit()

            else:
                print("올바른 입력이 아닙니다. 다시 시도해주세요.")
