#!/usr/bin/perl -w
use Bio::SeqIO;
use strict;


my $fasta = Bio::SeqIO->new( -file => "<$ARGV[0]", -format => 'fasta' );

my $minNlen = 5;
my $out=Bio::SeqIO->new(-file=>">$ARGV[0].parts.fasta",-format=>'fasta');
open(SCAFF,">$ARGV[0].parts.scaff");
while ( my $seqobj = $fasta->next_seq() ) {
	#gets contig id
	my $contig = $seqobj->display_id();
	#gets contig sequence
	my $seq = $seqobj->seq;
	my $lenseq=length $seq;
	$seq = uc $seq; #now all bases are in uppercase

	#Searches for NNNNN regions (scaffold breaks)
	#Hash nregions stores a hash from the contig id to the NNNNN regions found. 
	#Each region is represented as a pair "$ini $end" indicating that start and 
	#the end of the NNNNN region in the contig
	my @regions=();
	my @bases=split //,$seq;
	push(@bases,"E"); #This extra position marks the end of the contig
	my $n=0;
	#Sorry for this loop, but its less memory expensive than regular expressions
	for (my $i=0;$i<=$#bases;$i++) {
		if ($bases[$i] eq 'N') {
			$n++;
		} else {
			if ($n>=$minNlen) {
				my $end=$i;
				my $ini=$end-$n+1;
				push(@regions,"$ini $end");
			}
			$n=0;
		}
	}
	#Now, all regions without Ns are in @regions
	my $cont=1;
	my $laststart=1;
	if ($#regions>=0) {
		for (my $i=0;$i<=$#regions;$i++) {
			my ($ini,$end)=split /\s+/,$regions[$i];
			my $cini=$laststart; my $cend=$ini-1;
			my $pseqobj=$seqobj->trunc($cini,$cend);
			my $new_id=$contig . "_p$cont";
			$cont++;
			$pseqobj->display_id("$new_id");
			$out->write_seq($pseqobj);
			print SCAFF "$new_id $cini $cend\n";
			my $linksize=$end-$ini+1;
			print SCAFF "LINK $ini $end $linksize\n";	
			$laststart=$end+1;
		}
		my $lastregion=$regions[$#regions];
#		print "$lastregion $#regions\n"; die;
		my ($ini,$end)= split /\s+/,$lastregion;
		if (($end+1)<$lenseq) {
			my $cini=$end+1;
			my $cend=$lenseq;
		        my $pseqobj=$seqobj->trunc($end+1,$lenseq);
        		my $new_id=$contig . "_p$cont";
		        $pseqobj->display_id("$new_id");
        		$out->write_seq($pseqobj);
	        	print SCAFF "$new_id $cini $cend\n";
		}
	} else {
	     
		$seqobj->display_id("$contig.1.1");
		$out->write_seq($seqobj);
		print SCAFF "$contig.1.1 1 $lenseq\n";
	}
}
close(SCAFF);

