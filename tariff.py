from sql_query import SqlMobile


class Tariff:

    def tariff_logic(self):

        # SqlMobile.create_table_users()
        # SqlMobile.create_table_tariffs()
        # SqlMobile.add_users(('User1', 10000, 2, 'Yes'))
        # SqlMobile.add_users(('User2', 10000, 3, 'Yes'))
        # SqlMobile.add_users(('User3', 10000, 1, 'Yes'))
        # SqlMobile.add_tariff(('Standard', 500))
        # SqlMobile.add_tariff(('VIP', 1000))
        # SqlMobile.add_tariff(('Premium', 1500))
        months = input('Введите период расчета: ')
        SqlMobile.change_balance(months)








start = Tariff()
start.tariff_logic()