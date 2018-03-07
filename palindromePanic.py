inputFile = open("DATA10.txt","r")

data = inputFile.readlines()

for line in data:
    substring1 = ''
    substring2 = ''
    lengthF = 0
    lengthB = 0

    letters = list(line)
    del letters[len(letters)-1]

    letters2 = list(line[::-1])
    del letters2[0]

    if (line != line[::-1]):
    
        for letter in letters:
            substring1 += letter
            substring2 = substring1 [::-1]
            remainderStr = ''.join(letters).replace(substring1, "")
            
            if substring1 == substring2 and len(substring1) >= 2:
                lengthF = len(substring1)
                if (len(letters) - lengthF <= lengthF and remainderStr == remainderStr[::-1]):
                    print(lengthF)
                else:
                    print(len(letters) - lengthF)
            

        substring1 = ''
        substring2 = ''
        
        for letter in letters2:
            substring1 += letter
            substring2 = substring1 [::-1]
            remainderStr = ''.join(letters).replace(substring1, "")
            
            if substring1 == substring2 and len(substring1) >= 2 :
                lengthB = len(substring1)
                if (len(letters) - lengthB <= lengthB and remainderStr == remainderStr[::-1]):
                    print(lengthB)
                else:
                    print(len(letters) - lengthB)
    else:
        print("0")
                

inputFile.close()
 
