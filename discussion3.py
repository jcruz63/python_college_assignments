# This function demonstrates chained conditionals
# This function could be replaced with a switch case which could improve readability
# This function will be incorporated in future iterations of this program but is here to demo chained conditionals
def move(direction):
    if direction == "up":
        print("up")
    elif direction == "down":
        print("down")
    elif direction == "left":
        print("left")
    elif direction == "right":
        print("right")
    else:
        raise RuntimeError("Not a valid input to direction must be up, right, left, down")


# Created to demo a nested conditional logic that should be refactored
# Will incorporate this into the actual program at another time
# Based of the popular DnD table top game characters are able to preform double actions meaning same action twice
def character_action(action, is_double):
    if action == "move":
        if is_double:
            print("character moved twice")
    if action == "attack":
        if is_double:
            print("character double attacked")


# Refactored to combine nested conditionals into a single conditional
def character_action_refactored(action, is_double):
    if action == "move" and is_double:
        print("character moved twice")
    if action == "attack" and is_double:
        print("character double attacked")


# Character class creation


class Character:
    def __init__(self, attack_value, defense_value, damage_type, reduction_type, reduction_amount, damage_amount,
                 health):
        self.attack = attack_value
        self.defense = defense_value
        self.damage_type = damage_type
        self.reduction_type = reduction_type
        self.reduction = reduction_amount
        self.damage = damage_amount
        self.health = health


# This next section demonstrates composition


def is_attack_successful(attack_value, defense_value):
    if attack_value > defense_value:
        return True
    else:
        return False


def check_reduction_types(damage_type, reduction_type):
    if damage_type == reduction_type:
        return True
    else:
        return False


# Improvement this function could potentially add health
def after_damage_reduction(damage_amount, reduction_amount):
    return damage_amount - reduction_amount


# This function demonstrates composition and nested conditionals
# Nested conditional is appropriate in this case due to the fact that we do not need to check reduction types
# if the attack isn't first successful
def combat(combatant1, combatant2):
    # Check if combatant1 attack value is greater than combatant2's defense
    # Improvement will be to add some random value to the attack value to simulate a dice roll
    if is_attack_successful(combatant1.attack, combatant2.defense):

        # If attack is successful we determine if the combatant2 will have damage reduction aka a resistance to
        # a particular type of damage. If these types match the damage amount is reduced
        # Improvement will be to convert types into enumerations because there will be a fixed set of damage types
        # a good example of enumerations are the months of a year
        if check_reduction_types(combatant1.reduction_type, combatant2.reduction_type):

            # Apply reduce damage amount
            combatant2.health = combatant2.health - after_damage_reduction(combatant1.damage, combatant2.reduction)

            # Output health status
            # Improvement there is duplicate logic here and the following else statement need to refactor out
            print("Combatant twos health is now " + str(combatant2.health))

        else:

            # Combatant2 takes full damage because the check to reduction types has returned false
            combatant2.health = combatant2.health - combatant1.damage

            # Duplicate logic as above will need to refactor out
            print("Combatant twos health is now " + str(combatant2.health))
    else:

        # Is only called if attack fails
        print("attack failed")


if __name__ == '__main__':
    # Creating two characters
    player = Character(10, 8, "slashing", "piercing", 5, 8, 100)
    enemy = Character(8, 8, "piercing", "piercing", 5, 5, 100)

    # Simulating several rounds of combat
    combat(player, enemy)
    combat(enemy, player)
    combat(player, enemy)
