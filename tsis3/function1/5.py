string=str(input())
import itertools

def permutations(string):
  perms = [''.join(p) for p in itertools.permutations(string)]
  print(*perms, sep=' ')
permutations(string)