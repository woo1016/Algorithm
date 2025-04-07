import sys
import math

input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

denominator = b * d
a_molecule = a * d
c_molecule = c * b
molecule = a_molecule + c_molecule

k = math.gcd(molecule, denominator)
print(molecule//k, denominator//k)