
#Yılmaz Yuka - 18401784 - Historically Accurate Virtual Enigma Machine


#five different rotors with 26 letters and with different wiring inside of it.
#from a to z is equal to from 1 to 26.
#array index represents the side facing the cables coming from the plugboard
#the numbers inside of indexes represents the number of the pin that this pin is connected on the other side of the rotor, which is faced to the reflector
#these are the original wirings used in ww2 by german army
rotors = [[5,11,13,6,12,7,4,17,22,26,14,20,15,23,25,8,24,21,19,16,1,9,2,18,3,10], #EKMFLGDQVZNTOWYHXUSPAIBRCJ 
          [1,10,4,11,19,9,18,21,24,2,12,8,23,20,13,3,17,7,26,14,16,25,6,22,15,5], #AJDKSIRUXBLHWTMCQGZNPYFVOE 
          [2,4,6,8,10,12,3,16,18,20,24,22,26,14,25,5,9,23,7,1,11,13,21,19,17,15], #BDFHJLCPRTXVZNYEIWGAKMUSQO 
          [5,19,15,22,16,26,10,1,25,17,21,9,18,8,24,12,14,6,20,7,11,4,3,13,23,2], #ESOVPZJAYQUIRHXLNFTGKDCMWB 
          [22,26,2,18,7,9,20,25,21,16,19,4,14,8,12,24,1,23,13,10,17,15,6,5,3,11]] #VZBRGITYUPSDNHLXAWMJQOFECK 

#the wiring of the reflector
reflector = [25,18,21,8,17,19,12,4,16,24,14,7,15,11,13,9,5,2,6,26,3,23,22,10,1,20] #YRUHQSLDPXNGOKMIEBFZCWVJAT 

#empty plugboard
plugboard = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#represents the 3 selected rotor from all rotors, with their priority
rotor_selection = [0,0,0]

#represents the start position of rotors, with their priority
rotor_index = [0,0,0]

#keeps the text prepared for encryption
text_ascii = []

#keeps the length of the text
text_length = 0

#function that gets the text to be encrypted or decrypted
def text_input():

    global text_ascii
    global text_length

    text = input("Write using only Latin alphabet without using any numbers or signs!\n")   #text input
    text = text.replace(" ","")                                                             #removing spaces between the letters
    text = text.lower()
    texttmp = list(text)                                                                    #converting text to array by separating each letter in the text
    control_index = 0
    text_length = len(text)
    for i in range(0,text_length):
        texttmp[i] = ord(texttmp[i])                                                        #converting the letters to their ascii values
        texttmp[i] = int(texttmp[i])
        if texttmp[i]<97 or texttmp[i]>122:
            control_index=1
    
    #if the letter is not in the specified range
    while (control_index==1):
        text = input("Please write the text, without numbers or signs, using ONLY latin alphabet!!\n")
        text = text.replace(" ","")
        text = text.lower() 
        texttmp = list(text)
        control_index = 0
        text_length = len(text)
        for i in range(0,text_length):
            texttmp[i] = ord(texttmp[i])
            texttmp[i] = int(texttmp[i])
            if texttmp[i]<97 or texttmp[i]>122:
                control_index=1
    
    for i in range(0,text_length):
        texttmp[i] = texttmp[i] - 96
    text_ascii = texttmp.copy()
    print("")

