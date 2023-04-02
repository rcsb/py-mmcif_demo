#!/usr/bin/env python3
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

filepath = downloadFile("7r2y", file_type="pdb-validation")
io = IoAdapterCore()
list_data_container = io.readFile(filepath)
# read file, generate list of data containers

data_container = list_data_container[0]
# select the 1st data container

summary = data_container.getObj('pdbx_vrpt_summary_geometry')
# obtain data category from data container

d_row = summary.getRowAttributeDict(0)
print("percent_ramachandran_outliers: %s%%" %
      d_row["percent_ramachandran_outliers"])
print("percent_rotamer_outliers: %s%%" %
      d_row["percent_rotamer_outliers"])
print("clashscore: %s" % d_row["clashscore"])
