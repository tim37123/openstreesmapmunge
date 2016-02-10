# -*- coding: UTF-8 -*-
import xml.etree.cElementTree as ET

#Let's set the file in and out and open the stream for writing
INFILENAME = "reykjavik_iceland.osm"
OUTFILENAME= "reykjavik_iceland.json"
f = open(OUTFILENAME, 'w')

#Enormous postal code dictionary
postalCodeDict = {  '101':'Reykjavík (Miðborg)',
					'102':'Reykjavík international mail sorting station',
					'103':'Reykjavík (Háaleiti og Bústaðir)',
					'104':'Reykjavík (Laugardalur)',
					'105':'Reykjavík (Hlíðar)',
					'107':'Reykjavík (Vesturbær)',
					'108':'Reykjavík (Háaleiti og Bústaðir)',
					'109':'Reykjavík (Breiðholt)',
					'110':'Reykjavík (Árbær)',
					'111':'Reykjavík (Breiðholt)',
					'112':'Reykjavík (Grafarvogur)',
					'113':'Reykjavík (Grafarholt og Úlfarsárdalur)',
					'116':'Reykjavík (Kjalarnes)',
					'121':'Reykjavík PO boxes',
					'123':'Reykjavík PO boxes',
					'124':'Reykjavík PO boxes',
					'125':'Reykjavík PO boxes',
					'127':'Reykjavík PO boxes',
					'128':'Reykjavík PO boxes',
					'129':'Reykjavík PO boxes',
					'130':'Reykjavík PO boxes',
					'132':'Reykjavík PO boxes',
					'150':'Reykjavík',
					'155':'Reykjavík',
					'170':'Seltjarnarnes',
					'172':'Seltjarnarnes PO boxes',
					'190':'Vogar',
					'200':'Kópavogur',
					'201':'Kópavogur',
					'202':'Kópavogur PO boxes',
					'203':'Kópavogur',
					'210':'Garðabær',
					'212':'Garðabær PO boxes',
					'220':'Hafnarfjörður',
					'221':'Hafnarfjörður',
					'222':'Hafnarfjörður PO boxes',
					'225':'Álftanes',
					'230':'Reykjanesbær',
					'232':'Reykjanesbær PO boxes',
					'233':'Reykjanesbær',
					'235':'Reykjanesbær',
					'240':'Grindavík',
					'245':'Sandgerði',
					'250':'Garður',
					'260':'Reykjanesbær',
					'270':'Mosfellsbær',
					'271':'Mosfellsbær',
					'276':'Mosfellsbær',
					'300':'Akranes',
					'301':'Akranes',
					'302':'Akranes PO boxes',
					'310':'Borgarnes',
					'311':'Borgarnes',
					'320':'Reykholt',
					'340':'Stykkishólmur',
					'345':'Flatey',
					'350':'Grundarfjörður',
					'355':'Ólafsvík',
					'356':'Snæfellsbær',
					'360':'Hellissandur',
					'370':'Búðardalur',
					'371':'Búðardalur',
					'380':'Reykhólahreppur',
					'400':'Ísafjörður',
					'401':'Ísafjörður',
					'410':'Hnífsdalur',
					'415':'Bolungarvík',
					'420':'Súðavík',
					'425':'Flateyri',
					'430':'Suðureyri',
					'450':'Patreksfjörður',
					'451':'Patreksfjörður',
					'460':'Tálknafjörður',
					'465':'Bíldudalur',
					'470':'Þingeyri',
					'471':'Þingeyri',
					'500':'Staður',
					'510':'Hólmavík',
					'512':'Hólmavík',
					'520':'Drangsnes',
					'524':'Árneshreppur',
					'530':'Hvammstangi',
					'531':'Hvammstangi',
					'540':'Blönduós',
					'541':'Blönduós',
					'545':'Skagaströnd',
					'550':'Sauðárkrókur',
					'551':'Sauðárkrókur',
					'560':'Varmahlíð',
					'565':'Hofsós',
					'566':'Hofsós',
					'570':'Fljót',
					'580':'Siglufjörður',
					'600':'Akureyri',
					'601':'Akureyri',
					'602':'Akureyri PO boxes',
					'603':'Akureyri',
					'610':'Grenivík',
					'611':'Grímsey',
					'620':'Dalvík',
					'621':'Dalvík',
					'625':'Ólafsfjörður',
					'630':'Hrísey',
					'640':'Húsavík',
					'641':'Húsavík',
					'645':'Fosshóll',
					'650':'Laugar',
					'660':'Mývatn',
					'670':'Kópasker',
					'671':'Kópaskeri',
					'675':'Raufarhöfn',
					'680':'Þórshöfn',
					'681':'Þórshöfn',
					'685':'Bakkafjörður',
					'690':'Vopnafjörður',
					'700':'Egilsstaðir',
					'701':'Egilsstaðir',
					'710':'Seyðisfjörður',
					'715':'Mjóifjörður',
					'720':'Borgarfjörður eystri',
					'730':'Reyðarfjörður',
					'735':'Eskifjörður',
					'740':'Neskaupstaður',
					'750':'Fáskrúðsfjörður',
					'755':'Stöðvarfjörður',
					'760':'Breiðdalsvík',
					'765':'Djúpivogur',
					'780':'Höfn',
					'781':'Höfn',
					'785':'Öræfi',
					'800':'Selfoss',
					'801':'Selfoss',
					'802':'Selfoss PO boxes',
					'810':'Hveragerði',
					'815':'Þorlákshöfn',
					'816':'Ölfus',
					'820':'Eyrarbakki',
					'825':'Stokkseyri',
					'840':'Laugarvatn',
					'845':'Flúðir',
					'850':'Hella',
					'851':'Hella',
					'860':'Hvolsvöllur',
					'861':'Hvolsvöllur',
					'870':'Vík',
					'871':'Vík',
					'880':'Kirkjubæjarklaustur',
					'900':'Vestmannaeyjar',
					'902':'Vestmannaeyjar PO boxes'
					};


