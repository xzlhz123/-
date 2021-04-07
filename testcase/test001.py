'''
L =[['APPLE','Google','Microsoft'],['java','pyhton','Ruby','PHP'],['Adam','Bart','Lisa']]
#'打印APPLE'
print(L[0][0])
#打印python
print(L[1][1])
#打印Lisa
print(L[2][2])
'''

"""birth = input('birth:')
birth = int(birth)
if birth <2000:
    print('000前')
elif 2000< birth < 2010 :
    print('10后')
else:
    print('20后')"""


# h = float(input('请输入您的身高(m):'))
# w = float(input('请输入您的体重(kg)：'))
# bmi = w / h**2
# print(f'您的身高是:{w}kg\n你的身高是:{h}m\n你的BMI指数是：{bmi}')
# #print(f"你的体重是:{w} kg\n你的身高是:{h:.2f} m\n你的BMI指数是:{bmi:.2f}")
#
# if bmi <18.5:
#     print('过轻')
# elif 18.5 < bmi < 25:
#     print('正常')
# elif 25 < bmi  < 28 :
#     print('过重')
# elif 28 < bmi <32 :
#     print('肥胖')
# else:
#     print('严重肥胖')

# L =['Bart','Lisa','Adam']
# for L1 in  L:
#     print(L1)
#
# sum1 = 0
# for x in range(101):
#     sum1 = sum1+x
#     print(sum1)

# #打印100以内偶数和
# sum = 0
# n = 99
# while n >0:
#     sum = sum +n
#     n = n-1
# print(sum)

#for循环练习
# L = ['Bart', 'Lisa', 'Adam']
# for L1 in L:
#     print(L1)
# l2 = input('请输入：')
# for l1 in l2:
#     print(l1)

#死循环练习
# n =99
# while n <100:
#     print(n)

#continue用法
# n = 0
# while n<10:
#     n = n+1
#     if n %2 ==0:
#      continue
#     print(n)

# #使用dict和set
# d = {'a':1,'b':2}
# print(d['a'])
#
# d.pop('a')
# print(d)

# d = (1,2,3)
# print(d)
# d1 = set([[2,3],1])
# print(d1)

#print(abs(-1))

# n1=255
# n2 = 1000
# print(hex(255))

# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(input('请输入：'))

# import math
#
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
# print(move(1,2,3,4))

# def power(x):
#     return (x*x);
#
# i = int(input('请输入：'))
# print(power(i))

#计算x的n次方
# def power(x,n):
#     s = 1
#     while n>0:
#         n = n-1
#         s = s*x
#         print(s)
#     return s
#
# #r1 = input(input('请输入：'))
# print(power(2,2))

# def add_end(l=[]):
#     l.append(input('请输入：'))
#     return l
# print(add_end([1,2]))
# def calc (*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum+n*n
#     return sum
# print(calc(1,2))

# def person (name,age,**kw):
#     print('name:',name,'age:',age,'other:',kw)
# ss=person('张三','12岁', city='杭州')

# #计算n的平方
# def power(x,n):
#     s = 1
#     while n > 0 :
#         n = n - 1
#         s = s * x
#     return s
# print(power(2,3))


def add(a = 1,b =2):
    global sum
    print(a,b)
    print(sum)
    sum = a+b
add(2,3)
