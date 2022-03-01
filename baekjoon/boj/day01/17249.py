jab = input()
jab2 = jab.split('(')
print(jab2[0].count('@'), jab2[1].count('@'))
