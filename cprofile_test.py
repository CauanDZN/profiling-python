import cProfile

def exemplo_funcao():
    total = 0
    for i in range(10000):
        total += i ** 2
    return total

cProfile.run('exemplo_funcao()')
