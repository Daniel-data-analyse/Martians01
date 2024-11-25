import random

box_locations = [1, 3, 5]
box_weights = [200, 300, 213]
total_weight = sum(box_weights)
found_weight = 0

print("Hello! Help us find the hidden cargo boxes.")
print("Hint: There are 3 boxes, and their total weight is 713 kg.\n")

def move_boxes(locations):
    new_locations = []
    for loc in locations:
        new_locations.append(loc + random.randint(-2, 2))
    return new_locations

while found_weight != total_weight:
    print(f"Current weight found: {found_weight} kg. Target weight: {total_weight} kg.\n")
    
    guesses = []
    for i in range(3):
        guess = int(input(f"Enter the kilometer mark for box {i + 1}: "))
        guesses.append(guess)
    
    found_weight = 0
    for guess in guesses:
        if guess in box_locations:
            index = box_locations.index(guess)
            found_weight += box_weights[index]
    
    if found_weight == total_weight:
        print("\nCongratulations! You found all the boxes!")
        print(f"The boxes were at: {box_locations}. Total weight: {total_weight} kg.")
    else:
        print("\nWrong locations. The boxes are moving!\n")
        box_locations = move_boxes(box_locations)

print("Thank you for helping!")
