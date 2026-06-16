import random


def get_user_name():
    """Ask the user for their name and return it."""
    name = input("Enter your name: ").strip()

    """ if blank: default name is Friend"""
    if name == "":
        name = "Friend"

    return name


def get_fortunes():
    """Return a list of possible fortunes."""
    return [
        "You will have a great opportunity soon.",
        "A new friendship will bring you happiness.",
        "Hard work will pay off faster than you expect.",
        "You should trust your instincts this week.",
        "A surprise is coming your way.",
        "Stay patient. Good things are building slowly."
    ]


def choose_fortune(fortunes):
    """Choose and return one random fortune from the list."""
    return random.choice(fortunes)


def display_fortune():
    """Display the final fortune message to the user."""

    """ getting the users name """
    name = get_user_name()

    """ getting list of fortunes """
    fortunes = get_fortunes()

    """ choosing random fortune """
    fortune = choose_fortune(fortunes)

    print()
    print("🔮 Fortune Teller 🔮")

    """ printing the fortune message """
    print(f"{name}, your fortune is:")
    print(fortune)


def main():
    """Run the fortune teller program."""
    display_fortune()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

