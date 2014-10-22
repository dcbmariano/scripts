#!/usr/bin/perl -w
# ffn2pseudo.pl - perl script that performs blast of nucleotide multifasta against a whole genome and maps the CDSs and pseudogenes.
#
#
# Written by: Siomar C. Soares, Federal University of Minas Gerais (UFMG), 
#   Laboratory of Celular and Molecular Genetics, Brazil
#
# Date Written: Feb 13, 2014
#
#
#Usage: ffn2pseudo.pl --ffn reference.ffn --fasta new.genome.fasta -e evalue
#Usage: ffn2pseudo.pl --ffn reference.ffn --fasta new.genome.fasta -evalue evalue
#If the evalue is not set, 10e-50 is assumed.
#The penalty for a nucleotide mismatch is 0.
#Other blast parameters were not changed
#
#Do not forget to install fasta36 globally and, also, to install the perl module "Which" using the command "install File::Which" from within CPAN


use strict;
use File::Which; # exports which()
use Getopt::Long;
my $ffn;
my $fasta;
my $evalue = 10e-50;
use constant false => 0;
use constant true  => 1;

############################ Gets the paths for the input files #########################

GetOptions (
	"ffn=s" => \$ffn, # String
	"fasta=s" => \$fasta, # String
	"e|evalue=s" => \$evalue #String
) 
or die(
	"\nUsage: ffn2pseudo.pl --ffn reference.ffn --fasta new.genome.fasta -e evalue\n\n"
);
if ((!defined $ffn)||(!defined $fasta)){
	die(
	"\nThe ffn or fasta file was not defined. Please try again.\nUsage: ffn2pseudo.pl --ffn reference.ffn --fasta new.genome.fasta\n\n"
	);
}

print $ffn." is the ffn reference file\n";
print $fasta." is the fasta of the new genome\n";


############################ Defines blastall executable e execute blastall -p blastn #########################

my $fasta36_exec = which('fasta36');
if ($fasta36_exec == 0){
	print "The fasta36 executable path is ".$fasta36_exec."\n";
}else{
	die(
	"\nThere is no fasta36 executable in Path.\n\n"
	);
}

my $fasta36_ffn = system ($fasta36_exec." -E ".$evalue." -d 1 ".$ffn." ".$fasta." > ".$ffn."--vs--".$fasta.".out");

=pod
fasta36
USAGE
 fasta36 [-options] query_file library_file [ktup]
 fasta36 -help for a complete option list

DESCRIPTION
 FASTA searches a protein or DNA sequence data bank
 version: 36.3.6 Jan, 2014

COMMON OPTIONS (options must preceed query_file library_file)
 -s:  scoring matrix;
 -f:  gap-open penalty;
 -g:  gap-extension penalty;
 -S   filter lowercase (seg) residues;
 -b:  high scores reported (limited by -E by default);
 -d:  number of alignments shown (limited by -E by default);
 -I   interactive mode;

=cut

if ($fasta36_ffn == 0){
	print "The data was correctly aligned\n"
}else{
	die(
	"\nThere was a problem during alignment step. Please review your files.\n\n"
	);
}

############################ The parsing part of the script begins here #########################

my $blast_file = $ffn."--vs--".$fasta.".out";
my $query_start;
my $subj_start;
my $query_end;
my $subj_end;
my $query_sequence;
my $subj_sequence;
my $exon_start;
my $exon_end;
my $subj_head;
my $query_size;
my $percent_alignment;
my $ccc;


my $in;
my $c = 0;
my $cc = -1;
my $ccc = 0;
my $number_of_cdss;
my $lt; #short for locus_tag

my $cds_boolean = false;
my $align_boolean = false;
my $gene_boolean = false;
my $started_boolean = false;
my $subj_head_boolean = false;

my @info;
my @cds_coords;
my @locus_tag;
my @product;
my @gene;
my @strand;
my @cds_line;
my @colour;
my @color_number;
my @note;
my @query_overlap;


my $out;

open (IN, $blast_file);


