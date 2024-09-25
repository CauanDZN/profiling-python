# Bibliotecas de Profiling em Python

Este documento fornece uma visão geral de três bibliotecas populares para profiling de código Python: **line_profiler**, **cProfile** e **PyInstrument**. Essas ferramentas ajudam a identificar gargalos de desempenho, permitindo que os desenvolvedores otimizem suas aplicações.

## 1. line_profiler

### Descrição
**line_profiler** é uma biblioteca que permite a profilagem linha por linha de funções Python. Com essa ferramenta, você pode ver exatamente quanto tempo cada linha de uma função leva para ser executada.

### Principais Características
- **Profilagem linha por linha**: Fornece informações detalhadas sobre o tempo gasto em cada linha de uma função.
- **Fácil de usar**: Você apenas precisa adicionar um decorador `@profile` acima da função que deseja analisar.
- **Relatório detalhado**: O resultado é apresentado em um formato fácil de entender, mostrando hits, tempo total, e tempo por hit.

### Exemplo de Uso
```python
@profile
def exemplo_funcao(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

# Executando a linha de comando
# kernprof -l -v line_profiler_test.py
```

### Instalação
```bash
pip install line_profiler
```

---

## 2. cProfile

### Descrição
**cProfile** é um profiler integrado ao Python que oferece uma visão geral do desempenho do seu programa. Ele fornece métricas como o número de chamadas para cada função e o tempo total gasto nelas.

### Principais Características
- **Profilagem de funções**: Permite ver o tempo total e o número de chamadas para cada função em seu programa.
- **Fácil de usar**: Basta chamar `cProfile.run()` e passar a função que você deseja analisar.
- **Saídas em diferentes formatos**: Os resultados podem ser exibidos diretamente no console ou salvos em um arquivo para análise posterior.

### Exemplo de Uso
```python
import cProfile

def exemplo_funcao():
    total = 0
    for i in range(10000):
        total += i ** 2
    return total

cProfile.run('exemplo_funcao()')
```

### Instalação
**cProfile** vem embutido com Python, portanto, não é necessário instalar separadamente.

---

## 3. PyInstrument

### Descrição
**PyInstrument** é uma biblioteca de profiling que captura amostras de chamadas de funções durante a execução do seu programa. É particularmente útil para profiling de programas com execução mais longa.

### Principais Características
- **Profilagem baseada em amostras**: Captura amostras periodicamente, proporcionando uma visão geral de onde o tempo está sendo gasto no seu código.
- **Saídas legíveis**: O relatório gerado é bem formatado e fácil de entender.
- **Análise de CPU**: Oferece informações detalhadas sobre o tempo de CPU gasto em cada função.

### Exemplo de Uso
```python
from pyinstrument import Profiler

profiler = Profiler()
profiler.start()

def exemplo_funcao():
    total = 0
    for i in range(10000):
        total += i ** 2
    return total

exemplo_funcao()
profiler.stop()

print(profiler.output_text(unicode=True, color=True))
```

### Instalação
```bash
pip install pyinstrument
```

---

## Conclusão

Essas três bibliotecas oferecem maneiras poderosas de analisar e otimizar o desempenho do seu código Python. A escolha da ferramenta depende do tipo de análise que você deseja realizar:

- Use **line_profiler** para uma análise detalhada linha por linha.
- Use **cProfile** para uma visão geral do desempenho de funções.
- Use **PyInstrument** para capturar amostras em programas mais longos.

Explore cada biblioteca para ver qual se adapta melhor às suas necessidades!