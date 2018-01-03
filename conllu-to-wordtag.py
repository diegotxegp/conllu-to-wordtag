#!/usr/bin/env python
'''
Converter from .conllu format to [word]_[tag] format for tagger

@author: diego.garciap
Created on 19/12/2017


Command line:

python conllu-to-wordtag.py
'''

import os
from os import walk

#
for (path, folders, files) in walk("."):

    if len(files)>=9:
        for fil in files:

            if fil.endswith(".conllu"):

                directory = "./wordtag-path/"+fil.rsplit('-',2)[0]+'/'
                if not os.path.exists(directory):
                    os.makedirs(directory)

                #
                with open(str(path+'/'+fil),'r') as conllu, open(str(directory+fil[0:-7]+"-wordtag.txt"),'w') as word_tag:

                    lines=conllu.readlines()
                    sentence = ""

                    for line in lines:
                        tupl = line.split()

                        if len(tupl)!=0 and tupl[0]!='#' and '.' not in tupl[0] and '-' not in tupl[0]:
                            sentence = sentence+tupl[1]+'_'+tupl[3]+" "
                        if len(tupl)==0:
                            word_tag.write(sentence+"\n")
                            sentence = ""

                    print str(fil[0:-7]+"-wordtag.txt created at "+directory)
