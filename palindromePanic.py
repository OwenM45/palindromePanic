#opens input file
inputFile = open("DATA12.txt","r")
#puts input file into an array
data = inputFile.readlines()

#loops through the data
for line in data:
    #setup the substrings
    substring1 = ''
    substring2 = ''
    #setup the sub palindrome lengths
    lengthF = 0
    lengthB = 0

    #setup forward fed letters
    letters = list(line)
    del letters[len(letters)-1]

    #setup backward fed letters
    letters2 = list(line[::-1])
    del letters2[0]

    #check if line is not already a palindrome
    if (line != line[::-1]):     
        #check for sunpalindromes
        for letter in letters:
            substring1 += letter
            substring2 = substring1 [::-1]
            
            if substring1 == substring2 and len(substring1) >= 2:
                lengthF = len(substring1)
            elif lengthF != 0:
                substring1[:-1]
                substring2[:-1]
                           

        substring1 = ''
        substring2 = ''
        #check for sub palindromes
        for letter in letters2:
            substring1 += letter
            substring2 = substring1 [::-1]
            
            if substring1 == substring2 and len(substring1) >= 2 :
                lengthB = len(substring1)
            elif lengthB != 0:
                substring1[:-1]
                substring2[:-1]

        #check if there were palindromes on both sides     
        if (lengthF != 0 and lengthB != 0):
            #check if whole string is a palindrome
            if(lengthB == len(line)-1):
                print("0")
            #check for smallest sub palindrome
            elif (lengthF <= lengthB):
                #check if sub palindromes overlap
                if lengthF + lengthB > len(line)-1:
                    if lengthF >= lengthB: print(lengthB - 1)
                    if lengthB > lengthF: print(lengthF - 1)
                #check for space inbetween sub plaindromes
                elif lengthF + lengthB < len(line)-1:
                    if lengthF >= lengthB: print(len(line) - lengthF-1)
                    if lengthB > lengthF: print(len(line) - lengthB-1)
                else:
                    print(lengthF)
            #check for smallest sub palindrome
            elif (lengthB < lengthF):
                if lengthF + lengthB > len(line)-1:
                    if lengthF >= lengthB: print(lengthB - 1)
                    if lengthB > lengthF: print(lengthF - 1)
                #check for letters inbetween sub plaindromes
                elif lengthF + lengthB < len(line)-1:
                    if lengthF >= lengthB: print(len(line) - lengthF-1)
                    if lengthB > lengthF: print(len(line) - lengthB-1)
                else:
                    print(lengthB)
        else:
            #checks if there only one subpalindrome
            if (lengthF != 0 and len(substring1) - lengthF > 0):
                print(len(line) - lengthF-1)
            if (lengthB != 0 and len(substring1) - lengthB > 0):
                print(len(line) - lengthB-1)
            
    else:
        print("0")
                

inputFile.close()
 
