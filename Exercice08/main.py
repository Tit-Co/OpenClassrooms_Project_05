def log_decorator(func):
    def wrapper(*args, **kwargs):
        print('Hello before !')
        result = func(*args, **kwargs)
        print('Hello after !')
        return result
    return wrapper
 
@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")

def main():
    function_test()

if __name__ == '__main__':
    main()