#function that we choosed 3 rotors with their queue
def rotor_alignment():

    global rotor_selection

    rotor_selection[0] = input("For the 1st Rotor selection, please choose one of the numbers 1,2,3,4,5\n")
    rotor_selection[0] = int(rotor_selection[0])
    rotor_selection[0] = rotor_selection[0] - 1
    while(rotor_selection[0]< 0 or rotor_selection[0]> 4):
        rotor_selection[0] = input("Please enter one of the values 1,2,3,4,5, do not enter any other value!\n")
        rotor_selection[0] = int(rotor_selection[0]) 
        rotor_selection[0] = rotor_selection[0] - 1

    rotor_selection[1] = input("For the 2nd Rotor selection, please choose one of the numbers 1,2,3,4,5. It should be different from your previous selections!\n")
    rotor_selection[1] = int(rotor_selection[1])
    rotor_selection[1] = rotor_selection[1] - 1
    while(rotor_selection[1] == rotor_selection[0] or rotor_selection[1]< 0 or rotor_selection[1]> 4):
        if rotor_selection[1] == rotor_selection[0]: 
            rotor_selection[1] = input("Please enter a different value from the previous values!\n")
            rotor_selection[1] = int(rotor_selection[1])
            rotor_selection[1] = rotor_selection[1] - 1
        if rotor_selection[1]< 1 or rotor_selection[1]> 5:
            rotor_selection[1] = input("Please enter one of the values 1,2,3,4,5, do not enter any other value!\n")
            rotor_selection[1] = int(rotor_selection[1])
            rotor_selection[1] = rotor_selection[1] - 1

    rotor_selection[2] = input("For the 3rd Rotor selection, please choose one of the numbers 1,2,3,4,5. It should be different from your previous selections!!\n")
    rotor_selection[2] = int(rotor_selection[2])
    rotor_selection[2] = rotor_selection[2] - 1
    while(rotor_selection[2] == rotor_selection[0] or rotor_selection[2] == rotor_selection[1] or rotor_selection[2]< 0 or rotor_selection[2]>4):
        if rotor_selection[2] == rotor_selection[0] or rotor_selection[2] == rotor_selection[1]:
            rotor_selection[2] = input("Please enter a different value from the previous values!\n")
            rotor_selection[2] = int(rotor_selection[2])
            rotor_selection[2] = rotor_selection[2] - 1
        if rotor_selection[2]< 1 or rotor_selection[2]> 5:
            rotor_selection[2] = input("Please enter one of the values 1,2,3,4,5, do not enter any other value!\n")
            rotor_selection[2] = int(rotor_selection[2])
            rotor_selection[2] = rotor_selection[2] - 1

    print("")

#function that we choosed the starting indexes of the rotors
def rotor_index_selection():

    global rotor_index

    for i in range(3):
        rotor_index[i] = input("For the 1st Rotor index selection, select a number between 1 and 26 (including 1 and 26)\n")
        rotor_index[i] = int(rotor_index[i])
        rotor_index[i] = rotor_index[i] - 1
        while(rotor_index[i]< 0 or rotor_index[i]> 25):
            rotor_index[i] = input("Please enter one of the values in the specified range, not different values!\n")
            rotor_index[i] = int(rotor_index[i]) 
            rotor_index[i] = rotor_index[i] - 1

    print("")

#function that we choosed the binary letters on plugboard. maximum 10 binary letters for historical accuracy
def plugboard_selection():

    global plugboard

    counterrr = 0
    print("Please enter the binary letters you want replaced on plugboard. Press enter after entering each letter.")
    print("You can enter a maximum of 10 binary letters. If you don't want to enter any letters or if you don't want to type any more, type 1 and press enter.")
    while(counterrr!=10):
        print("enter new binary letters or log out")
        counterrr = counterrr+1
        letter1 = input()
        letter1 =letter1.lower()
        letter1 = ord(letter1)
        letter1 = int(letter1)
        if letter1==49:
            break
        while(letter1 < 97 or letter1 > 122 or plugboard[letter1-97]!=0):
            if(letter1 < 97 or letter1 > 122):
                print("Please write the letter, not numbers or signs, using ONLY latin alphabet!")
            if(plugboard[letter1-97]!=0):
                print("Please enter a different letter from the previous selected letters!")
            letter1 = input()
            letter1 = letter1.lower()
            letter1 = ord(letter1)
            letter1 = int(letter1)
        plugboard[letter1 - 97] = counterrr         #marking the choosed binary letters on plugboard array with their unique identify number

        letter2 = input()
        letter2 = letter2.lower()
        letter2 = ord(letter2)
        letter2 = int(letter2)
        if letter2==49:
            plugboard[letter1 - 97] = 0
            break
        while(letter2 < 97 or letter2 > 122 or plugboard[letter2-97]!=0):
            if(letter2 < 97 or letter2 > 122):
                print("lutfen ingiliz alfabesindeki harflerden birini giriniz!")
            if(plugboard[letter2-97]!=0):
                print("Please enter a different letter from the previous selected letters!")
            letter2 = input()
            letter2 = letter2.lower()
            letter2 = ord(letter2)
            letter2 = int(letter2)
        plugboard[letter2 - 97] = counterrr
    print("")

