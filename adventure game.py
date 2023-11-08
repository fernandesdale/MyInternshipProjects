import random

scenes = {
    "start": {
        "text": "You stand in the grand foyer of Blackwood Manor. The place looks eerie and dimly lit.",
        "choices": {
            "Investigate": "Investigate further",
            "leave": "Leave the mansion",
        }
    },
    "Investigate": {
        "text": "You find a dusty old book. It appears to be a journal. What do you do?",
        "choices": {
            "read_journal": "Read the journal",
            "leave": "Ignore it and and leave"
        }
    },
    "leave": {
        "text": "You left the mansion, never solving the mystery.",
        "choices": {}
    },
    "read_journal": {
        "text": "The journal reveals a family feud and hints at hidden treasures. You now have a clue.",
        "choices": {
            "continue": "Continue investigating."
        }
    },
    "continue": {
        "text": "You explore further and discover a secret passage. You enter it and find a hidden room.",
        "choices": {
            "search": "Search the room",
            "leave": "Leave the room",
        }
    },
    "search": {
        "text": "You find a hidden safe. Do you try to open it?",
        "choices": {
            "safe": "Try to open the safe"
        }
    },
    "safe": {
        "text": "You successfully open the safe and found the murder weapon",
        "choices": {
            "end_win": "Congratulations! You've solved the case!"
        }
    },
    "end_win": {
        "text": "Congratulations! You completed the adventure and won.",
        "choices": {}
    },
    "end_lose": {
        "text": "Game over.",
        "choices": {}
    }
}

def get_user_choice(scene):
    print(scene["text"])
    choices = scene["choices"]
    for i, (key, value) in enumerate(choices.items(), 1):
        print(f"{i}. {value}")
    choice = input("Enter the number of your choice: ")
    if choice.isdigit() and 1 <= int(choice) <= len(choices):
        return list(choices.keys())[int(choice) - 1]
    else:
        return "invalid"

def main():
    current_scene = "start"

    while current_scene:
        if current_scene in scenes:
            current_scene = scenes[current_scene]
            choice = get_user_choice(current_scene)

            if choice == "invalid":
                print("Invalid choice. Try again.")
            else:
                current_scene = choice

        elif current_scene == "end_lose":
            print("Game over. You lost the game.")
            break

if __name__ == "__main__":
    main()