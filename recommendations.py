def main():
    difficulty = input("Difficult or Casual? : ").lower()
    players = input("Multiplayer or Single-player : ")

    if difficulty == "difficult":
        if players == "Multiplayer":
            recommend("Poker")
        else:
            recommend("Klondike")
    else:
        recommend("Computer Games")


def recommend(keyword: str):
    print("You might like " + keyword)


main()
