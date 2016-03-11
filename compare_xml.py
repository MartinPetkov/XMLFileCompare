# Compares two XML files and returns true if they have the same elements with the same data and attributes, but not
# necessarily in the same order

import sys
import xml.etree.ElementTree as ET
import xmltodict
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
  # Parse files
  xmlstr1 = open(xmlfile1, 'r').read()
  xmlstr2 = open(xmlfile2, 'r').read()

  # Turn the strings into dicts
  xmldict1 = json.loads(json.dumps(xmltodict.parse(xmlstr1, process_namespaces=True)))
  xmldict2 = json.loads(json.dumps(xmltodict.parse(xmlstr2, process_namespaces=True)))

  # Sort the dictionaries for comparison
  xmldict1 = sort_dict(xmldict1)
  xmldict2 = sort_dict(xmldict2)

  # Compare the two dictionaries
  return(xmldict1 == xmldict2)


if __name__ == "__main__":
  print(compare_xml_files(sys.argv[1], sys.argv[2]))
