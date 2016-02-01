import xml.etree.cElementTree as ET
import re
import codecs
import json
import copy

INFILENAME = "reykjavik_iceland.osm"
OUTFILENAME= "reykjavik_iceland.json"

f = open(OUTFILENAME, 'w')
count = 0

def write_to_out(elem):
	return 0

def clean_up_way(elem):
	return 0

def clean_up_node(elem):
	node = {}
	node['pos'] = []
	node['created'] = {}
	for key in elem.attrib.keys():
		if key == "lat" or key == "lon":
			node['pos'].append(elem.attrib[key])
		if key == "changeset" or key == "version" or key == "user" or key == "uid" or key == "timestamp":
			node['created'][key] = elem.attrib[key]
		node[key] = elem.attrib[key]
	print node
	


for _, element in ET.iterparse(INFILENAME):
	if element.tag == "node":
		clean_up_node(element)
	if element.tag == "way":
		clean_up_way(element)