# https://www.codewars.com/kata/5552101f47fc5178b1000050/solutions/python

def dig_pow(n, p):
  s = str(n)
  sum, i = 0, 0
  for x in s:
    sum += int(x) ** (p + i)
    i = i + 1
  
  return (sum / n if(sum % n == 0) else -1)
      
print(dig_pow(89, 1))
