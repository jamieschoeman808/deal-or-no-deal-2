import random
game_running = True

values = [
    1, 5, 20, 50, 100, 500, 1000, 5000, 10000, 20000, 50000, 100000, 250000, 500000, 1000000
    ]
boxes = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
]
#The dictionary will keep track of the box numbers and their respective numbers
box_values = {i: None for i in range(1, 16)}

#Generate random Number
def GenerateValue(values):
    rndVal = random.choice(values)
    values.remove(rndVal)
    return rndVal

def GetUserBox(boxes):
    print(boxes)
    userBox = int(input("Choose your box - Enter a number from 1-15: "))
    while userBox < 1 or userBox > 15:
        print("Invalid option. Please select another box")
        print(boxes)
        userBox = int(input("Choose your box - Enter a number from 1-15: "))
    boxes.remove(userBox)
    return userBox

def ChooseFive(boxes, box_values):
    print(boxes)
    boxes_chosen = 0
    while boxes_chosen != 5:
        chosenBox = int(input("Select a box to remove: "))
        print(box_values[chosenBox])
        del box_values[chosenBox]
        boxes.remove(chosenBox)
        boxes_chosen = boxes_chosen + 1
        print(boxes)

def GetOffer(box_values):
    total = sum(box_values.values())
    average = total / len(box_values)
    offer = average * 0.7
    return offer

def GetAnswer():
    answer = input("Deal(d) or no deal(nd): ")
    return answer

def ChooseThree(boxes, box_values):
    print(boxes)
    boxes_chosen = 0
    while boxes_chosen != 3:
        chosenBox = int(input("Select a box to remove: "))
        print(box_values[chosenBox])
        del box_values[chosenBox]
        boxes.remove(chosenBox)
        boxes_chosen = boxes_chosen + 1
        print(boxes)

#Populate the dictionary with keys and values
for i in box_values:
    box_values[i] = GenerateValue(values)

#print(box_values)
print("You have chosen box: " + str(GetUserBox(boxes)))
while game_running:
    #print(box_values)
    ChooseFive(boxes, box_values)
    print("Your offer is R"+ str(GetOffer(box_values)))
    answer = GetAnswer()
    if answer == 'd':
        print("Congratulations! You won R" + str(GetOffer(box_values)))
        break
    ChooseFive(boxes, box_values)
    print("Your offer is R"+ str(GetOffer(box_values)))
    answer = GetAnswer()
    if answer == 'd':
        print("Congratulations! You won R" + str(GetOffer(box_values)))
        break
    ChooseThree(boxes, box_values)
    print("Your offer is R"+ str(GetOffer(box_values)))
    answer = GetAnswer()
    if answer == 'd':
        print("Congratulations! You won R" + str(GetOffer(box_values)))
        break
    swap = input("Swap(s) or no swap(ns): ")
    if swap == 's':
        print("Congratulations! You won R" + str(box_values[boxes[0]]))
        break
    else:
        print("Congratulations! You won R" + str(box_values[14]))
        break