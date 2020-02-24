"""
Author: Peter Elliott       Created:    19/02/2020

            Task
Taking the following XML document
write code to extract the RefText values
for the following RefCodes: ‘MWB’, ‘TRV’ and ‘CAR’

    Notes to self
1. read in xml file
2. Select the value needed from file
3. find and get RefText values from list
"""
import xml.etree.ElementTree as elTree


def getTags(node, tags_list, found):  # Recursive function check every child node in tree
    for child in node:  # loop through child of current node
        if child.get('RefCode') in tags_list:  # if current node refcodes is present check each child an
            for Details in child:  # refCode found now check each child in this node for refText
                if Details.tag == "RefText":
                    found.append({"Code": child.get('RefCode'), "Text": Details.text})  # The RefCode and RefText are stored in a dictionary which is then placed in a list
        else:
            getTags(child, refTags, found)  # if no refCode check child nodes in tree
    return found

XMLDATA = elTree.parse('Exercise2.xml')  # Xml is parsed in as tree each set of tag becomes a node and inner tags are child nodes
root = XMLDATA.getroot() # starts at most outer set of tags
refTags = ["MWB", "TRV", "CAR"]  # RefCodes being searched

found_tags = getTags(root, refTags, [])  # the empty array is to add the found codes and text into later

print(len(found_tags), " items where found")  # number of tags found
if len(found_tags) > 0:  # if tags were found display them
    for entry in found_tags:  # printed out for easy reading
        print("Reference code : ", entry["Code"], " and Text :", entry["Text"])
        # the above code takes out the refCode and refText displaying both in an easy to read format

input('Press enter to continue')
