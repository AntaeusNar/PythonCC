prompt = "\nTell me something and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

messages = []
entree = ""
while entree.lower() != 'quit':
    entree = input(prompt)
    if entree.lower() != 'quit':
        print(entree)
        messages.append(entree.lower())
    else:
        print("No..... Don't leave me!!!")
        if len(messages) > 0:
            print("\nThis is everything you made me say")
            for message in messages:
              print(message)


print("Now we can play and new game!!!!!")
print("\nTell me one thing agian and I will let you go.")
while True:
    entree=input()

    if entree in messages:
        print("Good work and goodbye!")
        break
    else:
        print("Looks like we can play somemore!!!")