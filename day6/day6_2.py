with open("input.txt", 'r') as file:
    line= file.readline()

i=0
bg_msg = 0
for i in range(len(line)):
    cont  = set()
    for j in range(4):
        cont.add(line[i+j])

    if len(cont)==4:
        bg_msg=i+4
        break

for i in range(bg_msg,len(line)):
    print(i)
    cont  = set()
    for j in range(14):
        cont.add(line[i+j])

    if len(cont)==14: 
        print(i+14)
        break
    