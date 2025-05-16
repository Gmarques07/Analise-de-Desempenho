class No(var valor: Int) {
    var prox: No? = null
}

class ListaEncadeada {
    var head: No? = null

    fun inserir(valor: Int, pos: Int) {
        val novo = No(valor)
        if (pos <= 0 || head == null) {
            novo.prox = head
            head = novo
            return
        }
        var atual = head
        var indice = 0
        while (atual?.prox != null && indice < pos - 1) {
            atual = atual.prox
            indice++
        }
        novo.prox = atual?.prox
        atual?.prox = novo
    }

    fun remover(valor: Int) {
        var atual = head
        var anterior: No? = null
        while (atual != null) {
            if (atual.valor == valor) {
                if (anterior != null) {
                    anterior.prox = atual.prox
                } else {
                    head = atual.prox
                }
                return
            }
            anterior = atual
            atual = atual.prox
        }
    }

    fun imprimir() {
        var atual = head
        val valores = mutableListOf<String>()
        while (atual != null) {
            valores.add(atual.valor.toString())
            atual = atual.prox
        }
        println(valores.joinToString(" "))
    }
}
    fun main() {
        val start = System.nanoTime()

        val linhas = java.io.File("C:/Users/Gabriel/Desktop/Atividade/arq-novo.txt").readLines()
        val primeiraLinha = linhas[0].replace("\uFEFF", "").trim()
        val valoresIniciais = primeiraLinha.split(" ")
            .filter { it.isNotBlank() }
            .map { it.trim().toInt() }
        val qtd = linhas[1].trim().toInt()
        val comandos = linhas.subList(2, 2 + qtd)

        val lista = ListaEncadeada()
        for (v in valoresIniciais.reversed()) {
            lista.inserir(v, 0)
        }

        for (comando in comandos) {
            if (comando.isBlank()) continue
            val partes = comando.trim().split(" ")
            when (partes[0]) {
                "A" -> {
                    val valor = partes[1].trim().toInt()
                    val pos = partes[2].trim().toInt()
                    lista.inserir(valor, pos)
                }
                "R" -> {
                    val valor = partes[1].trim().toInt()
                    lista.remover(valor)
                }
                "P" -> lista.imprimir()
            }
        }

        val end = System.nanoTime()
        val tempoSegundos = (end - start) / 1_000_000_000.0
        println("Tempo de execução: %.6f segundos".format(tempoSegundos))
    }
