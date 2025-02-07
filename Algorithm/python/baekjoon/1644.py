n= int(input())
if n == 1:
   print(0)

else:
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
      if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

    l = 0
    r = 0
    summ = primes[l]
    cnt = 0
    while r < len(primes):
        if n > summ:
          r += 1
          if r >= len(primes):
             break
          summ += primes[r]

        elif n < summ:
           summ -= primes[l]
           l += 1
        elif n == summ:
           cnt += 1
           r += 1
           if r >= len(primes):
              break
           summ += primes[r]


    print(cnt)