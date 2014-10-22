#!usr/local/bin/perl

# ----------------------------------------------------------------------------------------------
#
# info: baixar lista de genomas de bactéas e salva em um arquivo
#
# description: faz download da lista de bactéas do NCBI
#
# by: Diego Mariano
#
# contato: @DiiegoMariano
#
# ----------------------------------------------------------------------------------------------

use LWP::Simple;
open (OUT,">lista_bacterias.txt");

$link = "ftp://ftp.ncbi.nih.gov/genomes/Bacteria/";

# Para listar DRAFTS descomente as linhas abaixo
# $link = "ftp://ftp.ncbi.nih.gov/genomes/Bacteria_DRAFT/";
# close(OUT);
# open (OUT,">lista_bacterias_DRAFT.txt");

$pag = get($link);

@lista = split("\n",$pag);

foreach $l(@lista){
	if($l =~ /_/){
		$linha = substr($l,56);
		@separa = split("_",$linha);
		print $linha."\n";
	
		print OUT "$linha\t$separa[0]\t$separa[1]\t$separa[2]\t$separa[3]\t$separa[4]\t$separa[5]\n";
	}
}

close(OUT);
system("pause");
