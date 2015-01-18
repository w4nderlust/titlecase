#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from os import listdir, walk
from os.path import isfile, join
import ntpath

english_small = {"is", "am", "are", "have", "has", "the", "my", "your", "his", "her", "its", "our", "their", "whose", "this", "that", "these", "those", "which", "a", "an", "any", "another", "other", "what", "a", "abaft", "abeam", "aboard", "about", "above", "absent", "across", "afore", "after", "against", "along", "alongside", "amid", "amidst", "among", "amongst", "an", "anenst", "apropos", "apud", "around", "as", "aside", "astride", "at", "athwart", "atop", "barring", "before", "behind", "below", "beneath", "beside", "besides", "between", "beyond", "but", "by", "chez", "circa", "concerning", "despite", "down", "during", "except", "excluding", "failing", "following", "for", "forenenst", "from", "given", "in", "including", "inside", "into", "like", "mid", "midst", "minus", "modulo", "near", "next", "notwithstanding", "o'", "of", "off", "on", "onto", "opposite", "out", "outside", "over", "pace", "past", "per", "plus", "pro", "qua", "regarding", "round", "sans", "save", "since", "than", "through", "thru", "throughout", "thruout", "till", "times", "to", "toward", "towards", "under", "underneath", "unlike", "until", "unto", "up", "upon", "versus", "vs", "via", "vice", "vis-à-vis", "worth", "s", "and", "but", "or", "yet", "for", "nor", "so", "after", "although", "as", "because", "before", "even", "if", "once", "rather", "since", "so", "than", "that", "than", "though", "till", "unless", "until", "when", "whenever", "where", "whereas", "wherever", "while"}
italian_small = {"è", "ha", "ho", "hai", "hanno", "abbiamo", "avete", "e", "ed", "né", "o", "oppure" "inoltre", "ma", "però", "dunque", "anzi", "che", "allorché", "perché", "giacché", "purché", "affinché", "eppure", "oppure", "dopoché", "anche", "neanche", "neppure", "ovvero", "ossia", "oppure", "però", "tuttavia", "anzi", "nfatti", "cioè", "ossia", "dunque", "quindi", "perciò", "che", "come", "quando", "mentre", "finché", "siccome", "sebbene", "quantunque", "se", "qualora", "fuorché", "il", "lo", "la", "l", "i", "gli", "le", "un", "uno", "una", "di", "a", "da", "in", "con", "su", "per", "tra", "fra", "del", "dello", "della", "dei", "degli", "delle", "al", "allo", "alla", "ai", "agli", "alle", "dal", "dallo", "dalla", "dai", "dagli", "dalle", "nel", "nello", "nella", "nei", "negli", "nelle", "col", "coi", "sul", "sullo", "sulla", "sui", "sugli", "sulle"}

if len(sys.argv) < 2:
    sys.exit('Usage: %s <directory_path>' % sys.argv[0])

if not os.path.exists(sys.argv[1]):
    sys.exit('ERROR: Directory %s was not found!' % sys.argv[1])

file_list = []

for root, subFolders, files in walk(sys.argv[1]):
    for f in files:
    	if not f[0] == ".":
        	file_list.append(os.path.join(root, f))

for file_path in file_list:
	base, filename = ntpath.split(file_path)
	filename_dot = filename.split(".")
	words = filename_dot[0].lower().split()
	
	for i, word in enumerate(words):

		if len(word) > 1 and not (word in english_small or word in italian_small):
			words[i] = word[0].upper() + word[1:]
		
		if "'" in word:
			sub_words = word.split("'")
			for j, sub_word in enumerate(sub_words):
				if len(sub_word) > 1 and not (sub_word in english_small or sub_word in italian_small):
					sub_words[j] = sub_word[0].upper() + sub_word[1:]
			words[i] = "'".join(sub_words)

	words[0] = words[0][0].upper() + words[0][1:]

	for i, word in enumerate(words):
		if 1 > 0:
			if words[i - 1] == "-":
				words[i] = words[i][0].upper() + words[i][1:]

	new_filename = " ".join(words)
	for ext in filename_dot[1:]:
		new_filename = new_filename + "." + ext

	print "[" + base + "] " + filename + " -> " + new_filename

	os.rename(join(base, filename), join(base, new_filename))
