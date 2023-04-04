# =============================================================================
# Author:  Chenghua Shao
# Date:    2023-02-17
# Updates:
# =============================================================================
"""
mmmcif parser demo parsing Ligand Of Interest (LOI) from PDB entry 7TRT
"""
from mmcif.io.IoAdapterCore import IoAdapterCore
from downloadFile import downloadFile

filepath = downloadFile("7TRT")  #download file

io = IoAdapterCore()
list_data_container = io.readFile(filepath)
# read file, generate list of data containers

data_container = list_data_container[0]
# select the 1st data container

loi = data_container.getObj("pdbx_entity_instance_feature")
# select the LOI category from data container

l_index_loi = loi.selectIndices("SUBJECT OF INVESTIGATION","feature_type") 
# get list of indices by value/attribute pair, i.e. LOI

ccd_id_1 = loi.getValue("comp_id", l_index_loi[0])
print(ccd_id_1)
# get LOI ligand CCD ID

nonpoly = data_container.getObj("pdbx_entity_nonpoly")
# select the nonpoly category from data container

l_index_nonpoly = nonpoly.selectIndices(ccd_id_1, "comp_id")
# get list of indices by value/attribute pair, i.e. LOI CCD ID

print(nonpoly.getValue("name", l_index_nonpoly[0]))
# get LOI ligand name

coordinates = data_container.getObj('atom_site')
# obtain data category from data container

l_index = coordinates.selectIndices(ccd_id_1, "auth_comp_id")
for i in l_index:
    d_row = coordinates.getRowAttributeDict(i)
    l_value = [d_row["auth_comp_id"], d_row["auth_asym_id"], 
               d_row["auth_seq_id"], d_row["Cartn_x"], 
               d_row["Cartn_y"], d_row["Cartn_z"]]
    print('\t'.join(l_value))
