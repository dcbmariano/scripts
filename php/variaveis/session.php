<?php 
session_start();

$nome = 'José';
$_SESSION['nome'] = $nome;

echo 'Olá '.$nome;

setcookie('nome_usuario', $nome,  time()+3600);

echo "<br>Cookie salvo para o usuário: ".$_COOKIE['nome_usuario'];

?>

<a href="session2.php?nome=teste">Link</a>