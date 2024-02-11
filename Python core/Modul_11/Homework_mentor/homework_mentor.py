from collections import UserDict
from datetime import date, datetime, timedelta


class Field:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
        
    @value.setter
    def value(self, new_value):
        self.validate(new_value)
        self._value = new_value

    def validate(self, value):
        pass
                
    def __str__(self):
        return str(self._value)
    
class Name(Field):
    pass

class Phone(Field):
    def validate(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError('Phone should be 10 symbols')
            
class Birthday(Field):
    def validate(self, value):
        if value is not None:
            try:
                datetime.strptime(value, '%Y-%m-%d')
            except ValueError:
                raise ValueError('Invalid birthday format. Please use YYYY-MM-DD.')
              
class Record:
    def __init__(self, name, birthday_date=None):
        self.name = Name(name)
        self.birthday_date = Birthday(birthday_date)
        self.phones = []
          
    def add_phone(self, phone_number: str):     
        phone = Phone(phone_number)
        if phone not in self.phones:
            self.phones.append(phone)
           
    def remove_phone(self, phone_number):              
        self.phones = [phone for phone in self.phones if phone.value != phone_number]
    
    
    def edit_phone(self, old_phone, new_phone):
        for i in range(len(self.phones)):
            if self.phones[i].value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
            raise ValueError('Phone not found')
   
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:  
                return Phone(phone_number)
            
    def add_birthday_date(self, birthday_date: str):     
        birthday_date = Birthday(birthday_date)
        if birthday_date is not None:
            self.birthday_date = birthday_date

    def days_to_birthday(self):     
        date_today = date.today()
        td_0 = timedelta(days=0)
        
        if self.birthday_date.value is not None:
            birthday_date = datetime.strptime(self.birthday_date.value, '%Y-%m-%d') 
            birthday_date = birthday_date.replace(year = date_today.year)
            difference = birthday_date.date() - date_today
            if difference > td_0:
                return f"{self.name}'s birthday is {difference} away"
            elif difference == td_0:
                return f"Today is {self.name}'s birthday"
            elif difference < td_0:
                birthday_date = birthday_date.replace(year = date_today.year + 1)
                difference = birthday_date.date() - date_today
                return f"{self.name}'s birthday is {difference} away"               
                                
        return 'The date of birth has not been established'
    
    def __str__(self):
        phones_str = '; '.join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name}, phones: {phones_str}, birthday: {self.birthday_date}" 
    

class AddressBook(UserDict):
    def __str__(self):
        pass

    def add(self):
        pass

    def iterator(self, item_number):
        counter = 0
        result = ''
        for item, record in self.data.items():
            result += f'{item}: {record}'
            counter += 1
            if counter >= item_number:
                yield result
                counter = 0
                result = ''
                 
    def add_record(self, record):
        self.data[record.name.value] = record
            
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Контакт {name} видалено")
        else:
            print(f"Контакт {name} не знайдено")
    
    def find(self, name):
        if name in self.data:
            return self.data[name]
    
 

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
john_record.add_birthday_date("2001-11-25")
book.add_record(john_record)

a_record = Record("a")
a_record.add_phone("1234567891")

b_record = Record("b")
b_record.add_phone("1134567891")

c_record = Record("c")
c_record.add_phone("1114567891")

print(book.iterator(2))


# john = book.find("John")
# print(john)
# print(john.days_to_birthday())

# Додавання запису John до адресної книги
# book.add_record(john_record)

# Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# jane = book.find("Jane")
# print(jane)

# # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

# Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567891", "1112223333")
# # john.edit_phone("1234567891", "1112223333")

# john = book.find("John")
# print(john)

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
# found_phone = jane.find_phone("9876543210")
# print(f"{jane.name}: {found_phone}")  # Виведення: 5555555555

# # Видалення запису Jane
# book.delete("Jane")