<?php 

require_once 'Pessoa.php';

$pessoa1 = new Pessoa('José', '111.222.333-44');
echo 'Nome: ' . $pessoa1->getNome() . '<br>CPF: '. $pessoa1->getCpf();

echo '<br>';

$pessoa2 = new Pessoa('Maria', '222.222.333-91');
echo 'Nome: ' . $pessoa2->getNome() . '<br>CPF: '. $pessoa2->getCpf();
