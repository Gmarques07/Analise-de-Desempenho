import time
import tracemalloc

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[-1]
        menores = [x for x in lista[:-1] if x <= pivot]
        maiores = [x for x in lista[:-1] if x > pivot]
        return quick_sort(menores) + [pivot] + quick_sort(maiores)

def read_numeros(file_path):
    numeros = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                number = float(line.strip())
                numeros.append(number)
            except:
                pass
    return numeros

def write_numeros(lista, file_path):
    with open(file_path, 'w') as file:
        for number in lista:
            file.write(f"{number}\n")

def medir_tempo_memoria(func, *args):
    tracemalloc.start()
    inicio = time.perf_counter()
    resultado = func(*args)
    fim = time.perf_counter()
    memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    tempo_ms = (fim - inicio) * 1000
    return resultado, tempo_ms, memoria_pico

def main():
    arquivo_entrada = "arq.txt"
    numeros = read_numeros(arquivo_entrada)

    ## ---> Bubble Sort
    copia_bubble = numeros.copy()
    ordenado_bubble, tempo_bubble, pico_bubble = medir_tempo_memoria(bubble_sort, copia_bubble)
    write_numeros(ordenado_bubble, "arq-saida-bubble.txt")

    ## ---> Quick Sort
    copia_quick = numeros.copy()
    ordenado_quick, tempo_quick, pico_quick = medir_tempo_memoria(quick_sort, copia_quick)
    write_numeros(ordenado_quick, "arq-saida-quick.txt")

    print("\nConfiguração do sistema: Ryzen 7 5700x, 16 GB RAM, GTX 1650 SUPER")

    print("\n--- Bubble Sort ---")
    print(f"Tempo de execução: {tempo_bubble:.2f} ms")
    print(f"Pico de memória usado: {pico_bubble / 1024:.2f} KB")
    print("Arquivo de saída: arq-saida-bubble.txt")

    print("\n--- Quick Sort ---")
    print(f"Tempo de execução: {tempo_quick:.2f} ms")
    print(f"Pico de memória usado: {pico_quick / 1024:.2f} KB")
    print("Arquivo de saída: arq-saida-quick.txt")

if __name__ == "__main__":
    main()