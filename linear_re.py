"""linear sum"""
def linear_sum(S,n):       #S is the array of numbers
  if n==0:
    return 0
  else:
    return linear_sum(S,n-1) + S[n-1]
    
"""reversing recurtion"""
def reverse(S,start,stop):
  if start< stop-1:
    S[start],S[stop-1]=S[stop-1],S[start]
    reverse(S,start+1,stop-1)

"""powers"""
def power(x,n):
  if n==0:
    return 1
  else:
    return x*power(x,n-1)
#trivial recursion now will see using repeated squaring

def power_s(x,n):
  if n==0:
    return 1
  else:
    partial=power_s(x,n//2)
    result=partial*partial
    if n%2==1:
      result *=x
    return result
    