while ($in = <IN>){
	if (($subj_head_boolean == false)&&($in =~ m/The best scores are/)){
		$in = <IN>;
		@info = split (/[ ]+/, $in);
		$subj_head = $info[0];
		@info = "";
		$subj_head_boolean = true;
	}
	if (($in =~ m/^[ ]+[0-9]+\>\>\>/)||($in =~ m/^[0-9]+\>\>\>/)){
		if ($cc>=0){		
			my $exon = $exon_start."\.\.".$exon_end;
			push(@cds_coords, $exon);
			my $coord = join (", ", @cds_coords);
			$coord =~ s/^\, //g;
			@cds_coords = "";
			if ($coord =~ m/\,/){
				$cds_line[$cc] = "join($coord)";
				$colour[$cc] = "                     \/colour\=2\n                     \/pseudo";
				$note[$cc] = "                     \/note\=\"" . $note[$c] . "\"\n";
				
			}else{
				$cds_line[$cc] = "$coord";
				$colour[$cc] = "                     \/colour\=" . $color_number[$c];
				$note[$cc] = "                     \/note\=\"" . $note[$c] . "\"\n"; 
			}
		}
		my @tmp = split (" ", $in);
		$query_size = pop @tmp;
		$query_size = pop @tmp;
		$started_boolean = false;		
		$cc++;
		$in =~ s/.+\>\>\>//g;
		@info = split (" ", $in);
		$locus_tag[$c] = $info[0];
		if ($info[1] !~ m/.+\_[0-9]+/){
			$gene[$c] = "$info[1]";
			$gene_boolean = true;
		}else{
			$gene[$c] = "";
			$gene_boolean = false;
		}
		$product[$c] = $in;
		while ($product[$c] !~ m/[0-9]+\:[0-9]+/){
			$in = <IN>;
			$product[$c] .= $in;
		}
		$product[$c] =~ s/$locus_tag[$c] //g;
		$product[$c] =~ s/.+$locus_tag[$c] //g;
		if ($gene_boolean == true){
			$product[$c] =~ s/$gene[$c] //g;
		}
		$lt = substr($locus_tag[$c],0,5);
		$product[$c] =~ s/ [0-9]+\:[0-9]+.+//g;
		$product[$c] =~ s/[0-9]+\:[0-9]+.+//g;
		$product[$c] =~ s/\n//g;
		$product[$c] = "                     \/product\=\"".$product[$c]."\"\n";
		$gene[$c] = "                     \/gene\=\"".$gene[$c]."\"\n";
		$locus_tag[$c] = "                     \/locus_tag\=\"".$locus_tag[$c]."\"\n";
		#print $locus_tag.$gene.$product;
		$gene_boolean = false;
		$align_boolean = false;
		#print "$lt\n";
	}
	elsif ($in =~ m/^\!\! No sequences/){
		$product[$c] = "Do not print";
		@cds_coords = "";
		$strand[$c] = "No strand";
		$c++;
	}
	elsif ($in =~ m/\>\>$subj_head/){
		$align_boolean = true;
	}
	elsif (($in =~ m/^banded Smith-Waterman/)&&($align_boolean == true)){
		my $temp = $in;
		$temp =~ s/.+overlap \(//g;
		$temp =~ s/\:.+//g;
		@query_overlap = split("-", $temp);
		if ($query_overlap[0] < $query_overlap[1]){
			$strand[$c] = "     CDS             ";
			$percent_alignment = ((($query_overlap[1] - $query_overlap[0]) + 1)/$query_size)*100;
			$query_start = $query_overlap[0];
			$query_end = $query_overlap[1];
		}else{
			$strand[$c] = "     CDS             complement(";
			$percent_alignment = ((($query_overlap[0] - $query_overlap[1]) + 1)/$query_size)*100;
			$query_start = $query_overlap[1];
			$query_end = $query_overlap[0];
		}
		$temp = $in;
		$temp =~ s/.+\://g;
		$temp =~ s/\)//g;
		my @subj_overlap = split("-", $temp);
		$subj_start = $subj_overlap[0];
		$subj_end = $subj_overlap[1];
		$c++;
		$ccc = $c -1;
		if ($percent_alignment >= 100){
			$color_number[$c] = 3;
			$note[$c] = "Alinhamento de 100%.";
		}
		elsif ($percent_alignment < 100){
			if ($percent_alignment >= 80){
				$color_number[$c] = 4;
				$note[$c] = "Alinhamento de 80 a 100%.";
			}
			else{
				if ($percent_alignment >= 50){
					$color_number[$c] = 6;
					$note[$c] = "Alinhamento de 50 a 80%.";
				}
				else{

					$color_number[$c] = 7;
					$note[$c] = "Alinhamento menor que 50%.";
				}
			}
		}
		if ($query_start > 1){
			$note[$c] .= " Falta o começo.";
		}
		if ($query_end < $query_size){
			$note[$c] .= " Falta o final.";
		}
	}elsif ($in =~ m/^\>\-\-/){
		$align_boolean = false;
	}
#################################### CDSs on forward strand ##################
	elsif (($align_boolean == true)&&($in =~ m/^$lt/)&&($strand[$ccc] !~ m/complement/)){
		$query_sequence = substr($in, 7, 67);
		$in = <IN>;
		my $sequence_align = substr($in, 7, 67);
		$in = <IN>;
		$subj_sequence = substr($in, 7, 67);
		#print "$query_sequence\n$subj_sequence\n";
		if ($started_boolean == false){
			$exon_start = $subj_start;
			my $temp = $query_start-1;
			$temp = $temp % 3;
			$exon_start = $exon_start - $temp;
			$exon_end = $subj_start -1;
			$started_boolean = true;
		}
		for (my $i=0;$i<length $query_sequence;$i++) { 
			my $query_nt = substr($query_sequence,$i,1);
			my $align_points = substr($sequence_align,$i,1);
			my $subj_nt = substr($subj_sequence,$i,1);
			if (($query_nt =~ m/[atgcATGC]/)&&($subj_nt =~ m/[atgcATGC]/)&&($align_points =~ m/\:/)){
				$exon_end = $exon_end + 1;
			}elsif ($query_nt =~ m/\-/){
				my $exon = $exon_start."\.\.".$exon_end;
				$exon_end = $exon_end + 1;
				if ($exon_end > $exon_start){
					push(@cds_coords, $exon);
				}
				$exon_start = $exon_end + 1;
			}elsif ($subj_nt =~ m/\-/){
				my $exon = $exon_start."\.\.".$exon_end;
				if ($exon_end > $exon_start){
					push(@cds_coords, $exon);
				}
				$exon_start = $exon_end;
			}
		}				
	}
#################################### CDSs on Reverse strand ##################
	elsif (($align_boolean == true)&&($in =~ m/^$lt/)&&($strand[$ccc] =~ m/complement/)){
		$query_sequence = substr($in, 7, 67);
		$in = <IN>;
		my $sequence_align = substr($in, 7, 67);
		$in = <IN>;
		$subj_sequence = substr($in, 7, 67);
		#print "$query_sequence\n$subj_sequence\n";
		if ($started_boolean == false){
			$exon_start = $subj_start;
			my $temp = $query_start;
			$temp = $temp % 3;
			$exon_start = $exon_start + $temp;
			$exon_end = $subj_start - 1;
			$started_boolean = true;
		}
		for (my $i=0;$i<length $query_sequence;$i++) {
			my $spacers = 0; 
			my $query_nt = substr($query_sequence,$i,1);
			my $align_points = substr($sequence_align,$i,1);
			my $subj_nt = substr($subj_sequence,$i,1);
			if (($query_nt =~ m/[atgcATGC]/)&&($subj_nt =~ m/[atgcATGC]/)&&($align_points =~ m/\:/)){
				$exon_end = $exon_end + 1;
			}elsif ($query_nt =~ m/\-/){
				my $exon = $exon_start."\.\.".$exon_end;
				$exon_end = $exon_end + 1;
				if ($exon_end > $exon_start){
					push(@cds_coords, $exon);
				}
				$exon_start = $exon_end + 1;
			}elsif ($subj_nt =~ m/\-/){
				my $exon = $exon_start."\.\.".$exon_end;
				if ($exon_end > $exon_start){
					push(@cds_coords, $exon);
				}
				$exon_start = $exon_end;
			}
		}	
	}
}

