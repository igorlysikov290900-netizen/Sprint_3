import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        self.name = name
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(self.name)
            self.__number_items += 1

    def delete_item_from_check(self, name):
        self.name = name
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(self.name)
            self.__number_items -= 1

    def check_amount(self):
        total = []
        for item_name in self.__name_items:
            price = self.__item_price[item_name]
            total.append(price)
        total = sum(total)
        if len(self.__name_items) > 10:
            total = total * 0.9
        return total

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for item_name in self.__name_items:
            tax = self.__tax_rate[item_name]
            if tax == 20:
                twenty_percent_tax.append(item_name)
        for name in twenty_percent_tax:
            price = self.__item_price[name]
            total.append(price)
        total = sum(total)
        if len(self.__name_items) > 10:
            total = (total * 0.9) * 0.2
        else:
            total = total * 0.2
        return total

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for item_name in self.__name_items:
            tax = self.__tax_rate[item_name]
            if tax == 10:
                ten_percent_tax.append(item_name)
        for name in ten_percent_tax:
            price = self.__item_price[name]
            total.append(price)
        total = sum(total)
        if len(self.__name_items) > 10:
            total = (total * 0.9) * 0.1
        else:
            total = total * 0.1
        return total
    
    def total_tax(self):
        total = self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
        return total

    def check_amount_with_taxes(self): ### Решил добавить от себя метод, который определяет сумму покупки с налогами
        total = self.total_tax() + self.check_amount()
        return total

    @staticmethod
    def get_telephone_number(telephone_number):
        try:
            number = int(telephone_number)
        except ValueError:
            raise ValueError('Необходимо ввести цифры')
        if len(str(number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        return f"+7{number}"

    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        date = [['часы', lambda x: x.hour], ['минуты', lambda x: x.minute], ['день', lambda x: x.day], ['месяц', lambda x: x.month], ['год', lambda x: x.year]]
        for time in date:
            string = f"{time[0]}: {time[1](now)}"
            date_and_time.append(string)
        return date_and_time

store = OnlineSalesRegisterCollector()
store.add_item_to_cheque('чипсы')
store.add_item_to_cheque('кола')
store.add_item_to_cheque('печенье')
store.add_item_to_cheque('молоко')
store.add_item_to_cheque('кефир')
store.add_item_to_cheque('чипсы')
store.add_item_to_cheque('чипсы')
store.add_item_to_cheque('чипсы')
store.add_item_to_cheque('чипсы')
store.add_item_to_cheque('чипсы')
store.add_item_to_cheque('чипсы')
store.add_item_to_cheque('чипсы')
store.add_item_to_cheque('чипсы')
store.delete_item_from_check('чипсы')
print(store.check_amount())
print(store.twenty_percent_tax_calculation())
print(store.ten_percent_tax_calculation())
print(store.total_tax())
print(store.check_amount_with_taxes())
print(store.get_telephone_number(1111111111))
print(store.get_date_and_time())