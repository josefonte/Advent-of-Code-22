with open("input.txt", 'r') as file :
    lines = file.readlines()

i=0
stacks = {"1":[],"2":[],"3":[],"4":[],"5":[],"6":[],"7":[],"8":[],"9":[]}

moves = {"quant":[],
        "from": [],
        "to":[]}

for line in lines:
    line = line.replace('\n','')
    args = line.split(' ')
    if i<8 :
        space=0
        stack=1
        for arg in args:
            if arg=='' and space<4:
                space+=1
            elif space == 0 and arg!='':
                stacks[str(stack)].insert(0,arg)
                stack+=1 

            if space==4:
               stack+=1 
               space=0 
    elif i==8:
        print("\nINITIAL ARRANGMENT")
        print("1 " + str(stacks["1"]))
        print("2 " + str(stacks["2"]))  
        print("3 " + str(stacks["3"]))
        print("4 " + str(stacks["4"]))
        print("5 " + str(stacks["5"]))
        print("6 " + str(stacks["6"]))
        print("7 " + str(stacks["7"]))
        print("8 " + str(stacks["8"]))
        print("9 " + str(stacks["9"]))


    else :
        j=0
        for arg in args:
            if j==1:
                moves["quant"].append(arg)
            elif j==3:
                moves["from"].append(arg)
            elif j==5:
                moves["to"].append(arg)
            j+=1
    i+=1

i=0
while i<502:
    qt = int(moves["quant"][i])
    fr = moves["from"][i]
    to = moves["to"][i]

    for k in range(qt):
        elem = stacks[fr].pop()
        stacks[to].append(elem) 

    i+=1


print("\nFINAL ARRANGMENT")
print("1 " + str(stacks["1"]))
print("2 " + str(stacks["2"]))
print("3 " + str(stacks["3"]))
print("4 " + str(stacks["4"]))
print("5 " + str(stacks["5"]))
print("6 " + str(stacks["6"]))
print("7 " + str(stacks["7"]))
print("8 " + str(stacks["8"]))
print("9 " + str(stacks["9"]))


print("\nANSWER")
for i in range(1,10):
    print(stacks[str(i)].pop())