#!/usr/bin/env python3

class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age  = age
        self.pay  = pay
        self.job  = job
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

if __name__ == '__main__':
    larry = Person('Larry Wall', 62, job='artist')
    bill = Person('William Gates', 61, pay=1000000, job='programmer')

    #print(larry.name.split()[-1])
    print(larry.lastName())

    #bill.pay *= 1.10 # let's give Bill a raise
    bill.giveRaise(.10)
    print(bill.pay)
