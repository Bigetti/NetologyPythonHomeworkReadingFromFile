

with open('1.txt', encoding='utf-8') as f:
   
    lines = f.readlines()
    count1 = len(lines)
    print(lines)
    print(count1)
    print()

with open('2.txt', encoding='utf-8') as f:
    lines2 = f.readlines()
    count2 = len(lines2)
    print(lines2)
    print(count2)
    print()
    
with open('3.txt', encoding='utf-8') as f:
    lines3 = f.readlines()
    count3 = len(lines3)
    print(lines3)
    print(count3)
    print()

with open('4.txt', 'a', encoding='utf-8') as f:
    f.write('1.txt\n') 
    f.write(str(count1) +'\n')
    f.writelines(lines)
    f.write('\n')
    f.write('2.txt\n')
    f.write(str(count2)+'\n')
    f.writelines(lines2)
    f.write('\n')
    f.write('3.txt\n')
    f.write(str(count3)+'\n')
    f.writelines(lines3)
    f.write('\n')