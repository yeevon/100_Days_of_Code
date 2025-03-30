import random
from selectors import SelectSelector

while True:
    roshambo_list = [
        """    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

    """, """    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)""",
        """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""]

    user_input = int(input("What do you choose? \nType 0 for Rock, "
                           "1 for Paper or 2 for Scissors. Enter -1 to quit.\n"))

    if user_input == -1:
        print("Good Game!")
        break

    comp_input = random.randint(0, 2)

    result = "Tie"

    if user_input < comp_input:
        if comp_input - user_input == 2:
            result = "You win"
        else:
            result = "You lose"
    elif user_input > comp_input:
        if user_input - comp_input == 2:
            result = "You lose"
        else:
            result = "You win"

    print("\n" + roshambo_list[user_input] + "\n\n" +
          "Computer chose:\n\n" +
          roshambo_list[comp_input] + "\n\n" +
          result + "\n")