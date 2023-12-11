<?php 
session_start();

$nome = $_COOKIE['nome_usuario'];
// $nome = $_SESSION['nome'];
echo 'Olá '.$nome;

var_dump($_REQUEST);
var_dump($_SERVER['REQUEST_METHOD']);
?>

<a href="session.php">Link</a>
