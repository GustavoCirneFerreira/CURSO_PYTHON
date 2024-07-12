# Every recursive function must have:
#   - A problem that can be divided into little problems;
#   - A recursive case that solves that little problem;
#   - A base case that stops the recursion.
# import sys
# sys.setrecursionlimit(1004)


# def recursiva(inicio=0, fim=10):
#     print(inicio, fim)
    
#     # Base case:
#     if inicio >= fim:
#         return inicio
#     # Recursive case:
#     # Count the numbers till the end
    
#     inicio += 1
#     return recursiva(inicio, fim)

# print(recursiva())


# # def fatorial(n):
# #     resultado = 1
# #     for i in range(1, n + 1):
# #         resultado *= i
# #         print(resultado)
# #     return resultado


# # print(fatorial(5))
# recursiva(0, 1001)

def fatorial(n):
    if n <= 1:
        return 1
    
    return n * fatorial(n-1)


print(fatorial(5))
print(fatorial(10))    
    
    