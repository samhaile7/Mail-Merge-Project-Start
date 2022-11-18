#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open(".//Input/Names/invited_names.txt") as file:
    list_of_names= file.readlines()
    stripped_names = []
    for name in list_of_names:
        new = name.strip()
        stripped_names.append(new)

    print(list_of_names)
    print(stripped_names)

with open(".//Input/Letters/starting_letter.txt") as file:
    list_of_lines = file.readlines()

    for name in stripped_names:
        new_first_line = list_of_lines[0].replace("[name]", name)
        list_of_lines[0] = new_first_line



        with open(f".//Output/ReadyToSend/letter_to_{name}.txt", mode= "w") as new_letter_file:
            print(list_of_lines)
            for i in list_of_lines:
                new_letter_file.write(i)


print(list_of_lines)