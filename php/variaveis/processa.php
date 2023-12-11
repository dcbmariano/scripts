<?php 

if(isset($_POST['submit'])){
    $nome = $_POST['nome'];
    $assunto = $_POST['assunto'];
    $mensagem = $_POST['mensagem'];

    $anexo = $_FILES['arquivo'];

    $pasta = 'gravar/';

    if(move_uploaded_file($_FILES['arquivo']['tmp_name'], $pasta.$_FILES['arquivo']['name'])){
        echo "Gravado com sucesso";
    }
    else{
        echo "Erro.";
    }
    echo "NOME: $nome<br><br>";
    echo "ASSUNTO: $assunto<br><br>";
    echo "MENSAGEM: $mensagem";
}

?>