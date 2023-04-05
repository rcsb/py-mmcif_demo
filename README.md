# py-mmcif_demo
Demo using mmcif parser to parse PDBx/mmCIF-format files in the Protein Data Bank

Before running the demo, plese install 'mmcif' package with pip install or from https://github.com/rcsb/py-mmcif

1. parseSimple.py simplest code for using mmcif parser
2. downloadFile.py a utility to download mmCIF-format file for coordinates, ligand definition, and validation report
3. parseLigandOfInterestSimple.py demo cross-category mapping to find Ligand Of Interest (LOI) within a coordinates file
4. parsePdbx.py construct a class for parsing coordinates file
5. parseCcd.py construct a class for parsing ligand definition file
6. parseVal.py construct a class for parsing validation file
7. checkLOI.py use the above classes to do cross-file parsing and mapping to find information for LOI
8. sortBySource.py demo parsing source of polymer from coordinates file, and find the human proteins
