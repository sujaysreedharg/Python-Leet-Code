# Nth Fibonacci number
# O(2^n) Time | O(n) Space
# def fibnormal(n):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     else: return fibnormal(n-1) + fibnormal(n-2)

# DP Top Down Memoization
# O(n) Time | O(n) Space

# def fibtopdown(n,arr):
#     if n in arr:
#         return arr[n]
#     else:
#         arr[n] = fibtopdown(n-1,arr) + fibtopdown(n-2,arr)
#         return arr[n]
# print(fibtopdown(8,{1:0,2:1}))

# DP Bottom up
# O(n) Time | O(1) Space
def fibbottom(n):
    firsttwo = [0, 1]
    counter = 3
    while counter <= n:
        result = firsttwo[0] + firsttwo[1]
        firsttwo[0] = firsttwo[1]
        firsttwo[1] = result
        counter += 1
    return firsttwo[1] if n > 1 else firsttwo[0]


print(fibbottom(8))
