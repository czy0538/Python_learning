# # 习题1
# person1 = {"小明": "呵呵哒"}
# person2 = {"小红": "哒哒呵"}
# print("person1")
# name = input("请输入姓名")
# person1[name] = input("请输入武功")
# age = int(input("请输入年龄"))
# person1["age"] = age;
# print("person2")
# name = input("请输入姓名")
# person2[name] = input("请输入武功")
# age = int(input("请输入年龄"))
# person2["age"] = age;
# i = int(input("请输入序号"))
# if i == 1:
#     print(person1)
# else:
#     print(person2)

# # 拓展版
# n = int(input("你想输入几个人："))
#
# person = {}
# per = [person]
# for i in range(0, n, 1):
#     name = input("请输入姓名")
#     person[name] = input("请输入武功")
#     person["age"] = int(input("请输入年龄"))
#     per.append(person)
# for t in per:
#     print(t)

# #异常
# class StrExcept(Exception):
#     pass
#
#
# class MathExcept(Exception):
#     pass
#
#
# while True:
#     try:
#         x = input("请输入你的名字：")
#         if len(x) < 2 or len(x)>20:
#             raise StrExcept
#         y = int(input("请输入你的年龄："))
#         if y < 18 or y > 60:
#             raise MathExcept
#         z = int(input("请输入你的月收入"))
#         if z < 800:
#             raise MathExcept
#         print("姓名", x)
#         print("年收入", z * 12)
#         break
#     except StrExcept:
#         print("输入名称异常")
#     except MathExcept:
#         print("输入数值异常")
#     except Exception as e:
#         print("输入e",e)
#
# def mySum(i, j):
#     s = 0;
#     for k in range(i, j + 1, 1):
#         s = s + k
#     return s

