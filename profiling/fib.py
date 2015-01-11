def fib(n):
    a, b = 1, 1
    for i in range(n):
        a, b = a+b, a
    return a

def main():
    fib(10)

if __name__=="__main__":
    main()
    
