import day3_1
from collections import Counter

cont=0
elfGroup = list()
sum_Badges = 0
groups=0

for line in day3_1.lines:
    elfGroup.append(line)

    if cont==2 :
        c1 = Counter(elfGroup[0])
        c2 = Counter(elfGroup[1])
        c3 = Counter(elfGroup[2])
        group_badge = c1 & c2 & c3
        badge = list(group_badge.keys())[0]
        sum_Badges += day3_1.dic[badge]
        cont=0
        elfGroup =[]
    else:
        cont+=1

print(sum_Badges) 
