#!/usr/local/bin/python3
import os
import sys
import re
import entrezpy.conduit
import entrezpy.esearch.esearcher

#The aim of this section of the proigram is to access the NCBI database and search for the protein and/or organism
Tax1 = input ('Please type the taxonomic group and the protein you wish to search for \n\t')

w = entrezpy.conduit.Conduit('myemail')

#A new pipeline is created and stored in fetch_organism
fetch_organism = w.new_pipeline()

#Search organisms on NCBI
sid = fetch_organism.add_search({'db' : 'protein', 'term' : Tax1, 'rettype':'count', 'sort' : 'Date Released', 'mindate': 2000, ''maxdate':2019, 'datetype' : 'pdat'})
fid = fetch_organism.add_fetch({'retmax' : 10, 'retmode' : 'text', 'rettype' : 'fasta'}, dependancy=sid)

#Run search
print ('Searching...')
analyser = w.run(fetch_organism)

out1 = open ('sequences.fasta', 'w')
print(analyser)
out1.close()

#Ask user if wants to plot conservation of those genes
prog1=input('Do you wish to continue to plot the level of conservation of these genes? (y/n) \n\t')

if y:
        print('Firstly genes need to be aligned')
        align=clustalo -i sequences.fasta -o sequence_alignement
        print('aligning sequences...')
        out2= open ('alignment', 'w')
        print(alignment)
        out2.close()
        plotcon -i alignment -o plot.sequence
        print(plot.cs)

elif n:
        print(´The programme will now close. You can find the outputs of the previous steps in the directory. ')
        Assessment2.py.close()


else:
        print('please introduce a valid answer. ')
        print(prog1)

#Ask the user whether they want to search their sequences against ProSite database
prog2: input('Do you whish to scan your sequences against ProSite database? (y/n) ')

if y:
        out3=prosextract -prositedir -i sequences.fasta -o search.ProSite
        print(out3)
        out4= open('ProSite_results','w')
        print(out3)
        out4.close()


elif n:
        print(´The programme will now close. You can find the outputs of the previous steps in the directory. ')
        Assessment2.py.close()


else:
        print('please introduce a valid answer. ')
        print(prog2)

