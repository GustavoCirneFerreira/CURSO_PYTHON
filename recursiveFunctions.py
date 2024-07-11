# Every recursive function must have:
#   - A problem that can be divided into little problems;
#   - A recursive case that solves that little problem;
#   - A base case that stops the recursion.

# def recursiva(inicio=0, fim=10):
#     # Base case:
#     if inicio >= fim:
#         return inicio
#     # Recursive case:
#     # Count the numbers till the end
#     inicio += 1
#     return recursiva(inicio, fim)

# print(recursiva())

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
        print(resultado)
    return resultado


print(fatorial(5))
# recursiva()

    