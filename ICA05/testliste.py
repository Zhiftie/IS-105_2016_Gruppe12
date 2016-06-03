import timeit

def f():
    x = [i for i in range(1000)]
    
if __name__ == "__main__":
        timer = timeit.Timer(f)
        result = timer.repeat(repeat = 10, number = 1000)
        print("{:8.6f}".format(min(result)))