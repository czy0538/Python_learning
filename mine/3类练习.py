import datetime


class Data():
    def __init__(self, year, month, day):
        self.__year = year
        self.month = month
        self.day = day

    def display(self):
        print(self.__year, "-", self.month, "-", self.day)

    def change_year(self):
        self.__year = int(input("请输入你想要的年份"))


def main():
    t=Data(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day)
    t.display()
    t.change_year()
    t.display()

main()


