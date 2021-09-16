#!/usr/bin/python3
# usage: dataset_statistics.py <path to tsv file> <path to sequence.fasta file>


import csv
import sys
import re


dataset_file_path = 'dataset\\training.tsv'  #sys.argv[1]
seq_file_path = 'dataset/training_sequences.fasta'  #sys.argv[2]


pdb_2_chain_2_label = {}

with open(dataset_file_path, 'r') as dataset_file:
    d = csv.reader(dataset_file, delimiter='\t')
    for line in d:
        if line != [] and line[0] == 'pdb_id':  # header
            continue
        if line == []:  # empty line
            continue
        # entries with content
        if line[0] not in pdb_2_chain_2_label:
            pdb_2_chain_2_label[line[0]] = {}
        cath_info_in_one_protein = line[2].split('),(')
        #print(list(line[0]) + cath_info_in_one_protein)  # test
        for bracket in cath_info_in_one_protein:
            if re.match(r'.*[:]{1}([0-9|A-Z])', bracket):  # match object != None, there is a match
                #print(re.match(r'.*[:]{1}([A-Z])', bracket).group(1))  # test
                if bracket.split(',')[-1][-1] == ')':
                    cath_label = bracket.split(',')[-1][:-1]
                else:
                    cath_label = bracket.split(',')[-1]
                if re.match(r'.*[:]{1}([0-9|A-Z])', bracket).group(1) not in pdb_2_chain_2_label[line[0]]:
                    pdb_2_chain_2_label[line[0]][re.match(r'.*[:]{1}([0-9|A-Z])', bracket).group(1)] = {cath_label}
                else:
                    pdb_2_chain_2_label[line[0]][re.match(r'.*[:]{1}([0-9|A-Z])', bracket).group(1)].add(cath_label)


total = 0
counts = {1:0, 2:0, 3:0, 4:0, 6:0}


with open(seq_file_path, 'r') as seq_file:
    for line in seq_file:
        if line == '\n':  # empty line
            continue
        if line.startswith('>'):  # header
            total += 1
            header = line[1:].rstrip().split(':')
            if header[0] in pdb_2_chain_2_label:  # header[0] is pdb id
                if header[1] in pdb_2_chain_2_label[header[0]]:  # header[1] is chain
                    for label in pdb_2_chain_2_label[header[0]][header[1]]:
                        if label.startswith('1.'):
                            counts[1] += 1
                        if label.startswith('2.'):
                            counts[2] += 1
                        if label.startswith('3.'):
                            counts[3] += 1
                        if label.startswith('4.'):
                            counts[4] += 1
                        if label.startswith('6.'):
                            counts[6] += 1


print(total)
print(counts)


'''
pdb_ids = []
cath_labels = []


with open(dataset_file_path, 'r') as dataset_file:
    d = csv.reader(dataset_file, delimiter='\t')
    for line in d:
        #print(line)  # test
        if line != [] and line[0] == 'pdb_id':  # header
            continue
        if line == []:  # empty line
            continue
        # entries with content
        if line[0] not in pdb_ids:
            pdb_ids.append(line[0])
        cath_info_in_one_protein = line[2].split('),(')
        #print(cath_info_in_one_protein)  # test
        labels_in_one_protein = []
        for seg in cath_info_in_one_protein:
            if seg.split(',')[-1][-1] == ')':
                cath_label = seg.split(',')[-1][:-1]
            else:
                cath_label = seg.split(',')[-1]
            if cath_label not in labels_in_one_protein:  # version 2
                labels_in_one_protein.append(cath_label)  # version 2
            #labels_in_one_protein.append(cath_label)  # version 1
        for label in labels_in_one_protein:
            cath_labels.append(label)


counts = {1:0, 2:0, 3:0, 4:0, 6:0}


for code in cath_labels:
    if code.startswith('1.'):
        counts[1] += 1
    if code.startswith('2.'):
        counts[2] += 1
    if code.startswith('3.'):
        counts[3] += 1
    if code.startswith('4.'):
        counts[4] += 1
    if code.startswith('6.'):
        counts[6] += 1


print(counts)
print(len(pdb_ids))
'''