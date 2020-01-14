mylist = ['sympathize.', 'sufficient.', 'delightful.', 'contrasted.','unsatiable']
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(len(mylist)):
    for v in vowels:
        mylist[i] = mylist[i].replace(v,"")
print(mylist)


l = ['sympathize.', 'sufficient.', 'delightful.', 'contrasted.', 'unsatiable']

table = str.maketrans('', '', 'aeiou')

print ([s.translate(table) for s in l])
