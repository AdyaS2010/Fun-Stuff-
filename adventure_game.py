import random

def show_instructions():
    print("Welcome to The Adventure Game!")
    print("Commands: look, go [direction], get [item], inventory, quit, save, load")

def show_status():
    print("---------------------------")
    print("You are in the " + current_room)
    print("Inventory: " + str(inventory))
    print("Health: " + str(health))
    if "item" in rooms[current_room]:
        print("You see a " + rooms[current_room]['item'])
    print("---------------------------")

def check_win():
    if len(inventory) == len(items_needed_to_win):
        print("Congratulations! You have collected all the items and won the game!")
        return True
    return False

def check_lose():
    if health <= 0:
        print("Oh no! You have been defeated. You lose!")
        return True
    return False

def combat():
    global health
    if current_room == 'Kitchen' and 'sword' not in inventory:
        print("Oh no! You encountered the monster without a sword. You lose!")
        health = 0
    elif current_room == 'Kitchen' and 'sword' in inventory:
        print("You bravely fight the monster with your sword!")
        if random.choice([True, False]):
            print("You defeated the monster!")
            del rooms[current_room]['item']
        else:
            print("The monster injured you!")
            health -= 20
    elif current_room == 'Dungeon' and 'shield' not in inventory:
        print("Oh no! You encountered the dragon without a shield. You lose!")
        health = 0
    elif current_room == 'Dungeon' and 'shield' in inventory:
        print("You bravely fight the dragon with your shield!")
        if random.choice([True, False]):
            print("You defeated the dragon!")
            del rooms[current_room]['item']
        else:
            print("The dragon injured you!")
            health -= 50

def save_game():
    with open('savegame.txt', 'w') as f:
        f.write(current_room + '\n')
        f.write(','.join(inventory) + '\n')
        f.write(str(health) + '\n')
    print("Game saved!")

def load_game():
    global current_room, inventory, health
    with open('savegame.txt', 'r') as f:
        current_room = f.readline().strip()
        inventory = f.readline().strip().split(',')
        health = int(f.readline().strip())
    print("Game loaded!")

inventory = []
items_needed_to_win = ['map', 'key', 'sword', 'shield', 'potion']
rooms = {
    'Forest': {'north': 'Hall', 'item': 'map'},
    'Hall': {'south': 'Forest', 'east': 'Dining Room', 'west': 'Library', 'item': 'key'},
    'Kitchen': {'north': 'Hall', 'item': 'monster'},
    'Dining Room': {'west': 'Hall', 'south': 'Garden'},
    'Garden': {'north': 'Dining Room', 'item': 'sword'},
    'Library': {'east': 'Hall', 'item': 'book'},
    'Dungeon': {'down': 'Hall', 'item': 'dragon'},
    'Tower': {'up': 'Hall', 'item': 'shield'},
    'Potion Room': {'west': 'Garden', 'item': 'potion'}
}

current_room = 'Forest'
health = 100

show_instructions()

while True:
    show_status()
    move = input(">").lower().split()
    
    if move[0] == 'look':
        print("You see trees all around you." if current_room == 'Forest' else "You see a " + rooms[current_room].get('item', 'nothing special') + " here.")
    
    elif move[0] == 'go':
        if move[1] in rooms[current_room]:
            current_room = rooms[current_room][move[1]]
            if current_room in ['Kitchen', 'Dungeon']:
                combat()
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
    
    elif move[0] == 'save':
        save_game()
    
    elif move[0] == 'load':
        load_game()
    
    elif move[0] == 'quit':
        print("Thanks for playing!")
        break
    
    else:
        print("Invalid command. Please try again.")
    
    if check_win() or check_lose():
        break

