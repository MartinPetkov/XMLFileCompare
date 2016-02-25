# Compares two XML files and returns true if they have the same elements with the same data and attributes, but not
# necessarily in the same order

import sys
import xml.etree.ElementTree as ET
import xmltodict
from pprint import pprint
import json

# Makes sure all lists in the dictionary are sorted, at all levels of depth
def sort_dict(d):
  for k, v in d.items():
    if isinstance(v, dict):
      d[k] = sort_dict(v)
    elif isinstance(v, list):
      for i in range(len(v)):
        if isinstance(v[i], dict):
          v[i] = sort_dict(v[i])

      d[k] = sorted(v)

  return d


def compare_xml_files(xmlfile1, xmlfile2):
  # Parse file into ElementTree objects
  xmltree1 = ET.parse(xmlfile1)
  xmltree2 = ET.parse(xmlfile2)

  # Turn ElementTree objects into OrderedDicts (OrderedDicts are a bad output type, but this is the best library I found)
  xmldict1 = xmltodict.parse(ET.tostring(xmltree1.getroot()), process_namespaces=True)
  xmldict2 = xmltodict.parse(ET.tostring(xmltree2.getroot()), process_namespaces=True)

  # Turn the OrderedDicts into regular dicts and sort them for comparison
  xmldict1 = sort_dict(dict(json.loads(json.dumps(xmldict1))))
  xmldict2 = sort_dict(dict(json.loads(json.dumps(xmldict2))))

  # Compare the two dictionaries
  return(xmldict1 == xmldict2)
