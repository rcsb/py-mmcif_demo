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


class Ccd:
    """ class to parse CCD chemical definition file
    """

    def __init__(self):
        """ initialize the mmcif parser io
        """
        self.io = IoAdapterCore()

    def read(self, filepath_in):
        """ read the file contents into data containers

        Args:
            filepath_in (str): file path of coordinates file
        """
        self.l_dc = self.io.readFile(filepath_in)  #read into data containers
        self.dc0 = self.l_dc[0]  #choose the 1st data container
    
    def getDescriptor(self):
        """ get chemical descriptor of various types

        Returns:
            list : list of descriptors
        """
        descriptor = self.dc0.getObj('pdbx_chem_comp_descriptor')
        n_rows = descriptor.getRowCount()
        l_descriptor = []
        for i in range(n_rows):
            d_row = descriptor.getRowAttributeDict(i)
            l_row = [d_row["type"], d_row["descriptor"]]
            l_descriptor.append(l_row)
        return l_descriptor  


def main():
    filepath = downloadFile("ATP", file_type="ccd-definition")
    ccd = Ccd()
    ccd.read(filepath)
    l_descriptor = ccd.getDescriptor()
    for l_row in l_descriptor:
        print(": ".join(l_row))   


if __name__ == "__main__":
    main()
