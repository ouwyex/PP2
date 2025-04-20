import psycopg2
from config_1 import load_config

def insert(user_name, second_name, last_name, phone_number, config):
    sql = f"""INSERT INTO phone_book(name, second_name, last_name, phone_number) VALUES('{user_name}', '{second_name}', '{last_name}', '{phone_number}') RETURNING person_id"""

    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)

                rows = cursor.fetchone()
                if rows:
                    person_id = rows[0]
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return person_id
    
def query(name, second_name, last_name, config):
    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM phone_book WHERE name = '{name}' and second_name = '{second_name}' and last_name = '{last_name}'")
                row = cursor.fetchone()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        return row
    

def update(user_name, second_name, last_name, phone_number, config):
    sql = f""" 
        UPDATE phone_book
        SET phone_number = '{phone_number}'
        WHERE name = '{user_name}' and second_name = '{second_name}' and last_name = '{last_name}'
    """
    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    

def main():
    config = load_config()
    user_name = input("Введите имя: ")
    second_name = input("Введите отчество: ")
    last_name = input("Введите фамилию: ")
    phone_number = input("Введите номер телефона: ")
    if query(user_name, second_name, last_name, config) == None:
        insert(user_name, second_name, last_name, phone_number, config)
    else:
        print("Такой пользователь существует. Мы перезапишем ваши данные")
        update(user_name, second_name, last_name, phone_number, config)

if __name__ == "__main__":
    main()