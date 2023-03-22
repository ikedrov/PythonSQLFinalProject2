'''
1. Создать базу данных mobile.db
2. Создать таблицу mobile_users с колонками UserID (INTEGER), User_name (Text), Balance (INTEGER),
Mobile_tariff_ref (INTEGER), Activity (Text)
3. Создать таблицу mobile_tariff с колонками TariffID (INTEGER), Tariff (Text), Price (INTEGER)
4. Заполнение таблицы mobile_users:
    User1, 10000, 2, Yes
    User2, 10000, 3, Yes
    User3, 10000, 1, Yes
5. Заполнение таблицы mobile_tariff:
    1, Standard, 500
    2, VIP, 1000
    3, Premium, 1500

6. Задача кода производить ежемесячное списание денежных средств с баланса пользователей, в размере тарифа,
пока Статус колонки Activity = Yes. Как только на балансе пользователя недостаточно денежных средств для списания,
то Статус колонки Activity становится = No, и операции по данному пользователю больше не проводятся
7. Количество месяцев определяется вводом числа в консоль, через input()
8. Предусмотреть проверку на достаточную величину баланса, оповещение о недостаточности денежных средств,
невозможности уйти в минус.
9. Код в консоли должен начинаться с фразы "Введите период расчета: "
'''


import sqlite3


class SqlMobile:

    @staticmethod
    def create_table_users():

        with sqlite3.connect('mobile.db') as db:
            cur = db.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS mobile_users(
            UserID INTEGER PRIMARY KEY AUTOINCREMENT,
            User_name TEXT NOT NULL,
            Balance INTEGER NOT NULL,
            Mobile_tariff_ref INTEGER NOT NULL,
            Activity TEXT NOT NULL);''')
            print('Создана таблица mobile_users')

    @staticmethod
    def create_table_tariffs():

        with sqlite3.connect('mobile.db') as db:
            cur = db.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS mobile_tariff(
            TariffID INTEGER PRIMARY KEY AUTOINCREMENT,
            Tariff TEXT NOT NULL,
            Price INTEGER NOT NULL);''')
            print('Создана таблица mobile_tariff')

    @staticmethod
    def add_users(data_users):

        with sqlite3.connect('mobile.db') as db:
            cur = db.cursor()
            cur.execute('''INSERT OR REPLACE INTO mobile_users (User_name, Balance, Mobile_tariff_ref, Activity) VALUES (?, ?, ?, ?)''', data_users)
            print('Добавлен новый пользователь')

    @staticmethod
    def add_tariff(data_tariff):

        with sqlite3.connect('mobile.db') as db:
            cur = db.cursor()
            cur.execute(
                '''INSERT OR REPLACE INTO mobile_tariff (Tariff, Price) VALUES (?, ?)''',
                data_tariff)
            print('Добавлен новый тариф')

    @staticmethod
    def change_balance(months):

        with sqlite3.connect('mobile.db') as db:
            cur = db.cursor()
            cur.execute(f'''SELECT Balance FROM mobile_users''')
            balance_info_result = cur.fetchall()
            mobile_balance_users = [balance_info_result[0][0], balance_info_result[1][0], balance_info_result[2][0]]

            cur.execute(f'''SELECT Price FROM mobile_tariff''')
            tariff_info_result = cur.fetchall()
            tariffs = [tariff_info_result[0][0], tariff_info_result[1][0], tariff_info_result[2][0]]
            count1 = True
            count2 = True
            count3 = True

            for i in range(int(months)):
                if count1:
                    if mobile_balance_users[0] >= tariffs[1]:
                        cur.execute(f'''UPDATE mobile_users SET Balance = Balance -  mobile_tariff.Price  FROM mobile_tariff  WHERE  mobile_users.Mobile_tariff_ref = mobile_tariff.TariffID AND UserID = 1''')
                        db.cursor()
                        mobile_balance_users[0] -= tariffs[1]
                        print(f'User1, Ваш баланс {mobile_balance_users[0]}')
                    else:
                        cur.execute(f'''UPDATE mobile_users SET Activity = "No" WHERE UserID = 1''')
                        print('Недостаточно средств не счете, User1')
                        count1 = False

                if count2:
                    if mobile_balance_users[1] >= tariffs[2]:
                        cur.execute(f'''UPDATE mobile_users SET Balance = Balance -  mobile_tariff.Price  FROM mobile_tariff  WHERE  mobile_users.Mobile_tariff_ref = mobile_tariff.TariffID AND UserID = 2''')
                        db.cursor()
                        mobile_balance_users[1] -= tariffs[2]
                        print(f'User2, Ваш баланс {mobile_balance_users[1]}')
                    else:
                        cur.execute(f'''UPDATE mobile_users SET Activity = "No" WHERE UserID = 2''')
                        print('Недостаточно средств не счете, User2')
                        count2 = False

                if count3:
                    if mobile_balance_users[2] >= tariffs[0]:
                        cur.execute(f'''UPDATE mobile_users SET Balance = Balance -  mobile_tariff.Price  FROM mobile_tariff  WHERE  mobile_users.Mobile_tariff_ref = mobile_tariff.TariffID AND UserID = 3''')
                        db.cursor()
                        mobile_balance_users[2] -= tariffs[0]
                        print(f'User3, Ваш баланс {mobile_balance_users[2]}')
                    else:
                        cur.execute(f'''UPDATE mobile_users SET Activity = "No" WHERE UserID = 3''')
                        print('Недостаточно средств не счете, User3')
                        count3 = False














