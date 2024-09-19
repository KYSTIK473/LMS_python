name = input("Как Вас зовут?\n")


print(f"Здравствуйте, {name}!")

mood = input("Как дела?\n")

if mood == "хорошо":
    print("Я за вас рада!")
elif mood == "плохо":
    print("Всё наладится!")