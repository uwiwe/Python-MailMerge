#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("Input/Names/invited_names.txt") as invited_names:
    names = invited_names.read().splitlines()

with open("Input/Letters/starting_letter.txt", "r") as starting_letter:
    content = starting_letter.read()
for name in names:
    personalized_name = content.replace("[name]", name)

    with open(f"Output/ReadyToSend/letter_{name}.txt", "w") as create_letter:
        create_letter.write(personalized_name)