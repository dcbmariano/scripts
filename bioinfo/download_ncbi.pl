#!usr/local/bin/perl

# ----------------------------------------------------------------------------------------------
#
#        info: download FNA do FTP NCBI
#
# description: faz download de um genero inteiro do ftp do ncbi
#
#          by: Diego Mariano
#
#     contato: @DiiegoMariano
#
# ----------------------------------------------------------------------------------------------

use LWP::Simple;

# A lista de bacterias eh previamente configurada em listar_bacterias_ncbi.pl
open (ORG,"lista_bacterias.txt");

$ftp = "ftp://ftp.ncbi.nih.gov/genomes/Bacteria/";

#print "Digite a extensao do arquivo desejada (FNA, GBK, FNN): ";
#$ext = <STDIN>;
#print "\n";

if($ARGV[0] ne ''){
	$genero = $ARGV[0];
}
else {
	print "Digite o genero que deseja baixar: ";
	chomp($genero = <STDIN>);
	print "\n";
}

#le lista de bacterias
while($linha = <ORG>){
	@itens = split("\t",$linha);

	if($itens[1] =~ /$genero/){
		print "$itens[0]\n";
		# Acesse o FTP do NCBI e baixe toda a pasta
		$pag = get($ftp.$itens[0]);
		@lista = split("\n",$pag);

		# Agora varra todos os itens da pasta buscando a extensãindicada
		foreach $l(@lista){
			if($l =~ /.fna/){
				$linha = substr($l,56);
				open (OUT,">data/$linha");
				$content = get($ftp.$itens[0]."/".$linha);
				print OUT "$content";
				close(OUT);
			}
		}
	}
}

system("pause");
