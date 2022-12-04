with open("input.txt", 'r') as file:
    lines = file.readlines()

cont=0
for line in lines :
   
    args = line.split(',')
    p1_s = args[0].split('-')[0]
    p1_e = args[0].split('-')[1]
    p2_s = args[1].split('-')[0]
    p2_e = args[1].split('-')[1]
    
    if(int(p1_s)<=int(p2_s) and int(p1_e)>=int(p2_e)):
        cont+=1        
    elif(int(p2_s)<=int(p1_s) and int(p2_e)>=int(p1_e)):
        cont+=1
    #pair = (args[0], args[1])

print(cont)