#!usr/local/bin/perl

# ----------------------------------------------------------------------------------------------
#
# info: blast genero
#
# description: faz blast da query contra todos os elementos do genero
#
# by: Diego Mariano
#
# contato: @DiiegoMariano
#
# ----------------------------------------------------------------------------------------------

$diretorio = "lacto";
$q = "Ll-NCDO2118_out.unpadded.fasta";

# Leia todo o diretó de arquivos de referêia
opendir(DIR,"$diretorio/.");
@arquivos = readdir(DIR);
close(DIR);

foreach $arquivo(@arquivos){
	if($arquivo =~ /.fna/){
		push (@fastas,$arquivo);
	}
}


# Agora leia o arquivo de contigs
foreach $f(@fastas){
	print $f."\n";
	$query = "blastn -subject $diretorio/$f -query $q -outfmt \"6 sacc score\" >> result.txt";
	#print "\n\n$query\n";
	system($query);
}
