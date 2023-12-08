class counting:

    def __init__(self, numbers):
        self.numbers = numbers

    def count(self):
        for number in self.numbers:
            print(number)

count1 = counting([1, 2, 3, 4, 5])
for i in range(count1):
    print("\t" * i)


count2 = counting([6, 7, 8, 9, 0])

count1.count()
count2.count()