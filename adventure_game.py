def main():
    inventory = []

    while True:
        print("\nYou find yourself in a dark forest. What do you want to do?")
        print("1. Look around")
        print("2. Walk forward")
        print("3. Check inventory")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("You see trees all around you.")
        elif choice == "2":
            print("You walk forward and find a path.")
        elif choice == "3":
            if inventory:
                print("Your inventory contains:", ", ".join(inventory))
            else:
                print("Your inventory is empty.")
        elif choice == "4":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

""" Other direction I might go in, similar to bag in a way, more interactive and user-controlled:  
def show_instructions():
    print("Welcome to the Adventure Game!")
    print("Commands: go [direction], get [item]")

def show_status():
    print("---------------------------")
    print("You are in the " + current_room)
    print("Inventory: " + str(inventory))
    if "item" in rooms[current_room]:
        print("You see a " + rooms[current_room]['item'])
    print("---------------------------")

inventory = []
rooms = {
    'Hall': {'south': 'Kitchen', 'east': 'Dining Room', 'item': 'key'},
    'Kitchen': {'north': 'Hall', 'item': 'monster'},
    'Dining Room': {'west': 'Hall', 'south': 'Garden'},
    'Garden': {'north': 'Dining Room'}
}

current_room = 'Hall'

show_instructions()

while True:
    show_status()
    move = input(">").lower().split()
    if move[0] == 'go':
        if move[1] in rooms[current_room]:
            current_room = rooms[current_room][move[1]]
        else:
            print("You can't go that way!")
    if move[0] == 'get':
        if 'item' in rooms[current_room] and move[1] == rooms[current_room]['item']:
            inventory.append(move[1])
            print(move[1] + " got!")
            del rooms[current_room]['item']
        else:
            print("Can't get " + move[1] + "!")
