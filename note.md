# Python程序设计语言

[TOC]



## 0基础

### 0.1python语句

- python一行一句，可以没有分号
- 多个语句写在一行时，需要有； 其他时候可以没有分号

### 0.2缩进

- python使用严格的缩进表明程序的框架
- Tab和空格不能混用
- 平级的语句行缩进必须相同
- 分支、循环、函数定义全部采用缩进格式，特点是末尾有：

### 0.3注释

单行注释 #

多行注释'''

### 0.4标识符、关键字

- 大小写敏感，长度不限
- help()
- 保留标识符 _代表上次运算的结果
- __ new __() 系统定义函数名

### 0.5输入输出

- <变量>=input(提示）都是字符串类型

- 需要什么类型的需要进行转化 

  如：a=int(input("请输入整数"))

- print(<输出项列表>，sep=<分隔符>,end=<结束符>)

- print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 **,**

  ```python
  (1). %字符：标记转换说明符的开始
  (2). 转换标志：-表示左对齐；+表示在转换值之前要加上正负号；“”（空白字符）表示正数之前保留空格；0表示转换值若位数不够则用0填充
  (3). 最小字段宽度：转换后的字符串至少应该具有该值指定的宽度。如果是*，则宽度会从值元组中读出。
  (4). 点(.)后跟精度值：如果转换的是实数，精度值就表示出现在小数点后的位数。如果转换的是字符串，那么该数字就表示最大字段宽度。如果是*，那么精度将从元组中读出
  ```

  

### 0.6 

- 函数：完成一定功能程序段

- 模块： 多个函数及变量

- 包：多个模块

- 库：多个包

- 模块和函数使用：

  - import 模块名

  - 模块名.函数名(参数)

  - from 模块名 import 函数名、变量名

  - import 模块名*  //全部引入
  
    ```py
    from math import sin,sqrt
    sqrt(2)
    sin(0.7)
    ```



## 1数据表示与基本运算

### 1.1常量、变量、对象

- 常量
  - python常量包括 数字，字符串，bool值，空值
  - 没有定义常量的保留字

- 对象
  - 一切都是对象
  - 获取对象的标识（id）和类型
    - id(11) //内存位置 
    - type(11)
  - 对象的类型是不可改变的

- 变量

  - 通过赋值运算符创建，指向一个对象

    ```python
    a=112
    type(a)
    <class 'int'>
    id(a)//引用
    140723675558000
    id(112)#对象
    140723675558000
    b=112//引用
    id(b)
    140723675554736
    ```

  - 不需要声明

  - 可以随时赋不同类型的值

  - 可以使用一个赋值号给多个变量赋值



- 对象和数据

  - 对象包含属性和方法

  - 数据是某类对象的属性值

    ```python
    a=5
    a.bit_length()##调用对象同cpp
    3
    a=254
    a.bit_length()
    8
    ```



- 数据类型

  - 整数型

    - 标准类型 ：-2^31~2^31-1
    - 长整型 内存长度

  - 浮点型（精确值）

    - 表示实数 <实数>E<整数>
    - IEEE764   8个字节

  - 复数类型

    - 实部和虚部都是浮点数，至少有一个虚部
    - 3+4j,1j

  - bool 型

    - True
    - False
    - 区分大小写

  - 高精度数，分数

    - Decimal类型:from decimal import Decimal

      ```python
      >>>from decimal import Decimal
      >>>a=Decimal(1)/Decimal(3)
      >>>a
      Decimal('0.3333333333333333333333333333')
      >>>type(a)
      <class 'decimal.Decimal'>
      ```

    - 分数：from fractions import Fraction

      ```python
      >>>from fractions import Fraction
      >>>Fraction(1,2)
      Fraction(1, 2)
      >>>Fraction(12,10)
      Fraction(6, 5)
      >>>Fraction(1.25)
      Fraction(5, 4)
      ```



- 序列类型

  若干有序的数据，分为不可变序列类型和可变序列类型

  可变序列：列表，字节数组等

  不可变序列：字符串、元组、字节序列

  - 字符串：unicode字符数列

  - 元组类型

    - 圆括号内，逗号隔开 如(1,2,3)
    - 元组内数据类型可以不同(1,2,"abc")

  - 字节序列：数据是一系列的字节，以'b'开头的字符串

    ```python
    >>>print(str)
    abcd字节序列
    >>>a=str.encode("utf-8")
    >>>a
    b'abcd\xe5\xad\x97\xe8\x8a\x82\xe5\xba\x8f\xe5\x88\x97'
    >>>a=str.encode("gb2312")
    >>>a
    b'abcd\xd7\xd6\xbd\xda\xd0\xf2\xc1\xd0'
    ```

  - 列表：方括号中用逗号隔开的若干数据，数据类型可以不同 [1,2],["f",[1,2]]
  
  - 字节数组：可修改的字节数列
  
  - 其它类型
  
    - 集合：无顺序，不重复，大括号中，逗号隔开，数据可变
  
    - 字典：key-value对，值可变
  
      ```python
      {key:value,key:value}
      #键值对之间为：
      >>> c={"name":"zxd","func":"打飞机"}
      >>> c
      {'name': 'zxd', 'func': '打飞机'}
      >>> c['name']="hehe"
      >>> c['age']=75
      >>> c
      {'name': 'hehe', 'func': '打飞机', 'age': 75}
      ```
  
- python一切皆有类型

### 1.2运算符

- lambda

  ```python
  >>> f=lambda x,y:x+y
  >>> f(1,2)
  3
  ```

- if ---else

  ```python
  >>> x=1;y=2;z=3
  ... m=x if y else z
  >>> m
  1
  >>> y=0
  >>> m=x if y else z
  >>> m
  3
  ```

- 逻辑运算符：or,and,not

- 成员运算符:in,not in,is,is not

  ```python
  >>> y={1,2,3}
  >>> x in y
  True
  >>> x not in y
  False
  >>> x is y
  False
  >>> x is not y
  True
  ```

- 算术运算符:+,-,*,/（正常除法）,//（整除）,**（乘方），%（取余）

  ```python
  >>> 1/2
  0.5
  >>> 1//2
  0
  ```

  ![1562066837198](C:\Users\czy05\AppData\Roaming\Typora\typora-user-images\1562066837198.png)



### 1.3内置函数（67个）

- divmod(a,b)

  返回a除以b的商和余数

- eval(expression)

  返回字符串表达式的值
  
  

## 2.控制结构与异常处理

### 2.1顺序结构

程序按照语句的书写次序自上而下顺序执行

### 2.2分支控制结构

应该在if elif之前进行声明变量，才是全局的

- 一路分支结构

if<expression>:

​	<do something>

else:

​	<do something>

- 二路分支结构

if<expression>:

​	<do something>

elif<expression>:

​	<do something>

....

else:

​	<do something>

### 2.3 for循环

- for <variable> in range (begin,end,step)

​	<循环体>/<语句块>

- for<variable> in <可迭代对象的结合>

  ​	<循环体>/<语句块>

  else:

  ​	<语句块>

### 2.4 while循环

while<循环条件>:

​	<循环体>/<语句块>

else:

​	<语句块>

### 2.5 特殊语句

- pass：什么也不做，占位的作用

- continue

- break

  ```python
  j = 0
  for i in range(1, 5, 1):
      if (i % 2):
          continue// j=2
          #pass//j=4
          j += 1
      else:
          j += 1
  print(j)
  ```


### 2.6异常处理

- 异常：程序中产生的错误

- 后果：如果一场对象未被处理或者捕获，程序就会用所谓的回溯（Traceback）终止执行

- 异常捕获一般格式：

  ```python
  try:
      <statements1>#正常的代码
  except<name1>:
      <statements2>
  except<name2,name3>:
      <statements3>
  except<name4> as e:
      <statements4>
  except:
      <statements5>
  finally:
      <statements7>
  ```

- ```python
  #给定的异常类型
  try:
      x = int(input("请输入一个整数"))
      y = int(input("请输入一个整数"))
      print("x/y", x / y)
  except ValueError:
      print("请输入整数")
  except ZeroDivisionError:
      print("除数不能为0")
  ```

- 自定义异常类

  ```python
  class SomeCustomeException(Exception):#继承自exception
      pass
  #自定义异常处理代码可以写在except语句里面
  
  raise<class> #创建并抛出异常类
  raise<instance>#抛出异常类的实例
  
  ```

- assert断言

  期望满足用户指定的条件。当用户定义的约束不满足时触发 AssertionError 异常

  ```python
  assert <test>,<data> #<data>可选
  #等效
  if not<test>:
  	raise AssertionError(<data>)
  ```



## 3函数

### 3.1 函数的定义

- def 函数名(<形式参数>):

  ​	<函数体>

- 没有参数类型，也没有返回值的类型

- 返回值 return<表达式>

- 参数传递方式：位置绑定，记不住可以采用名字绑定

- 可以指定缺省值

- 可变长参数

  - def 函数名(arg1元组变长参数,ag2,...,*tuple_args字典变长参数

- 允许多返回值

- lambda函数的定义

  - 用单行的表达式定义函数
  - 函数名 = lambda 参数：表达式
  - 可以使用默认参数

### 3.2 函数的调用

- 格式：函数名（实参）
- 函数出现的位置：
  - 作为单独的语句
  - 出现在表达实里
  - 作为实际参数出现在其他函数中

### 3.3.作用域

- 局部变量：只能在程序的特定部分使用

- 全局变量：可以在文件中任何地方使用

  - 使用global

    ```python
    >>> g=0
    >>> def add(a,b):
    ...     g=a#还是局部变量
    ...     return a+b
    ... 
    >>> print(add(1,2))
    3
    >>> g
    0
    
    >>> def add(a,b):
    ...     global g#先把g声明为全局
    ...     g=a#g被改变
    ...     return a+b
    ... 
    >>> add(1,2)
    3
    >>> g
    1
    ```

    

### 3.4 内嵌函数及其作用域

