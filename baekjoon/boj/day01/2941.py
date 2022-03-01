

word = input()
cl =['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in cl:
    word = word.replace(i, 'a')
      
print(len(word))