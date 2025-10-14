# 과제 11
a = list(map(int, input('숫자 5개 입력: ').split()))
b =[int(input())]
c = a+b

print(c)

#과제 12
a = list(map(int, input('숫자 5개 입력: ').split()))
del a[3:]

print(a)

#과제 13
a =list(map(int, input('숫자 5개 입력 :').split()))

for index, value in enumerate(a):
    print(index+101,value, end=' / ')


#과제 14
a = [10,20,30,40,30,20,10]

print(a.count(20),"개")

#과제 15

​
a = list(map(int, input('숫자 10개를 아무작위로 입력해보세여: ').split()))

print('가장큰수: ',max(a),'/', '가장 작은 수: ', min(a))

#과제 16

a = list(map(int, input('숫자 10개를 아무작위로 입력해보세여: ').split()))

a.remove(max(a))
a.remove(min(a))
result = sum(a)
print(result)

#과제 17

a=[10,20,30,40,30,20,10]

for i in a:
    if i == 20:
        a.remove(20)

print(a)

#과제 18

a = list(i for i in range(6) if i > 0)
print(a)

#과제 19

a = list(i for i in range(1,20) if i %2 ==1)
print(a)

#과제 20

a,b = (map(int, input('두가지 숫자 입력: ').split()))

result = list(2 ** i for i in range(a,b+1))
del result[1:2]
del result[8:9]
print(result)


#과제 21

test = str(input('Hello, world!라고 입력하시오.'))

result = test.replace('Hello','Hi')

print(result)

#과제 22

test = list(map(str, input('임의의 4개 문자 입력: ').split()))
test = " / ".join(test)
print(test)

#과제 23

first_name = (str(input('성을 영어로 입력하시오: ')))
new = first_name.lower()

result = new.rjust(10)

print(result)

#과제 24

a = list(map(int, input('표준입력: ').split(';')))

a.sort(reverse=True)
for i in a:
    print("{:>9}".format(i))



