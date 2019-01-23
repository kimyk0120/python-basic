
def safe_sum(a, b):

    if type(a) != type(b):
        print("n/a")
        return False
    return print(a + b)


def sum(a,b):
    return print(a + b)


if __name__ == "__main__":
    safe_sum("a",1)
    safe_sum(1,4)
    sum(10,10.4)
