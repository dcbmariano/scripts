#!/usr/bin/perl
#
#              INGLÊS/ENGLISH
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  http://www.gnu.org/copyleft/gpl.html
#
#
#             PORTUGUÊS/PORTUGUESE
#  Este programa é distribuído na expectativa de ser útil aos seus
#  usuários, porém NÃO TEM NENHUMA GARANTIA, EXPLÍCITAS OU IMPLÍCITAS,
#  COMERCIAIS OU DE ATENDIMENTO A UMA DETERMINADA FINALIDADE.  Consulte
#  a Licença Pública Geral GNU para maiores detalhes.
#  http://www.gnu.org/copyleft/gpl.html
#
#  Copyright (C) 2010  Federal University Of Pará
#
#  Laboratório de Polimorfismo de DNA
#  Pós-graduação em Bioinformática
#  Universidade Federal do Pará
#  Rua Augusto Corrêa, 01 - Guamá. Caixa postal 479.
#  Belém - Pará
#  Brasil
#  CEP 66075-110
#  
#
#  Rommel Ramos
#  rommelramos@ufpa.br
#  www.rommelramos.com
#  http://lpdna.ufpa.br
#
# $Id$

=head1 VERSION 
0.1
=head1 SYNOPSIS

=head1 ABSTRACT

=head1 DESCRIPTION
Percorre um arquivo multifasta retirando as sequencias que estao na lista de referencia
=head1 AUTHOR

Rommel Ramos E<lt>rommelramos@ufpa.br<gt>

Copyright (c) 2010 Federal University Of Pará - Brazil

=head1 LICENSE

GNU General Public License

http://www.gnu.org/copyleft/gpl.html

=cut
use strict;
#use Bio::SeqIO;
use Getopt::Long;


my $csfastaFile; #Arquivo de FASTA de entrada
my $outputCsfastaFile; #Arquivo de FASTA de entrada
my $qualFile; #arquivo fasta de saida
my $outputQualFile; #arquivo fasta de saida
my $phred; # Qualidade Phred e Corte
my $usage = qq(

Realiza o filtro de qualidade sobre os dados oriundos do sequencimento

Sintaxe :  perl $0 [Option]

Opção:   -c           csfastaFile

         -q           qualFile
	 -p           phred
         -oc           output
         -oq           output

Examplo: perl $0 -c solid.fasta -q solid.qual -p 20 -oc saida.csfasta -oq saida.qual



Version: 0.2

Date   : 2011-04-2
Developed by Rommel Ramos
\n);

my %opts;

GetOptions

(

	\%opts,

	"c:s"=>\$csfastaFile,

	"q:s"=>\$qualFile,
	"p:s"=>\$phred,
	"oc:s"=>\$outputCsfastaFile,
	"oq:s"=>\$outputQualFile,

);

die($usage) if (((!defined $csfastaFile) ||(!defined $qualFile) ||(!defined $phred) ||(!defined $outputCsfastaFile) ||(!defined $outputQualFile)));


my $arqSaida;
my %readsFasta;
my $outQual;
my $outCsfasta;
my $readsQual;
my $cabecalho;
my $linha;
my $chave;
my $cont;
my $contFilter;
carregaFasta($csfastaFile,\%readsFasta);
print scalar (keys %readsFasta) . " fasta sequences were loaded.\n";

open($outQual, ">", $outputQualFile);
open($outCsfasta, ">", $outputCsfastaFile);
open($readsQual, "<", $qualFile);
$linha = readline($readsQual);
$cont=0;
$contFilter=0;
 while ($linha){
 $cabecalho = substr($linha,0,1);
 if ($cabecalho eq ">"){
    $cont++;
    $chave = $linha;
    chomp($chave);
    $chave =~ s/\>//g;
    $linha = readline($readsQual);
    if ( getMedia($linha) >= $phred ){
      print $outQual ">".$chave."\n";
      print $outQual $linha;
      print $outCsfasta ">".$chave."\n";
      print $outCsfasta %readsFasta->{$chave};
      $contFilter++;
    }
  }
 $linha = readline($readsQual);
 }
print $cont . " quality sequences were loaded.\n";
print $contFilter." sequences remaing after the filter.\n";

sub carregaFasta{
 my ($inputFile,$sequenciasEntrada) = @_;
 my $entrada;
 my $cabecalho;
 my $linha;
 my $chave;
 open($entrada,"<",$inputFile);
 $linha = readline($entrada);
 while ($linha){
 $cabecalho = substr($linha,0,1);
 if ($cabecalho eq ">"){
    $chave = $linha;
    chomp($chave);
    $chave =~ s/\>//g;
    $linha = readline($entrada);
    $sequenciasEntrada->{$chave}=$linha;
  }
 $linha = readline($entrada);
 } 
 close($entrada);
}

#Recebe a sequencia e verifica a média
sub getMedia(){
 my ($seq) = @_;
 my @array = split(" ",$seq);
 my $arrayLength= scalar @array;
 my $count=0;
 my $sum=0;
 my $average=0;
for( $count=0;$count<$arrayLength;$count++){
 $sum+=$array[$count];
}
$average=$sum/$arrayLength;
return $average;
}

