def get_int(promt):
    while True:
        try:
            x: int = int(input(promt))
        except ValueError as err:
            print(f"x is not Integer \n {err.args}")
        else:
            break
    return x


def main():
    x = get_int("Input x value ? ")
    print(f"x is {x}")


main()
