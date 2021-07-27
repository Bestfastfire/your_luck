import random


class Luck:
    def __init__(self):
        self.persons = []

    def put_person(self, name, n1, n2):
        num = [n1, n2]
        num.sort()

        person = [name] + num
        self.persons.append(person)
        return person

    def generate(self):
        luckNums = [random.randint(0, 9), random.randint(0, 9)]
        luckNums.sort()

        return luckNums, list(filter(lambda n: luckNums == [n[1], n[2]], self.persons))
