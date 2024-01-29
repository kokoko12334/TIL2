sum=0
for(i in 1:10){
  
  x=i*dbinom(i, 10, 1/6)
  sum=sum+x
  
 }
print(sum)