#this is where the encryption happens
def enigma():

    global text_length
    global text_ascii
    global plugboard
    global rotor_index
    global rotor_selection
    
    text_final = text_ascii.copy()
    text_tmp = text_ascii.copy()

    #placing selected rotors in enigma with their queue
    selected_rotor1 = rotors[rotor_selection[0]].copy()
    selected_rotor2 = rotors[rotor_selection[1]].copy()
    selected_rotor3 = rotors[rotor_selection[2]].copy()

    #adjusting starting indexes of the rotors by shifting the array
    ratchet_rotor1 = rotor_index[0]
    ratchet_rotor2 = rotor_index[1]
    ratchet_rotor3 = rotor_index[2]

    for i in range(0,rotor_index[0]+1):
        shift = selected_rotor1.pop(0)
        selected_rotor1.append(shift)

    for i in range(0,rotor_index[1]+1):
        shift = selected_rotor2.pop(0)
        selected_rotor2.append(shift)

    for i in range(0,rotor_index[2]+1):
        shift = selected_rotor3.pop(0)
        selected_rotor3.append(shift)

    #encrypting letters one by one
    for i in range(0,text_length):

        #the part that spins the rotors every time a new letter is encrypted
        shift1 = selected_rotor1.pop(0)
        selected_rotor1.append(shift1)

        if(ratchet_rotor2%26==0):
            shift3 = selected_rotor3.pop(0)
            selected_rotor3.append(shift3)
            ratchet_rotor3 = ratchet_rotor3 + 1

        if(ratchet_rotor1%26==0):
            shift2 = selected_rotor2.pop(0)
            selected_rotor2.append(shift2)
            ratchet_rotor2 = ratchet_rotor2 + 1

        ratchet_rotor1 = ratchet_rotor1 + 1

        #the first arrival of the letter on the plugboard. 
        #if it has a binary letter, it will be replaced with it, otherwise it will continue on its way.
        if(plugboard[text_tmp[i]-1] != 0):
            for j in range(0,26):
                if(j == text_tmp[i]-1):
                    continue
                elif(plugboard[j]==plugboard[text_tmp[i]-1]):
                    text_tmp[i] = j+1
                    break

        #encryption from the first rotor to the reflector
        text_tmp[i] = selected_rotor1[text_tmp[i]-1]
        text_tmp[i] = selected_rotor2[text_tmp[i]-1]
        text_tmp[i] = selected_rotor3[text_tmp[i]-1]
        text_tmp[i] = reflector[text_tmp[i]-1]

        #encryption from reflector to first rotor
        for k in range(0,26):
            if(selected_rotor3[k]==text_tmp[i]):
                text_tmp[i] = k+1
                break

        for h in range(0,26):
            if(selected_rotor2[h]==text_tmp[i]):
                text_tmp[i] = h+1
                break

        for m in range(0,26):
            if(selected_rotor1[m]==text_tmp[i]):
                text_tmp[i] = m+1
                break

        #returning from the rotors to the plugboard
        if(plugboard[text_tmp[i]-1] != 0):
            for n in range(0,26):
                if(n == text_tmp[i]-1):
                    continue
                elif(plugboard[n]==plugboard[text_tmp[i]-1]):
                    text_tmp[i] = n+1
                    break

        text_tmp[i] = text_tmp[i] + 96

    for i in range(0,text_length):              #after all letters are encrypted, the values are converted from ascii to letters.
        text_final[i] = chr(text_tmp[i])        
    
    print("crypted text:")
    print("".join(text_final))                  #reshaping it from array to a single piece of string
    print("")

    for i in range(26):
        plugboard[i] = 0

    for i in range(3):
        rotor_selection[i] = 0
        rotor_index[i] = 0

    text_length = 0
    text_ascii.clear()

def menu():
    menu=1
    print("Hello, thank you for using virtual enigma\nPlease do not go beyond the instructions shown to you")
    print("Take note of the settings you entered in order to decode the encrypted text.\nBy entering the same settings, you can access the decrypted text after entering the encrypted text.")
    menu = input("Press 1 to encrypt the text, press 0 to quit the application.\n")
    menu = int(menu)
    while menu<0 or menu>1:
        menu = input("please do not enter any value other than 1 or 0\n")
        menu = int(menu)

    menu = int(menu)
    while(menu==1):
        rotor_alignment()
        rotor_index_selection()
        plugboard_selection()
        text_input()
        enigma()
        menu = input("Press 1 to encrypt the text, press 0 to quit the application.\n")
        menu = int(menu)
        while menu<0 or menu>1:
            menu = input("please do not enter any value other than 1 or 0\n")
            menu = int(menu)
    print("Have a nice day!")

menu()