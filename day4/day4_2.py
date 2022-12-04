import day4_1

sumOL = 0
for line in day4_1.lines:
    args = line.split(',')
    p1_s = args[0].split('-')[0]
    p1_e = args[0].split('-')[1]
    p2_s = args[1].split('-')[0]
    p2_e = args[1].split('-')[1]
    

    r1 = range(int(p1_s), int(p1_e)+1)
    r2 = range(int(p2_s), int(p2_e)+1)
    set1 = set(r1)
    set2 = set(r2)
    intersection = set1.intersection(set2)
    
    print(p1_s + "-"+ p1_e + " | " + p2_s + "-" + p2_e +  str(intersection))

    if len(intersection)!=0:
        sumOL += 1
        print("SUM: "+ str(sumOL)+ "\n")
    else:
        print ("\n")

print(sumOL) 

