import random

class Solution:
    def game(self):

        game_list = ["Қайшы","Қағаз","тас"]

        c=0
        p=0
        print(f"Есеп : Компьютер - {c}, Ойыншы - {p}")

        while True:
            computer_choice = random.choice(game_list)
            person_choice = input("Қайшы, Қағаз, тас немесе Шығу: ")

            if person_choice == computer_choice:
                print("Тең түсті !")

            elif person_choice == "Қайшы":
                if computer_choice == "Қағаз":
                    p+=1
                    print("Диас жеңді !")
                else:
                    c+=1
                    print("Компьютер жеңді !")

            elif person_choice == "Қағаз":
                if computer_choice == "тас":
                    p+=1
                    print("Диас жеңді !")
                else:
                    c+=1
                    print("Компьютер жеңді !")

            elif person_choice == "тас":
                if computer_choice == "Қайшы":
                    p+=1
                    print("Диас жеңді !")
                else:
                    c+=1
                    print("Компьютер жеңді !")

            elif person_choice == "Шығу":
                break

            else:
                print("Қате команда")

            print(f"Диастың таңдауы: {person_choice}")
            print(f"Компьютер таңдауы: {computer_choice}")
            print(f"\nЕсеп : Компьютер - {c}, Диас - {p}\n")

p=Solution()
p.game()
