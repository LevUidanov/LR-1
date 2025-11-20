import sys
import math

def получить(индекс,текст):
    if len(sys.argv)>индекс:
        з=sys.argv[индекс]
    else:
        з=None

    while True:
        if з is None:
            print(текст,end="")
            з=input()

        проверка=з.replace('.','').replace('-','')
        if проверка.isdigit():
            return float(з)
        else:
            print("Ошибка: введите число.")
            print(текст,end="")
            з=input()

def корни(a,b,c):
    r=[]
    D=b*b-4*a*c
    if D<0: return r
    if D==0:
        t=-b/(2*a)
        if t>0:
            r+=[math.sqrt(t),-math.sqrt(t)]
        elif t==0:
            r.append(0.0)
        return r
    d=math.sqrt(D)
    t1=(-b+d)/(2*a)
    t2=(-b-d)/(2*a)
    for t in(t1,t2):
        if t>0:
            r+=[math.sqrt(t),-math.sqrt(t)]
        elif t==0:
            r.append(0.0)
    return r

def main():
    a=получить(1,"A: ")
    b=получить(2,"B: ")
    c=получить(3,"C: ")
    k=корни(a,b,c)
    if len(k)==0:
        print("Нет корней")
    elif len(k)==1:
        print("Один корень:",k[0])
    else:
        print("Корни:")
        for x in k: print(x)

if __name__=="__main__":
    main()
