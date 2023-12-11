<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabela de livros</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
  
</head>
<body>

    <?php $arquivo = fopen('livros.csv', 'r'); ?>

    <table class="table table-striped table-hover table-sm">

        <?php while($linha = fgets($arquivo)): ?>

            <tr>
                <?php $celulas = explode("\t",$linha); ?>

                <?php foreach($celulas as $celula): ?>
                    <td><?=$celula?></td>
                <?php endforeach; ?>
            </tr>

        <?php endwhile; ?>

    </table>
</body>
</html>