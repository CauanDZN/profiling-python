@profile
def exemplo_funcao(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

if __name__ == "__main__":
    exemplo_funcao(1000000)

# Executando a linha de comando
# kernprof -l -v line_profiler_test.py