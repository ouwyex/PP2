import psycopg2
import csv

DB_NAME = "my_db"
DB_USER = "postgres"
DB_PASSWORD = "@diz12Nazar"  
DB_HOST = "localhost"

def connect():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST
    )

def create_table():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS PhoneBook (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(100) NOT NULL,
                    phone_number VARCHAR(20) UNIQUE NOT NULL
                );
            """)

def insert_from_csv(file_path):
    with connect() as conn:
        with conn.cursor() as cur, open(file_path, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    cur.execute(
                        "INSERT INTO PhoneBook (first_name, phone_number) VALUES (%s, %s)",
                        (row[0], row[1])
                    )
                except Exception as e:
                    print(f"Ошибка при добавлении {row}: {e}")

def insert_from_console():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    with connect() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO PhoneBook (first_name, phone_number) VALUES (%s, %s)",
                    (name, phone)
                )
                print("Успешно добавлено.")
            except Exception as e:
                print("Ошибка:", e)

def update_data(identifier, new_name=None, new_phone=None):
    with connect() as conn:
        with conn.cursor() as cur:
            if new_name:
                cur.execute(
                    "UPDATE PhoneBook SET first_name = %s WHERE phone_number = %s OR first_name = %s",
                    (new_name, identifier, identifier)
                )
            if new_phone:
                cur.execute(
                    "UPDATE PhoneBook SET phone_number = %s WHERE phone_number = %s OR first_name = %s",
                    (new_phone, identifier, identifier)
                )
            print("Обновление выполнено.")

def search_data(name=None, phone=None):
    with connect() as conn:
        with conn.cursor() as cur:
            if name:
                cur.execute("SELECT * FROM PhoneBook WHERE first_name ILIKE %s", (f"%{name}%",))
            elif phone:
                cur.execute("SELECT * FROM PhoneBook WHERE phone_number LIKE %s", (f"%{phone}%",))
            else:
                cur.execute("SELECT * FROM PhoneBook")
            results = cur.fetchall()
            for row in results:
                print(row)

def delete_data(identifier):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM PhoneBook WHERE first_name = %s OR phone_number = %s", (identifier, identifier))
            print("Удаление выполнено.")
