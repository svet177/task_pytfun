import sys, random
# x is going to collect all our output
x=[]
def generate_permutations(a, n):
    if n == 0:
        # changed from direct output on each iteration to appending values in a list
        x.append(''.join(a))
    else:
        for i in range(n):
            generate_permutations(a, n-1)
            j = 0 if n % 2 == 0 else i
            a[j], a[n] = a[n], a[j]
            generate_permutations(a, n-1)
if len(sys.argv) !=2 :
    sys.stderr.write('Exactly one argument is required\n')
    sys.exit(1)

word = sys.argv[1]

generate_permutations(list(word), len(word)-1)
# output of 20 random values from the cllection of values in the list x (duplicates allowed)
print(random.sample(x,20))