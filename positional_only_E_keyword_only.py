# Controlling the size of positional and named arguments in functions
# args - Unlimited positional arguments
# kwargs - Unlimited named arguments

# Positional-only Parameters (/) - Everything before
#   the bar NEEDS TO BE ONLY POSITIONAL

# Keyword-only Arguments (*) - Everything after 
#   NEEDS TO BE NAMED

def soma(a, b, /, *, c, **kwargs):
    print(a + b + c)
    print(kwargs)

soma(1, 2, c=3, nome='teste')