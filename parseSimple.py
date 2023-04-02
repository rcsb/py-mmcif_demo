# =============================================================================
# Author:  Chenghua Shao
# Date:    2023-02-17
# Updates:
# =============================================================================
"""
mmmcif parser demo simplest example on PDB entry 2HYV
"""
import os
import urllib.request
from mmcif.io.IoAdapterCore import IoAdapterCore
# File IO class, read and write mmcif file

url_2hyv = "https://files.rcsb.org/download/2HYV.cif"
filepath_local = os.path.join("/tmp", "2hyv.cif")
urllib.request.urlretrieve(url_2hyv, filepath_local)
# download file

io = IoAdapterCore()
list_data_container = io.readFile(filepath_local)
# read file, generate list of data containers

data_container = list_data_container[0]
# select the 1st data container

entity = data_container.getObj('entity')
# select the entity category from data container

print(entity.data)
# review all data in entity as a list of rows
print("----------")
for each_data in entity.data:
    print(each_data)  # review each row separately
print("----------")

print(entity.getRowAttributeDict(0))
# review 1st row as a dictionary with attr/value pair
print("----------")
for attr, value in entity.getRowAttributeDict(0).items():
    print((attr, value))  # review each attr/value pair
print("----------")

print(entity.getValue("pdbx_description", 0))
# review value of an attr by index, 0 means first value

# parse sequence from entity_poly category
entity_poly = data_container.getObj('entity_poly')
print(entity_poly.getValue("pdbx_strand_id", 0))
print(entity_poly.getValue("pdbx_seq_one_letter_code", 0))
print("----------")

# parse refinement statistics
refine = data_container.getObj('refine')
d_refine = refine.getRowAttributeDict(0)
l_attr = ["ls_d_res_high",
          "ls_R_factor_R_work",
          "ls_R_factor_R_free",
          "pdbx_method_to_determine_struct"]
for attr in l_attr:
    print("%s: %s" % (attr, d_refine[attr]))
