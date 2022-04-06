import sys


def fibonacci(n, print_stmt=True):

    n1, n2 = 0, 1
    count = 0
    fib_list = [0]
    while count < n:
        if print_stmt:
            print(f"{count}: {n1}")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        fib_list.append(n1)
        count += 1

    return fib_list


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("You need to provide an integer number!")
    elif len(sys.argv) > 2:
        print("You can only provide a single number to the script!")
    else:
        num_terms = sys.argv[1]
        try:
            num_terms = int(num_terms)
            print(fibonacci(num_terms))
        except:
            print(f"{num_terms} is not an integer number!")

