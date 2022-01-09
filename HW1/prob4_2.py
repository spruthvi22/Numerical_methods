import time
def fibonacci(n):
    if(n<2):
        return n
    return fibonacci(n-1)+fibonacci(n-2)

start=time.time()
print("f(40) = ",fibonacci(40))
end=time.time()
print("Elapsed time = ",end-start)
