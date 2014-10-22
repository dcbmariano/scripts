#!/usr/bin/perl -w

# Program: split_fasta_into_tags.pl

if (scalar(@ARGV) == 1) {
    $fasta_input_file = shift;
}
else {
    die "Usage: $0 fasta_input_file\n\n";
}

open (TAG1, ">tag1.fasta");
open (TAG2, ">tag2.fasta");

$tag_id = '';
$tag_seq = '';
open (FASTA_IN, $fasta_input_file) or die "Can't open input file '$fasta_input_file': $!\n";
while (<FASTA_IN>) {
    chomp;
    if ( /^>(.+)/ ) {
	$new_tag_id = $1;
	if ($tag_seq ne '') {
	    if ( $tag_id =~ /\.r$/ ) {
		print TAG1 ">$tag_id\n$tag_seq\n";
	    }
	    elsif ( $tag_id =~ /\.f$/ ) {
		print TAG2 ">$tag_id\n$tag_seq\n";
	    }
	    else {
		# skip tags that are not .f or .r
	    }
	}
	$tag_id = $new_tag_id;
    }
    else {
	$tag_seq = $_;
	$tag_seq =~ s/[actg]+//g; # remove low quality bases, 
                          # which are in lower case
    }
}

