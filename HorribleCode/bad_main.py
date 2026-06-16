import random
import sys

""" List of Month Names """
months = ["January","February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

""" List of Tarot Cards"""
tarot_deck = [
    # Major Arcana (22)
    "The Fool",
    "The Magician",
    "The High Priestess",
    "The Empress",
    "The Emperor",
    "The Hierophant",
    "The Lovers",
    "The Chariot",
    "Strength",
    "The Hermit",
    "Wheel of Fortune",
    "Justice",
    "The Hanged Man",
    "Death",
    "Temperance",
    "The Devil",
    "The Tower",
    "The Star",
    "The Moon",
    "The Sun",
    "Judgement",
    "The World",

    # Minor Arcana - Wands (14)
    "Ace of Wands",
    "Two of Wands",
    "Three of Wands",
    "Four of Wands",
    "Five of Wands",
    "Six of Wands",
    "Seven of Wands",
    "Eight of Wands",
    "Nine of Wands",
    "Ten of Wands",
    "Page of Wands",
    "Knight of Wands",
    "Queen of Wands",
    "King of Wands",

    # Minor Arcana - Cups (14)
    "Ace of Cups",
    "Two of Cups",
    "Three of Cups",
    "Four of Cups",
    "Five of Cups",
    "Six of Cups",
    "Seven of Cups",
    "Eight of Cups",
    "Nine of Cups",
    "Ten of Cups",
    "Page of Cups",
    "Knight of Cups",
    "Queen of Cups",
    "King of Cups",

    # Minor Arcana - Swords (14)
    "Ace of Swords",
    "Two of Swords",
    "Three of Swords",
    "Four of Swords",
    "Five of Swords",
    "Six of Swords",
    "Seven of Swords",
    "Eight of Swords",
    "Nine of Swords",
    "Ten of Swords",
    "Page of Swords",
    "Knight of Swords",
    "Queen of Swords",
    "King of Swords",

    # Minor Arcana - Pentacles (14)
    "Ace of Pentacles",
    "Two of Pentacles",
    "Three of Pentacles",
    "Four of Pentacles",
    "Five of Pentacles",
    "Six of Pentacles",
    "Seven of Pentacles",
    "Eight of Pentacles",
    "Nine of Pentacles",
    "Ten of Pentacles",
    "Page of Pentacles",
    "Knight of Pentacles",
    "Queen of Pentacles",
    "King of Pentacles"
]

""" List of palm reading lines"""
lines = [
        "Life line is strong → long and healthy life ahead.",
        "Heart line is curved → emotional and passionate nature.",
        "Head line is straight → logical thinker.",
        "Fate line is faint → you shape your own destiny.",
        "Broken lines → unexpected changes ahead."
    ]

""" function to get fortune """
def main():

    """ Show the menu """
    show_menu()

""" function for user to choose fortune type """
def choose_fortune_type():

    try:
        choice = int(input("Choose what type of fortune you want to see:\n1. Astrology\n2. Tarot\n3. Palm Reading\n"))
        return choice
    except ValueError:
        print("Please enter a number not a word")

""" menu function """
def show_menu():
    while True:
        choice = choose_fortune_type()

        if choice == 1:
            month = show_astrology()
            print(f'You chose astrology and you were born in {months[month-1]}')

        elif choice == 2:
            card = show_tarot()
            print(f'The tarot card that was pulled is : {card}!\n')

        elif choice == 3:
            print(show_palm_reading())

        elif choice == 4:
            sys.exit()

        else:
            print("\nError when selecting from the menu\nClosing program")
            sys.exit()


""" function for showing astrology """
def show_astrology():
    try:
        month = int(input("Enter the number of the month you were born in: "))
    except ValueError:
        print("Please enter a number not a word")
    return month

""" function for showing tarot """
def show_tarot():
    return random.choice(tarot_deck)

""" function for showing palm reading """
def show_palm_reading():
    print("\n✋ Palm Reading Session ✋")
    return random.choice(lines)


if __name__ == '__main__':
    main()