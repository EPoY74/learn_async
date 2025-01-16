import time
import os


def clock():
    time0 = round(time.time())
    while True:
        if (round(time.time()) - time0) % 5 == 0:
            # print("5 sec")
            yield  "5 sec"
        else:
            yield 0 

def query():
    for i in os.walk("c:\\"):
        # print(i[0])
        # Далаем генератор
        yield i[0]  


def main():
    data = query()
    alarm = clock()
    
    while True:
        d = next(data)
        a = next(alarm)
        print(d)
        if a: print(a)
        time.sleep(1)

main()