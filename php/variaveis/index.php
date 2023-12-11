<!-- CSS only -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">

<div class="container">

<h1>Contato</h1>

<form action="processa.php" method="POST" enctype="multipart/form-data">

    <label>Nome:</label>
    <input type="text" name="nome" placeholder="Digite o seu nome" class="form-control">

    <label>Assunto:</label>
    <input type="text" name="assunto" placeholder="Digite o assunto" class="form-control">

    <label>Mensagem:</label>
    <textarea name="mensagem" placeholder="Digite a mensagem"  class="form-control"></textarea>

    <label>Anexos:</label>
    <input type="file" name="arquivo">

    <p>
        <input type="submit" name="submit" value="Enviar" class="btn btn-success">
    </p>
</form>


</div>