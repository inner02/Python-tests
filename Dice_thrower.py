import dice

def simulate_dice_throw():

    result1 = dice.roll_dice()
    result2 = dice.roll_dice()
    
    print(f"Dice 1: {result1}")
    print(f"Dice 2: {result2}")
    print(f"Total: {result1 + result2}")

simulate_dice_throw()
