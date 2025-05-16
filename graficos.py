import matplotlib.pyplot as plt
import numpy as np

### --->>> DADOS PYTHON 
labels_py_orig = ['Python (Bubble Sort)', 'Python (Quick Sort)']
media_tempo_py = [515642.10, 137.24]
mediana_tempo_py = [511377.835, 135.13]
media_memoria_py = [0.29, 1320.12]
mediana_memoria_py = [0.29, 1320.12]

### --->>> DADOS JAVA
labels_java_orig = ['Java (Bubble Sort)', 'Java (Quick Sort)']
media_tempo_java = [3792.03, 27.70]
mediana_tempo_java = [3777.78, 27.31]
media_memoria_java = [18385.66, 12288.00]
mediana_memoria_java = [18374.39, 12288.00]

labels_combinados = ['Py Bubble', 'Py Quick', 'Java Bubble', 'Java Quick']

media_tempo_combinada = media_tempo_py + media_tempo_java
mediana_tempo_combinada = mediana_tempo_py + mediana_tempo_java

media_memoria_combinada = media_memoria_py + media_memoria_java
mediana_memoria_combinada = mediana_memoria_py + mediana_memoria_java

x_combinado = np.arange(len(labels_combinados)) 
width = 0.35 

def autolabel(rects, ax, is_ms=False):
    for rect in rects:
        height = rect.get_height()
        if (is_ms and 0 < height < 1) or \
           (not is_ms and 0 < height < 1):
             label_text = f'{height:,.3f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
        else:
            label_text = f'{height:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

        ax.annotate(label_text,
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=8) 

### --->>> GRÁFICO COMBINADO DE TEMPO DE EXECUÇÃO
fig_tempo_combinado, ax_tempo_combinado = plt.subplots(figsize=(12, 7))
rects1_tempo_combinado = ax_tempo_combinado.bar(x_combinado - width/2, media_tempo_combinada, width, label='Média', color='skyblue')
rects2_tempo_combinado = ax_tempo_combinado.bar(x_combinado + width/2, mediana_tempo_combinada, width, label='Mediana', color='lightcoral')

ax_tempo_combinado.set_ylabel('Tempo (ms)')
ax_tempo_combinado.set_title('Comparativo de Tempo de Execução - Python vs Java', fontsize=14)
ax_tempo_combinado.set_xticks(x_combinado)
ax_tempo_combinado.set_xticklabels(labels_combinados, rotation=10, ha="right") 
ax_tempo_combinado.legend()

autolabel(rects1_tempo_combinado, ax_tempo_combinado, is_ms=True)
autolabel(rects2_tempo_combinado, ax_tempo_combinado, is_ms=True)

fig_tempo_combinado.tight_layout()
plt.show()

### --->>> GRÁFICO COMBINADO DE USO DE MEMÓRIA
fig_memoria_combinado, ax_memoria_combinado = plt.subplots(figsize=(12, 7))
rects1_memoria_combinado = ax_memoria_combinado.bar(x_combinado - width/2, media_memoria_combinada, width, label='Média', color='skyblue')
rects2_memoria_combinado = ax_memoria_combinado.bar(x_combinado + width/2, mediana_memoria_combinada, width, label='Mediana', color='lightcoral')

ax_memoria_combinado.set_ylabel('Memória (KB)')
ax_memoria_combinado.set_title('Comparativo de Uso de Memória - Python vs Java', fontsize=14)
ax_memoria_combinado.set_xticks(x_combinado)
ax_memoria_combinado.set_xticklabels(labels_combinados, rotation=10, ha="right")
ax_memoria_combinado.legend()

autolabel(rects1_memoria_combinado, ax_memoria_combinado)
autolabel(rects2_memoria_combinado, ax_memoria_combinado)

fig_memoria_combinado.tight_layout()
plt.show()