######## Add and fix the last coordinates ########
my $exon = $exon_start."\.\.".$exon_end;
push(@cds_coords, $exon);
my $coord = join (", ", @cds_coords);
$coord =~ s/^\, //g;
@cds_coords = "";
=pod
if ($coord =~ m/\,/){
	$cds_line[$cc] = "join($coord)";
	$colour[$cc] = "                     \/colour\=2\n                     \/pseudo";
}else{
	$cds_line[$cc] = "$coord";
	$colour[$cc] = "                     \/colour\=".$color_number[$cc];
}
=cut
if ($coord =~ m/\,/){
	$cds_line[$cc] = "join($coord)";
	$colour[$cc] = "                     \/colour\=2\n                     \/pseudo";
	$note[$cc] = "                     \/note\=\"".$note[$c]."\"\n";
				
}else{
	$cds_line[$cc] = "$coord";
	$colour[$cc] = "                     \/colour\=".$color_number[$c];
	$note[$cc] = "                     \/note\=\"".$note[$c]."\"\n"; 
}

###################################################

$number_of_cdss = $c;
$c=0;

for ($ccc = 0; $ccc< $number_of_cdss; $ccc++){
	if ($product[$ccc] !~ m/Do not print/){
		if($strand[$ccc] !~ m/complement/){
			$out .= "$strand[$ccc]$cds_line[$ccc]\n$colour[$ccc]\n$gene[$ccc]$product[$ccc]$note[$ccc]";
		}elsif ($strand[$ccc] =~ m/complement/){
			$out .= "$strand[$ccc]$cds_line[$ccc]\)\n$colour[$ccc]\n$gene[$ccc]$product[$ccc]$note[$ccc]";
		}
	}
}
my $outfile = $fasta."\.tab";
open (OUT, ">$outfile");
print OUT ($out);




