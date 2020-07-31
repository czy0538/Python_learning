# k=0
# while k<4:
#     try:
#         x=int(input())
#         y=int(input())
#         print(x/y)
#     except ValueError:
#         print("a")
#     except ZeroDivisionError:
#         print("b")
#     k+=1

k = 0
while k < 4:
    try:
        x = int(input())
        y = int(input())
        print(x / y)

    except (ValueError, ZeroDivisionError) as e:
        print(e)
    k += 1
