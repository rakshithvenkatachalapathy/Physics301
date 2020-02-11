u'''
 #>>>[fact(x) for x in range(6)]
#[0, 1, 2

>>> fact(3)
6
'''
def fact(n):
    if n<0 :
        return
    sum=0 
    if n==0 or n==1:
        return n
    else:
        sum = n*fact(n-1)

    return sum
    
if __name__ == "__main__":

    import doctest
    doctest.testmod()

    print(fact(2))
	 
