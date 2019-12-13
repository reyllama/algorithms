import time
################# MY SOLUTION #############################################
def fibonacci(n):
    __cache = [0, 1]
    if n in [0,1]:
        return n
    elif n < len(__cache):
        return __cache[n-1] + __cache[n-2]
    else:
        for i in range(n-len(__cache)):
            __cache.append(__cache[-1]+__cache[-2])
        return __cache[-1]+__cache[-2]

###########################################################################

def fubonacci(n):
  fib = [0,1]
  for i in range(2,n+1):
    fib.append(fib[i-1] + fib[i-2])
  return fib[n]

###########################################################################
 def memoized(f):
    cache = {}
    def wrapped(k):
        v = cache.get(k)
        if v is None:
            v = cache[k] = f(k)
        return v
    return wrapped

@memoized
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
############################################################################

t0 = time.time()
print(fibonacci(2000))
t1 = time.time()
print(fubonacci(2000))
t2 = time.time()

print("My Algorithm takes {0:.2f}s while original one takes {1:.2f}s".format(t1-t0, t2-t1))
print('Time difference: {:.2f}'.format(t2-2*t1+t0))
