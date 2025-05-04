<?php

class No {
    public $valor;
    public $prox = null;

    public function __construct($valor) {
        $this->valor = $valor;
    }
}

class ListaEncadeada {
    public $head = null;

    public function inserir($valor, $pos) {
        $novo = new No($valor);
        if ($pos <= 0 || $this->head === null) {
            $novo->prox = $this->head;
            $this->head = $novo;
            return;
        }
        $atual = $this->head;
        $indice = 0;
        while ($atual->prox !== null && $indice < $pos - 1) {
            $atual = $atual->prox;
            $indice++;
        }
        $novo->prox = $atual->prox;
        $atual->prox = $novo;
    }

    public function remover($valor) {
        $atual = $this->head;
        $anterior = null;
        while ($atual !== null) {
            if ($atual->valor == $valor) {
                if ($anterior !== null) {
                    $anterior->prox = $atual->prox;
                } else {
                    $this->head = $atual->prox;
                }
                return;
            }
            $anterior = $atual;
            $atual = $atual->prox;
        }
    }
    public function imprimir() {
        $atual = $this->head;
        $valores = [];
        while ($atual !== null) {
            $valores[] = $atual->valor;
            $atual = $atual->prox;
        }
        echo implode(' ', $valores) . PHP_EOL;
    }
}

$start = microtime(true);

$linhas = file('arq-novo.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

$primeiraLinha = preg_replace('/^\xEF\xBB\xBF/', '', trim($linhas[0])); // Tratamento do BOM
$valoresIniciais = array_map('intval', preg_split('/\s+/', $primeiraLinha));
$qtd = intval(trim($linhas[1]));
$comandos = array_slice($linhas, 2, $qtd);

$lista = new ListaEncadeada();
for ($i = count($valoresIniciais) - 1; $i >= 0; $i--) { // (em ordem reversa)
    $lista->inserir($valoresIniciais[$i], 0);
}

foreach ($comandos as $comando) {
    $comando = trim($comando);
    if ($comando === '') continue;
    $partes = preg_split('/\s+/', $comando);
    if ($partes[0] === 'A') {
        $valor = intval($partes[1]);
        $pos = intval($partes[2]);
        $lista->inserir($valor, $pos);
    } elseif ($partes[0] === 'R') {
        $valor = intval($partes[1]);
        $lista->remover($valor);
    } elseif ($partes[0] === 'P') {
        $lista->imprimir();
    }
}

$end = microtime(true);
$tempo = $end - $start;
printf("Tempo de execução: %.6f segundos\n", $tempo);
