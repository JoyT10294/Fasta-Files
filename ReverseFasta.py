#!/usr/bin/env python
# coding: utf-8

# In[11]:



from Bio import SeqIO

def ReverseFasta(fastafile):
    order=0
    filenamefull=fastafile.split('.')
    filename=filenamefull[0]
    reversefile= filename + '_reverse_abridged.fasta'
    proteinsequences = SeqIO.parse(open(fastafile),'fasta')
    with open(reversefile, 'w') as reversef:
        for protein in proteinsequences:
            order=order+1
            strorder=str(order).zfill(6)
            name, sequence = protein.id, str(protein.seq)
            protein.id= 'REV_' + strorder + ' reversed'
            protein.seq=protein.seq[::-1]
            protein.description=''
            fastareverse=SeqIO.write(protein, reversef, 'fasta')



# In[12]:


fasta='dummy.fasta'
ReverseFasta(fasta)


# In[ ]:




