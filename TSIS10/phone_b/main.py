from phone_book import *

# 1. Создание таблицы
create_table()

# 2. Вставка из CSV
insert_from_csv("contacts.csv")

# 3. Ввод вручную
insert_from_console()

# 4. Обновление данных
update_data("John", new_phone="000111222")

# 5. Поиск
search_data(name="Alice")

# 6. Удаление
delete_data("Bob")
