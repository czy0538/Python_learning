#异常
class StrExcept(Exception):
    pass


class MathExcept(Exception):
    pass


while True:
    try:
        x = input("请输入你的名字：")
        if len(x) < 2 or len(x)>20:
            raise StrExcept
        y = int(input("请输入你的年龄："))
        if y < 18 or y > 60:
            raise MathExcept
        z = int(input("请输入你的月收入"))
        if z < 800:
            raise MathExcept
        print("姓名", x)
        print("年收入", z * 12)
        break
    except StrExcept:
        print("输入名称异常")
    except MathExcept:
        print("输入数值异常")
    except Exception as e:
        print("输入e",e)
