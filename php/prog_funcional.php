<?php

// PROGRAMAÇÃO FUNCIONAL COM PHP

// declação de funções
function soma_1($a, $b){
    // procedimentos
    echo $a + $b;
}

// soma_1(2, 2);

function soma_2($a, $b){
    // funções
    return $a + $b;
}

// echo soma_2(2, 3);

// funções anônimas
function($a, $b){
    return $a + $b;
};


// first-class function => caracteristica de uma linguagem de programação de aplicar funções a variáveis
// function expression

$soma_3 = function($a, $b){
    return $a+$b;
};

// echo $soma(33, -30);

// IIFE (Immediately Invoked Function Expression)
// (function($a, $b){ echo $a+$b; })(30, 20); // adição
// (function($a, $b){ echo $a - $b; })(99, 34); // subtração

$soma = fn($a, $b) => $a+$b;
$subtracao = fn($a, $b) => $a-$b;
$multiplicacao = fn($a, $b) => $a*$b;
$divisao = fn($a, $b) => $a/$b;

$dobro = fn($x) => $x*2;

echo $dobro(10);
