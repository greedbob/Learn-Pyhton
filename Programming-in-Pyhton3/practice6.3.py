class Transaction(object):

    def __init__(self, amount, date, currency='USD', usd_conversion_rate=1, description=None):
        self.__amount = amount
        self.__date = date
        self.__currency = currency
        self.__usd_conversion_rate = usd_conversion_rate
        self.__description = description
        self.__usd = amount * usd_conversion_rate