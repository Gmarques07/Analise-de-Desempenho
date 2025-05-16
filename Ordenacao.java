import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.lang.management.ManagementFactory;
import java.lang.management.MemoryMXBean;
import java.lang.management.MemoryUsage;

public class Ordenacao {

    public static void bubbleSort(List<Double> arr) {
        int n = arr.size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr.get(j) > arr.get(j + 1)) {
                    double temp = arr.get(j);
                    arr.set(j, arr.get(j + 1));
                    arr.set(j + 1, temp);
                }
            }
        }
    }

    public static List<Double> quickSort(List<Double> lista) {
        if (lista.size() <= 1) {
            return lista;
        } else {
            double pivot = lista.get(lista.size() - 1);
            List<Double> menores = new ArrayList<>();
            List<Double> maiores = new ArrayList<>();
            for (int i = 0; i < lista.size() - 1; i++) {
                if (lista.get(i) <= pivot) {
                    menores.add(lista.get(i));
                } else {
                    maiores.add(lista.get(i));
                }
            }
            List<Double> resultado = quickSort(menores);
            resultado.add(pivot);
            resultado.addAll(quickSort(maiores));
            return resultado;
        }
    }

    public static List<Double> carregarNumeros(String caminhoArquivo) {
        List<Double> numeros = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(caminhoArquivo))) {
            String linha;
            while ((linha = br.readLine()) != null) {
                try {
                    double numero = Double.parseDouble(linha.trim());
                    numeros.add(numero);
                } catch (NumberFormatException e) {
                }
            }
        } catch (IOException e) {
            System.err.println("Erro ao ler o arquivo: " + e.getMessage());
        }
        return numeros;
    }

    public static void salvarNumeros(List<Double> lista, String caminhoArquivo) {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(caminhoArquivo))) {
            for (Double numero : lista) {
                bw.write(numero.toString());
                bw.newLine();
            }
        } catch (IOException e) {
            System.err.println("Erro ao escrever no arquivo: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        String arquivoEntrada = "arq.txt";
        List<Double> numeros = carregarNumeros(arquivoEntrada);

        if (numeros.isEmpty() && !new java.io.File(arquivoEntrada).exists()) {
            System.out.println("Arquivo de entrada '" + arquivoEntrada + "' não encontrado ou vazio, ou erro na leitura. Encerrando.");
            return;
        }
         if (numeros.isEmpty() && new java.io.File(arquivoEntrada).exists()) {
            System.out.println("Arquivo de entrada '" + arquivoEntrada + "' está vazio ou contém apenas dados inválidos. Os algoritmos serão executados com uma lista vazia.");
        }

        MemoryMXBean memoryMXBean = ManagementFactory.getMemoryMXBean();

        // ---> Bubble Sort
        List<Double> copiaBubble = new ArrayList<>(numeros);

        MemoryUsage beforeBubble = memoryMXBean.getHeapMemoryUsage();
        long inicioBubble = System.nanoTime();
        bubbleSort(copiaBubble);
        long fimBubble = System.nanoTime();

        MemoryUsage afterBubble = memoryMXBean.getHeapMemoryUsage();
        salvarNumeros(copiaBubble, "arq-saida-bubble.txt");
        double tempoBubbleMs = (fimBubble - inicioBubble) / 1e6;

        long memoryUsedBubble = afterBubble.getUsed() - beforeBubble.getUsed();

        // ---> Quick Sort
        List<Double> copiaQuick = new ArrayList<>(numeros);


        MemoryUsage beforeQuick = memoryMXBean.getHeapMemoryUsage();
        long inicioQuick = System.nanoTime();
        copiaQuick = quickSort(copiaQuick);
        long fimQuick = System.nanoTime();

        MemoryUsage afterQuick = memoryMXBean.getHeapMemoryUsage();
        salvarNumeros(copiaQuick, "arq-saida-quick.txt");
        double tempoQuickMs = (fimQuick - inicioQuick) / 1e6;

        long memoryUsedQuick = afterQuick.getUsed() - beforeQuick.getUsed();

        System.out.println("\nConfiguração do sistema: Ryzen 7 5700x, 16 GB RAM, GTX 1650 SUPER");

        System.out.println("\n--- Bubble Sort ---");
        System.out.printf("Tempo de execução: %.2f ms%n", tempoBubbleMs);
        System.out.printf("Memória utilizada: %.2f KB%n", memoryUsedBubble / 1024.0);
        System.out.println("Arquivo de saída: arq-saida-bubble.txt");

        System.out.println("\n--- Quick Sort ---");
        System.out.printf("Tempo de execução: %.2f ms%n", tempoQuickMs);
         System.out.printf("Memória utilizada: %.2f KB%n", memoryUsedQuick / 1024.0);
        System.out.println("Arquivo de saída: arq-saida-quick.txt");
    }
}