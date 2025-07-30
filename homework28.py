import string
class BankUser:
    def __init__(self,name,surname,age,account_number,money,password):
        if type(name)!=str or type(surname)!=str:
            raise ValueError("Print your name and surname with letters")
        elif age<=0 :
            raise ValueError("Print your age correctly")
        elif len(account_number)!=16:
            raise ValueError("Print your account number correctly")
        elif money<=0 :
            raise ValueError("There is somthing wrong")
        elif len(password)<8:
            raise ValueError("Password must be at least 8 characters long")
        self._name=name
        self._surname=surname
        self._age=age
        self.__account_number=account_number
        self.__money=money
        self.__password=password
        self.__account_blocked=False
        self.__failed_attempts=0
    def info1(self):
        if self.__account_blocked:
            raise ValueError("Account is blocked")
        return f"Name:{self._name}, Surname:{self._surname}, Age:{self._age}"
    def info2(self,__password):
        if self.__account_blocked:
            raise ValueError("Account is blocked")
        if __password==self.__password:
            self.__failed_attempts=0
            return f"Account number {self.__account_number},money {self.__money}"
        else:
         self.__failed_attempts+=1
         if self.__failed_attempts>=3:
            self.__account_blocked=True
            raise ValueError("Account has just blocked")
         raise ValueError("Wrong password")

    def add(self,amount):
        if self.__account_blocked:
            raise ValueError("Account is blocked")
        if amount<=0:
            raise ValueError("Amount must be positive")
        self.__money+=amount
        return f"Balance {self.__money}"
    def draw(self,amount):
        if self.__account_blocked:
            raise ValueError("Account is blocked")
        if amount<=0:
            raise ValueError("Amount must be positive")
        self.__money-=amount
        return f"Balance {self.__money}"
    def restore(self,name,surname,last_4_digits):
        if name==self._name and surname==self.surname and str(last_4_digits)==__account_mumber[-4:]:
            self.__account_blocked=False
            self.__failed_attempts=0
            return True
        return False
user=BankUser("Jack","Brown",27,"1234567891234567",1000,"qwerty123")
print(user.info1())
print(user.add(1000))
print(user.draw(500))
print(user.info2("qwerty123"))

