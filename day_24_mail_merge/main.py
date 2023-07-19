# TODO: Create a letter using starting_letter.txt
#  for each name in invited_names.txt
#  Replace the [name] placeholder with the actual name.
#  Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# read the starting letter
# read the invited names and turn it to a list
# replace the [name] part of the starting letter with a name
# save that replacement as a string
# save that string to the txt file


with open("./Input/Letters/starting_letter.txt", "r") as file:
    starting_letter = file.read()

with open("./Input/Names/invited_names.txt", "r") as file:
    names = file.readlines()

for name in names:
    name = name.strip("\n ")
    with open(f"./Output/ReadyToSend/{name}.txt", "w") as file:
        temp_letter = starting_letter.replace("[name]", name)
        file.write(temp_letter)

