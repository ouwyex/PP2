import psycopg2
from config_1 import load_config

def search_like(column, text):
    query = f"""SELECT * FROM phone_book WHERE {column} LIKE '%{text}%';"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                row = cursor.fetchone()

                print(row)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == "__main__":
    search_like("phone_number", "776")