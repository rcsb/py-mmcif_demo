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


class Pdbx:
    def __init__(self):
        self.io = IoAdapterCore()

    def read(self, filepath_in):
        self.l_dc = self.io.readFile(filepath_in)
        self.dc0 = self.l_dc[0]

    def findLoi(self):
        l_loi_id = []
        loi = self.dc0.getObj("pdbx_entity_instance_feature")
        l_index_loi = loi.selectIndices(
            "SUBJECT OF INVESTIGATION", "feature_type")
        for i in l_index_loi:
            ccd_id = loi.getValue("comp_id", i)
            if ccd_id not in l_loi_id:
                l_loi_id.append(ccd_id)
        return l_loi_id

    def getCoordinatesByCcdId(self, l_loi_id):
        if not l_loi_id:
            return None
        coordinates = self.dc0.getObj('atom_site')
        l_index = []
        for ccd_id in l_loi_id:
            l_index.extend(coordinates.selectIndices(ccd_id, "auth_comp_id"))
        l_loi_coord = []
        for i in l_index:
            d_row = coordinates.getRowAttributeDict(i)
            l_row = [d_row["auth_comp_id"], d_row["auth_asym_id"], d_row["auth_seq_id"], d_row["auth_atom_id"],
                     d_row["Cartn_x"], d_row["Cartn_y"], d_row["Cartn_z"]]
            l_loi_coord.append(l_row)
        return l_loi_coord


def main():
    filepath = downloadFile("7TRT")  # download file
    pdbx = Pdbx()
    pdbx.read(filepath)
    l_loi_id = pdbx.findLoi()
    print(l_loi_id)
    l_loi_coord = pdbx.getCoordinatesByCcdId(l_loi_id)
    for l_row in l_loi_coord:
        print('\t'.join(l_row))


if __name__ == "__main__":
    main()
