 

tuple_list =[]

with open('1.txt', encoding='utf-8') as f:
   
    lines1 = f.readlines()
    count1 = len(lines1)
    filename1 = '1.txt'
    # print(lines)
    # print(count1)
    # print()
    new_tuple = (filename1, count1, lines1)
    tuple_list.append(new_tuple)

with open('2.txt', encoding='utf-8') as f:
    lines2 = f.readlines()
    count2 = len(lines2)
    filename2 = '2.txt'
    # print(lines2)
    # print(count2)
    # print()
    new_tuple = (filename2, count2, lines2)
    tuple_list.append(new_tuple)
    
with open('3.txt', encoding='utf-8') as f:
    lines3 = f.readlines()
    count3 = len(lines3)
    filename3 = '3.txt'
    # print(lines3)
    # print(count3)
    # print()
    new_tuple = (filename3, count3, lines3)
    tuple_list.append(new_tuple)

print()


sorted_list = sorted(tuple_list, key = lambda x : x[1])
print(sorted_list)
print()

with open('4.txt', 'w', encoding='utf-8') as f:
    for item in sorted_list:
        filename, count, lines = item
        f.write(filename + '\n')
        f.write(str(count) + '\n')
        f.writelines(lines)
        f.write('\n')