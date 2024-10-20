import threading
from time import sleep
from random import randint
from threading import Thread, Lock


class Bank():
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            a = randint(50, 500)
            self.balance += a
            print(f'Пополнение: {a}. Баланс: {self.balance}')
            sleep(0.001)


    def take(self):
        for _ in range(100):
            b = randint(50, 500)
            print(f'Запрос на {b}')
            if self.balance >= b:
                self.balance -= b
                print(f'Снятие: {b}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

