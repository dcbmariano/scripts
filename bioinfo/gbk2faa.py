#! /usr/bin/python
#     Program: gbk2faa.py
#    Function: Converte GBK cocm FAA
# Description: 
#      Author: Diego Mariano
#     Version: 1

from Bio import GenBank
from Bio import SeqIO
import sys

gbk_filename = sys.argv[1]
faa_filename = "%s_out.faa" %gbk_filename

input_handle  = open(gbk_filename, "r")
output_handle = open(faa_filename, "w")

for seq_record in SeqIO.parse(input_handle, "genbank") :
    print "Dealing with GenBank record %s" % seq_record.id
    for seq_feature in seq_record.features :
        if seq_feature.type=="CDS" :
            assert len(seq_feature.qualifiers['translation'])==1
            output_handle.write(">%s from %s\n%s\n" % (
                   seq_feature.qualifiers['locus_tag'][0],
                   seq_record.name,
                   seq_feature.qualifiers['translation'][0]))

output_handle.close()
input_handle.close()
print "Done"