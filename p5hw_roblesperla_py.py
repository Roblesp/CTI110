# Perla Robles

# 04/19/2025

# P5HW_Adventure_Game

# Creating a Game using Python

import time, random

def createPlayer():
    player_name = input("What is your name? ")
    health_points = 100
    dif_abil = ["invisibility", "turning into a ball", "barehands"]

    time.sleep(1)
    print("Creating your character...")
    time.sleep(2)
    print(f"Your starting abilities are: {dif_abil}")
    time.sleep(1)

    return {"name": player_name, "health": health_points, "abilities": dif_abil}

def intro(player):
    print(f"Welcome, {player['name']}. You have just entered the Dragon's Castle.")
    time.sleep(2)
    print("Do you want to Explore or LEAVE?")

    while True:
        choice = input("Type 'Explore' or 'Leave': ").lower()
        if choice == "explore":
            print("You bravely decided to explore deeper into the castle...")
            time.sleep(2)
            break
        elif choice == "leave":
            print("You chose to leave the castle safely. Game over.")
            exit()
        else:
            print("Invalid choice. Please type 'Explore' or 'Leave'.")

def enter_room(player):
    room = random.choice(["Sword Room", "Trap Room", "Treasure Room"])
    print(f"{player['name']} enters the {room}...")
    time.sleep(3)

    if room == "Sword Room":
        print("You find a glowing sword! It adds to your abilities.")
        time.sleep(2)
        player["abilities"].append("glowing sword")
    elif room == "Trap Room":
        print("A spiked floor trap activates! You lose 20 health.")
        player["health"] -= 20
    elif room == "Treasure Room":
        print("You found a diamond necklace! It's pretty, but cursed! You lose 15 health.")
        player["health"] -= 15

    print(f"💖 Health: {player['health']}")
    print(f"✨ Abilities: {player['abilities']}")

def dragon_battle(player):
    if player["health"] <= 0:
        print("You have no health left... The dragon claims another victim. 💀")
        return "died"

    choice = input("You encounter a dragon. Would you like to fight the dragon? (yes/no): ").lower()
    if choice == "no":
        print("You decided to leave without any harm. Sometimes, retreat is wise.")
        return "retreated"

    print("Time to fight the dragon! To get the door behind him!")
    time.sleep(2)

    print("Your abilities:")
    for ability in player["abilities"]:
        print(f"- {ability}")

    chosen = input("What do you want to use to fight the dragon? ").strip().lower()

    if chosen not in [a.lower() for a in player["abilities"]]:
        print("You try using an ability you don't have... The dragon isn't impressed.")
        print("🔥 The dragon breathes fire and defeats you.")
        print("💀 Game Over.")
        return "died"

    print(f"You chose to use: {chosen}")
    time.sleep(2)

    if chosen == "glowing sword":
        print("You use your Glowing Sword and strike the dragon down with a critical hit! 🗡️")
        print("🎉 You defeat the dragon and find the hidden door behind him. You grab the treasure and escape the castle!")
        return "won"
    elif chosen == "invisibility":
      print("You turn invisible and sneak behind the dragon unnoticed...")
      time.sleep(2)
      print("You grab the treasure quietly, but the strain of holding your breath and sneaking drains all your strength.")
      player["health"] = 0
      print("You collapse outside the castle, treasure in hand. The last thing you see is the sunrise... 🌅")
      return "won_stealth"

    elif chosen == "turning into a ball":
        print("You tuck and roll, transforming into a compact blur of motion! 🌀")
        time.sleep(2)
        print("You ricochet off the walls, dodging fire blasts by inches...")
        time.sleep(2)
        print("The dragon tries to track your movement, but you're too fast!")
        time.sleep(2)
        print("You land behind the dragon, panting — with the treasure in sight.")
        player["health"] -= 40
        if player["health"] > 0:
            print("You barely made it, losing 40 health in the chaos.")
            return "won_ball"
        else:
            print("The effort was too much. You collapse from the impact as the treasure slips from your fingers...")
            return "died"
    elif chosen == "barehands":
        print("You charge at the dragon with nothing but your fists...")
        print("💥 'Steel is for the weak — I am the weapon!'")
        time.sleep(2)
        print("...The dragon raises an eyebrow, then breathes fire 🔥")
        time.sleep(2)
        print("You're instantly turned to ashes.")
        print("💀 Game Over.")
        return "died"
    else:
        print("The dragon laughs at your attempt. You are roasted.")
        print("💀 Game Over.")
        return "died"

    if player["health"] <= 0:
        print("You have no health left... The dragon claims another victim. 💀")
        return "died"

# Entry point
def main():
    player = createPlayer()
    intro(player)
    enter_room(player)
    result = dragon_battle(player)

    if result == "won":
        print(f"🏆 {player['name']}, you have conquered the dragon in combat and claimed the treasure!")
        print("You walk out of the Dragon's Castle victorious. 🎉")
    elif result == "won_stealth":
        print(f"🕶️ {player['name']}, you escaped with the treasure, but at a great cost...")
    elif result == "won_ball":
        print(f"🏀 {player['name']} pulled off an insane ricochet roll and got the treasure!")
        print("You may be bruised and battered, but you made it. 🎉")
        if player["health"] <= 0:
            print("You died from exhaustion shortly after escaping, but the treasure was yours. 💀💎")
        else:
            print("You survived and escaped undetected. Brilliant work! 🎉")

    print(f"🏁 Final Health: {player['health']}")

if __name__ == "__main__":
  main()

