ev_distance = {"ionic 5": 1000, "byd seal": 950, "tesla": 1200}


def check_distance(car: str):
    print(f"The car distance is : {ev_distance[car.lower()]}")


def main():
    car = input("Car name ?: ")
    try:
        check_distance(car)
    except KeyError:
        print(f"Car named: {car} is not in dictionary")


main()
