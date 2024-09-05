def show_instructions():
    print("Welcome to the Adventure Game!")
    print("Commands: look, go [direction], get [item], inventory, quit")

def show_status():
    print("---------------------------")
    print("You are in the " + current_room)
    print("Inventory: " + str(inventory))
    if "item" in rooms[current_room]:
        print("You see a " + rooms[current_room]['item'])
    print("---------------------------")

def check_win():
    if len(inventory) == len(items_needed_to_win):
        print("Congratulations! You have collected all the items and won the game!")
        return True
    return False

def check_lose():
    if current_room == 'Kitchen' and 'sword' not in inventory:
        print("Oh no! You encountered the monster without a sword. You lose!")
        return True
    return False

inventory = []
items_needed_to_win = ['map', 'key', 'sword']
rooms = {
    'Forest': {'north': 'Hall', 'item': 'map'},
    'Hall': {'south': 'Forest', 'east': 'Dining Room', 'west': 'Library', 'item': 'key'},
    'Kitchen': {'north': 'Hall', 'item': 'monster'},
    'Dining Room': {'west': 'Hall', 'south': 'Garden'},
    'Garden': {'north': 'Dining Room', 'item': 'sword'},
    'Library': {'east': 'Hall', 'item': 'book'}
}

current_room = 'Forest'

show_instructions()

while True:
    show_status()
    move = input(">").lower().split()
    
    if move[0] == 'look':
        print("You see trees all around you." if current_room == 'Forest' else "You see a " + rooms[current_room].get('item', 'nothing special') + " here.")
    
    elif move[0] == 'go':
        if move[1] in rooms[current_room]:
            current_room = rooms[current_room][move[1]]
        else:
            print("You can't go that way!")
    
    elif move[0] == 'get':
        if 'item' in rooms[current_room] and move[1] == rooms[current_room]['item']:
            inventory.append(move[1])
            print(move[1] + " got!")
            del rooms[current_room]['item']
        else:
            print("Can't get " + move[1] + "!")
    
    elif move[0] == 'inventory':
        if inventory:
            print("Your inventory contains:", ", ".join(inventory))
        else:
            print("Your inventory is empty.")
    
    elif move[0] == 'quit':
        print("Thanks for playing!")
        break
    
    else:
        print("Invalid command. Please try again.")
    
    if check_win() or check_lose():
        break
