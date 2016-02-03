import xml.etree.cElementTree as ET
import re
import codecs
import json
import copy

INFILENAME = "reykjavik_iceland.osm"
OUTFILENAME= "reykjavik_iceland.json"

f = open(OUTFILENAME, 'w')
count = 0

def write(elem):
	elem = str(elem)+"\n"
	f.write(elem)
	return True

def clean_up_way(elem):
	node = {}
	node['node_refs'] = []
	node['created'] = {}
	node['address'] = {}
	for key in elem.attrib.keys():
		if key == "changeset" or key == "user" or key == "uid" or key == "timestamp" or key == "version":
			node['created'][key] = elem.attrib[key]
		else:
			node[key] = elem.attrib[key]
	for child in elem:
		if child.tag == 'tag':
			if 'addr:' in child.attrib['k']:
				newKey = child.attrib['k'][5:]
				node['address'][newKey] = child.attrib['v']
			else:
				node[child.attrib['k']] = child.attrib['v']
		if child.tag == 'nd':
			node['node_refs'] = child.attrib['ref']
	return node

def clean_up_node(elem):
	node = {}
	node['pos'] = []
	node['created'] = {}
	for key in elem.attrib.keys():
		if key == "lat" or key == "lon":
			node['pos'].append(elem.attrib[key])
		elif key == "changeset" or key == "version" or key == "user" or key == "uid" or key == "timestamp":
			node['created'][key] = elem.attrib[key]
		else:
			node[key] = elem.attrib[key]
	return node
	

for _, element in ET.iterparse(INFILENAME):
	if element.tag == "node":
		write(clean_up_node(element))
	if element.tag == "way":
		write(clean_up_way(element))