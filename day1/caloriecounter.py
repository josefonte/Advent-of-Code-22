def readInput(filepath):
    with open(filepath, 'r') as file:
            lines = file.readlines()

    register = {}
    elf = "elf"
    elfX = "elf0"
    counter = 0
    listCal = []
    
    for line in lines: 
           
        if line == "\n":
            register[elfX] = listCal
            counter +=1
            elfX = elf + str(counter)
            listCal = []
            
        else :
            cal = line.split("\n")
            listCal.append(int(cal[0]))
            
    
    return register

def findMax(reg:dict):
    max = 0 
    for key, values in reg.items():
        Calsum = sum(values)
        if max < Calsum : 
            max = Calsum 
            elfName = key
        
    return (elfName,max)

def main():
    reg = readInput("input.txt")
    sumCals = 0
    for i in range(3):
        elf, cals = findMax(reg)
        print("("+elf+ " - " + str(cals) + ")")
        sumCals += cals 
        del reg[elf]
    
    print(sumCals)

if __name__ == "__main__":
    main()