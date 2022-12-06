with open("input.txt", 'r') as file:
    line= file.readline()

i=0
for i in range(len(line)):
    cont  = set()
    for j in range(4):
        cont.add(line[i+j])

    if len(cont)==4: 
        print(str(i+4)) 
        break