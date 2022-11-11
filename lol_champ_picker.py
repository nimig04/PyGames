from random import choice

CHAMPS_BY_ROLE = {
    "top": [
        "Fiora",
        "Jax",
        "Renekton",
        "Quinn",
        "Sett",
        "Riven",
        "Kayle",
        "Rengar",
        "Volibear",
        "Topturne",
        "Vayne",
        "Akshan",
    ],
    "jg": ["Lee Sin", "Olaf", "Shyvana", "Sejuani", "Lillia", "Kindred", "Kha'zix", "Talon"],
    "mid": [],
    "sup": [],
    "bot": [],
}


def choose_champ(role: str):
    "Randomly select a League of Legends champion, given a role to play."

    global choosing

    if role not in CHAMPS_BY_ROLE:
        print("\nThat's not a role.\n")

    else:
        choosing = False
        champs = CHAMPS_BY_ROLE[role]
        champ = choice(champs)
        print(f"\nYou should play {champ} {role}!")


if __name__ == "__main__":
    choosing = True
    while choosing:
        role = input("Which role would you like to play? (top/jg/mid/sup/bot)\n>>>")
        choose_champ(role)
