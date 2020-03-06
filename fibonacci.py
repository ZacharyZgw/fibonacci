def fibonacci_recursion(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
def fibonacci(num):
    a,b = 1,1
    for i in range(num-1):
        a,b = b,a+b
    return a

if __name__ == "__main__":
    for i in range(1,201):
        print("fibonacci({num}) = {result} ".format(num=i,result=fibonacci(i)))
        
