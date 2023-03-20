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
            mobile_balance_user1 = balance_info_result[0][0]
            mobile_balance_user2 = balance_info_result[1][0]
            mobile_balance_user3 = balance_info_result[2][0]
            print(mobile_balance_user1, mobile_balance_user2, mobile_balance_user3)

            cur.execute(f'''SELECT Price FROM mobile_tariff''')
            tariff_info_result = cur.fetchall()
            tariff_standard = tariff_info_result[0][0]
            tariff_vip = tariff_info_result[1][0]
            tariff_premium = tariff_info_result[2][0]
            print(tariff_standard, tariff_vip, tariff_premium)

            cur.execute(
                '''SELECT UserID, User_name, Balance, Mobile_tariff_ref, Activity FROM mobile_users LEFT JOIN mobile_tariff ON UserID = TariffID''')
            db.commit()
            # for i in range(int(months)):
            #     if mobile_balance_user1 >= tariff_vip:
            #         mobile_balance_user1 -= tariff_vip







