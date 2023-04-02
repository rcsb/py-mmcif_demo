# =============================================================================
# Author:  Chenghua Shao
# Date:    2023-02-17
# Updates:
# =============================================================================
"""
mmmcif parser demo CCD parsing
"""

from mmcif.io.IoAdapterCore import IoAdapterCore
from downloadFile import downloadFile


class CCD:
    """Class to process CCD file
    """

    def __init__(self):
        self.io = IoAdapterCore()

    def read(self, filepath_in):
        self.l_dc = self.io.readFile(filepath_in)
        self.dc0 = self.l_dc[0]
    
    def getDescriptor(self):
        descriptor = self.dc0.getObj('pdbx_chem_comp_descriptor')
        n_rows = descriptor.getRowCount()
        for i in range(n_rows):
            d_row = descriptor.getRowAttributeDict(i)
            l_row = [d_row["type"], d_row["descriptor"]]
            print(": ".join(l_row))    


def main():
    filepath = downloadFile("ATP", file_type="ccd-definition")
    ccd = CCD()
    ccd.read(filepath)
    ccd.getDescriptor()


if __name__ == "__main__":
    main()