#After the element types we care about have been written to JSON this funtion writes it to the out stream
def write(elem):
	elem = str(elem)+"\n"
	elem = elem.decode("utf-8").encode('iso-8859-1')
	f.write(elem)
	return True

#Take any way tags and convert them into JSON
def clean_up_way(elem):
	#some of the inital backbone of the dictionary need to be created before iterating
	node = {}
	node['node_refs'] = []
	node['created'] = {}
	node['address'] = {}

	#This takes any key tags that are children of way and strips out metadata we care about
	for key in elem.attrib.keys():
		if key == "changeset" or key == "user" or key == "uid" or key == "timestamp" or key == "version":
			node['created'][key] = elem.attrib[key]
		else:
			node[key] = elem.attrib[key]

	#This takes any elem tags that are children of way and reorganizes the data we care about
	for child in elem:
		if child.tag == 'tag':
			#'addr' info needs to be handled differently so add an if statement, then everything else just gets its own key value pair
			if 'addr:' in child.attrib['k']:
				newKey = child.attrib['k'][5:]
				node['address'][newKey] = child.attrib['v']
			else:
				node[child.attrib['k']] = child.attrib['v']
		#nd elements are handled different then tag elements, just add all the references to an array
		if child.tag == 'nd':
			node['node_refs'] = child.attrib['ref']

	#if we have postal code data for this node, lookup the associated region in our big dictionary above and create a new bit of data
	if 'postal_code' in node:
		node['postal_code_region'] = lookupRegion(node['postal_code'])

	return node

#This takes all the node elements and cleans it into a JSON model
def clean_up_node(elem):
	#some of the inital backbone of the dictionary need to be created before iterating
	node = {}
	node['pos'] = []
	node['created'] = {}

	#This takes each key on the tag and transforms it into the JSON model
	for key in elem.attrib.keys():
		#lat and lon keys go into a special pos array
		if key == "lat" or key == "lon":
			node['pos'].append(elem.attrib[key])
		#these keys go into a special created dict
		elif key == "changeset" or key == "version" or key == "user" or key == "uid" or key == "timestamp":
			node['created'][key] = elem.attrib[key]
		#everything else gets its own key/value
		else:
			node[key] = elem.attrib[key]
	return node

#To help alleviate missing address data I look up region by postal code and embed in teh json
def lookupRegion(code):
	return postalCodeDict[code]
	
#iterate through the xml document listed at the top of this file
for _, element in ET.iterparse(INFILENAME):
	if element.tag == "node":
		write(clean_up_node(element))
	if element.tag == "way":
		write(clean_up_way(element))