def display(function):
    def wrapper():
        print("\n")
        print(function())
        print("")
        print(10 * "-")

    return wrapper
