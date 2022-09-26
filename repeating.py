main_str =[]
index_str =[]
name=input("enter the word :")
for i in name:
    index_str.append(name.count(i))
    main_str.append(i)
print(main_str)
print(index_str)
m=index_str.index(max(index_str))
print(*main_str[m])