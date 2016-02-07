import xml.etree.cElementTree as ET

#Let's set the file in and out and open the stream for writing
INFILENAME = "reykjavik_iceland.osm"
OUTFILENAME= "reykjavik_iceland.json"
f = open(OUTFILENAME, 'w')

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
				if 'addr:postcode' in child.attrib['k']:
					if int(child.attrib['v']) > 902:
						print child
				newKey = child.attrib['k'][5:]
				node['address'][newKey] = child.attrib['v']
			else:
				node[child.attrib['k']] = child.attrib['v']
		#nd elements are handled different then tag elements, just add all the references to an array
		if child.tag == 'nd':
			node['node_refs'] = child.attrib['ref']
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
	
#iterate through the xml document listed at the top of this file
for _, element in ET.iterparse(INFILENAME):
	if element.tag == "node":
		clean_up_node(element)
	if element.tag == "way":
		clean_up_way(element)