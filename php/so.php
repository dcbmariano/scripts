<?php 

//GLOB
// arquivos php

// arquivos txt
$arquivos_txt = glob('*.txt');
@mkdir('txt');

foreach($arquivos_txt as $i){
    echo '<br><b>'.$i.'</b><br>';

    $texto = file_get_contents($i);
    echo $texto;

    $w = fopen('txt/'.$i, 'w');
    fwrite($w, $texto);
    fclose($w);
}

