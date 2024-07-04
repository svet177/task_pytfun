import sys, random 
# the list x is going to work as our collection of outputs
x=[]
def generate_permutations(a, n):
        if n == 0:
            # collect all outputs in the list X
            x.append(''.join(a))
            #print(''.join(a))
            #print(x)
        else:
            for i in range(n):
                generate_permutations(a, n-1)
                j = 0 if n % 2 == 0 else i
                a[j], a[n] = a[n], a[j]
                generate_permutations(a, n-1)

            


word = 'Svetlin'

generate_permutations(list(word), len(word)-1)

print(random.sample(x,20))


#len returns length - 3
#list 