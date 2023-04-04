# =============================================================================
# Author:  Chenghua Shao
# Date:    2023-02-17
# Updates:
# =============================================================================
"""
mmmcif parser demo validation report parsing
"""

from mmcif.io.IoAdapterCore import IoAdapterCore
from downloadFile import downloadFile


class Val:
    def __init__(self):
        self.io = IoAdapterCore()

    def read(self, filepath_in):
        self.l_dc = self.io.readFile(filepath_in)
        self.dc0 = self.l_dc[0]

    def parseGeometrySummary(self):
        summary = self.dc0.getObj('pdbx_vrpt_summary_geometry')
        return summary.getRowAttributeDict(0)

    def parseLigand(self, ccd_id):
        self.d_lig_instance = {}
        model_instance = self.dc0.getObj("pdbx_vrpt_model_instance")
        l_index = model_instance.selectIndices(ccd_id, "label_comp_id") 
        for i in l_index:
            d_row = model_instance.getRowAttributeDict(i)
            instance_id = d_row["id"]
            self.d_lig_instance[instance_id] = [d_row["auth_asym_id"], d_row["auth_seq_id"]]
        l_lig_instance = list(self.d_lig_instance.keys())
        
        geometry = self.dc0.getObj("pdbx_vrpt_model_instance_geometry")
        self.d_lig_geo = {}
        for instance_id in l_lig_instance:
            index_geo = geometry.selectIndices(instance_id, "instance_id")[0]
            d_row = geometry.getRowAttributeDict(index_geo)
            self.d_lig_geo[instance_id] = {}
            self.d_lig_geo[instance_id]["bonds_RMSZ"] = d_row["bonds_RMSZ"]
            self.d_lig_geo[instance_id]["angles_RMSZ"] = d_row["angles_RMSZ"]

        fit = self.dc0.getObj("pdbx_vrpt_model_instance_density")
        self.d_lig_fit = {}
        for instance_id in l_lig_instance:
            index_fit = fit.selectIndices(instance_id, "instance_id")[0]
            d_row = fit.getRowAttributeDict(index_fit)
            self.d_lig_fit[instance_id] = {}
            self.d_lig_fit[instance_id]["RSCC"] = d_row["RSRCC"]
            self.d_lig_fit[instance_id]["RSR"] = d_row["RSR"]


def main():
    filepath = downloadFile("7trt", file_type="pdb-validation")
    val = Val()
    val.read(filepath)

    d_summary = val.parseGeometrySummary()
    print("percent_ramachandran_outliers: %s%%" %
          d_summary["percent_ramachandran_outliers"])
    print("percent_rotamer_outliers: %s%%" % 
          d_summary["percent_rotamer_outliers"])
    print("clashscore: %s" % d_summary["clashscore"])

    val.parseLigand("KQF")
    print(val.d_lig_instance)
    print(val.d_lig_geo)
    print(val.d_lig_fit)


if __name__ == "__main__":
    main()
