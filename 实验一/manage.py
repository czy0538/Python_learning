import matplotlib.pyplot as plt


class Stu:
    __all_info = []

    def __init__(self):
        __all_info = []

    def menu(self):
        print('+--------------------------------+')
        print('|  1) 添加学生信息                 |')
        print('|  2) 查看所有学生信息              |')
        print('|  3) 修改学生的成绩                |')
        print('|  4) 删除学生信息                 |')
        print('|  5) 按成绩打印学生信息            |')
        print('|  6) 按年龄打印学生信息            |')
        print('|  7) 保存信息到文件(cj.txt)        |')
        print('|  8)从文件中读取数据cj.txt)        |')
        print('|  9) 成绩分析                      |')
        print('|  q) 退出                        |')
        print('+--------------------------------+')

    def start(self):
        while True:
            self.menu()
            num = input('请选择：')
            if num == '1':
                self.add_stu_info()
            elif num == '2':
                self.show_stu_info()
            elif num == '3':
                self.chang_stu_info()
            elif num == '4':
                self.del_stu_info()
            elif num == '5':
                self.score_Sort()
            elif num == '6':
                self.age_Sort()
            elif num == '7':
                self.save_file()
            elif num == '8':
                self.read_file()
            elif num == '9':
                self.analysis()
            elif num == 'q':
                break

    def add_stu_info(self):
        while True:
            name = input('请输入学生姓名,输入Stop：')
            if name == "Stop":
                break
            age = int(input('请输入学生年龄：'))
            score = int(input('请输入学生成绩：'))
            self.__all_info += [{'name': name, 'age': age, 'score': score}]

    def show_stu_info(self):
        for i in self.__all_info:
            print(i)
            print('|%s|%s|%s|' % (i['name'].center(20), str(i['age']).center(6), str(i['score']).center(6)))

    def chang_stu_info(self):
        flag = True
        name = input('请输入要修改信息的学生姓名：')
        for j in self.__all_info:
            if j['name'] == name:
                flag = False
                print('****系统找到该学生的信息****')
                age = int(input('请输入学生年龄：'))
                score = int(input('请输入学生成绩：'))
                j['age'] = age
                j['score'] = score
                print('修改后的学生信息是：',
                      '|%s|%s|%s|' % (j['name'].center(20), str(j['age']).center(6), str(j['score']).center(6)))

        if flag:
            print('系统没有', name, '的学生信息,无法修改，是否需要添加?')
            what = input("Y/N?")
            if what == "Y":
                self.add_stu_info()

    def del_stu_info(self):
        flag = 0
        count = 0
        name = input('请输入学生姓名：')
        for k in self.__all_info:
            if k['name'] == name:
                del self.__all_info[count]
                flag = 1
                print('学生', name, '的信息已经删除')
            count += 1
        if flag == 0:
            print('系统没有', name, '的学生信息!!!')

    def score_Sort(self):
        what = int(input('你想怎么排成绩?\n1高到底\n2低到高'))
        if what == 1:
            res = sorted(self.__all_info, key=lambda all_info: all_info['score'], reverse=True)
            print('按成绩从高至低打印学生信息:')
            for n in res:
                print('|%s|%s|%s|' % (n['name'].center(20), str(n['age']).center(6), str(n['score']).center(6)))
        elif what == 2:
            res = sorted(self.__all_info, key=lambda all_info: all_info['score'])
            print('按成绩从低至高打印学生信息:')
            for n in res:
                print('|%s|%s|%s|' % (n['name'].center(20), str(n['age']).center(6), str(n['score']).center(6)))
        else:
            print("请检查输入")

    def age_Sort(self):
        what = int(input('你想怎么按年龄排成绩?\n1高到底\n2低到高'))
        if what == 1:
            res = sorted(self.__all_info, key=lambda all_info: all_info['age'], reverse=True)
            print('按年龄从高至低打印学生信息:')
            for n in res:
                print('|%s|%s|%s|' % (n['name'].center(20), str(n['age']).center(6), str(n['score']).center(6)))
        elif what == 2:
            res = sorted(self.__all_info, key=lambda all_info: all_info['age'])
            print('按年龄从低至高打印学生信息:')
            for n in res:
                print('|%s|%s|%s|' % (n['name'].center(20), str(n['age']).center(6), str(n['score']).center(6)))
        else:
            print("请检查输入")

    def save_file(self):
        f = open('cj.txt', 'w')
        for i in self.__all_info:
            f.write('|%s|%s|%s|\n' % (i['name'].center(20), str(i['age']).center(6), str(i['score']).center(6)))
        f.close()

    def read_file(self):
        f = open('cj.txt', 'r')
        while True:
            s = f.readline()
            if s == '':
                break
            print(s)
        f.close()

    def analysis(self):
        name_list = ['A', 'B', 'C', 'D', 'E']
        num_list = [0, 0, 0, 0, 0]
        for t in self.__all_info:
            if t['score'] >= 90:
                num_list[0] += 1
            elif 80 <= t['score'] < 90:
                num_list[1] += 1
            elif 70 <= t['score'] < 80:
                num_list[2] += 1
            elif 60 <= t['score'] < 70:
                num_list[3] += 1
            elif t['score'] < 60:
                num_list[4] += 1

        plt.bar(range(len(num_list)), num_list, color='rgb', tick_label=name_list)
        plt.show()


def main():
    stu = Stu()
    stu.start()


main()
