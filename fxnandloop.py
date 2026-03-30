word="artificial"
count=0

for ch in word:
    if(ch == 'a' or ch =='e' or ch == 'i' or ch == 'o' or ch=='u'):
        count +=1
        print("ans=",count)
for i in range(1,10,2):
 print(i)
i=int(input("enter youe no"))
sum=(i*(i+1))/2
print("sum:",sum)
sum=0
for i in range(1,5):
    sum += i
    print("sum:",sum)
def hello():
    print("hello")
    print("from python")
    hello()
def sum(a,b):
    s=a+b
    return s
ans = sum(3,4)
print(ans)
def avg(a,b,c):
    sum=a+b+c
    return sum/3
print(avg(1,2,3))
sum=lambda a,b,c: a+b+c 
print(sum(4,5,6))
def cal(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        return fact
    n=int(input("enter i:"))
    print(cal(n))




