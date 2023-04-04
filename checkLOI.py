# =============================================================================
# Author:  Chenghua Shao
# Date:    2023-02-17
# Updates:
# =============================================================================
"""
mmmcif parser demo parsing Ligand Of Interest (LOI) from PDB entry 7TRT.
Next, parse the SMILES/InCHI descriptors from the ligand definition file for the LOI.
Finally, parse the geometry and density fitting validation statistics of the ligand
from wwPDB validation report. 
"""
from mmcif.io.IoAdapterCore import IoAdapterCore
from downloadFile import downloadFile
from parsePdbx import Pdbx
from parseCcd import Ccd
from parseVal import Val


def main():
    pdb_id = "7TRT"
    pdbx = Pdbx()
    filepath_pdbx = downloadFile(pdb_id)  # download file
    pdbx.read(filepath_pdbx)
    l_loi_id = pdbx.findLoi()
    print(l_loi_id)
    l_loi_coord = pdbx.getCoordinatesByCcdId(l_loi_id)
    for l_row in l_loi_coord:
        print('\t'.join(l_row))

    ccd = Ccd()
    for ccd_id in l_loi_id:
        filepath_ccd = downloadFile(ccd_id, file_type="ccd-definition")
        ccd.read(filepath_ccd)
        l_descriptor = ccd.getDescriptor()
        for l_row in l_descriptor:
            print(": ".join(l_row))

    val = Val()
    filepath_val = downloadFile(pdb_id, file_type="pdb-validation")
    val.read(filepath_val)
    for ccd_id in l_loi_id:
        val.parseLigand(ccd_id)
        print(val.d_lig_instance)
        print(val.d_lig_geo)
        print(val.d_lig_fit)


if __name__ == "__main__":
    main()
