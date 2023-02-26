travel = input().split("||")
fuel = int(input())
ammunition = int(input())

for elements in travel:
    elements_args = elements.split()
    if elements_args[0] == "Travel":
        if int(elements_args[1]) > fuel:
            print("Mission failed.")
            break
        else:
            fuel -= int(elements_args[1])
            print(f"The spaceship travelled {elements_args[1]} light-years.")
    elif elements_args[0] == "Enemy":
        if int(elements_args[1]) <= ammunition:
            ammunition -= int(elements_args[1])
            print(f"An enemy with {elements_args[1]} armour is defeated.")
        elif int(elements_args[1]) > ammunition:
            if int(elements_args[1]) * 2 > fuel:
                print("Mission failed.")
                break
            else:
                fuel -= int(elements_args[1]) * 2
                print(f"An enemy with {elements_args[1]} armour is outmaneuvered.")
    elif elements_args[0] == "Repair":
        fuel += int(elements_args[1])
        ammunition += int(elements_args[1]) * 2
        print(f"Ammunitions added: {int(elements_args[1]) * 2}.")
        print(f"Fuel added: {elements_args[1]}.")
    elif elements_args[0] == "Titan":
        print("You have reached Titan, all passengers are safe.")
