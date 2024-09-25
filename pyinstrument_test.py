from pyinstrument import Profiler

profiler = Profiler()
profiler.start()

def exemplo_funcao():
    total = 0
    for i in range(1000000):
        total += i ** 2
    return total

exemplo_funcao()

profiler.stop()

print(profiler.output_text(unicode=True, color=True))
