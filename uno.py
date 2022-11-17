import xml.etree.ElementTree as ET

from flask import Flask

import deck as cards

app = Flask(__name__)

# Opens "cards.xml" and parses data to generate cards and puts them in an array named deck
tree = ET.parse('cards.xml')
root = tree.getroot()
deck = []

for i in root:
	if i.tag == 'color':
		prefix = i.attrib['id']
		for j in i:
			if j.tag == 'card':
				deck += [cards.Card(prefix, j.attrib['id'])]
			if j.tag == 'ccard':
				deck += [cards.CCard(prefix, j.attrib['id'], j.attrib['ssc'].strip(), j.attrib['csc'].strip(), j.text.strip())]
			if j.tag == 'scard':
				deck += [cards.SCard(prefix, j.attrib['id'], None, j.attrib.get('draw', 0), j.attrib.get('skamt', 0), j.attrib.get('iswild', False))]

if __name__ == '__main__':
	# inits game with player array and deck array
	# TODO make working multiplayer
	f = cards.UNO(['a', 'b'], deck)

	while len(f.douac['a']) > 0 and len(f.douac['b']) > 0:
		print(f.ccard, f.douac['a'])
		play = int(input('a: please slect cardddd'))
		f.round('a', play)
		print(f.ccard, f.douac['b'])
		play = int(input('b: please slect cardddd'))
		f.round('b', play)