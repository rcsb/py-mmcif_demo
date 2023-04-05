# py-mmcif_demo
Demo using mmcif parser to parse PDBx/mmCIF-format files in the Protein Data Bank

Demo code works under python3 only
Before running the demo, plese install 'mmcif' package with pip install or from https://github.com/rcsb/py-mmcif

1. parseSimple.py demonstrates the simplest coding for using mmcif parser with step-by-step explanation 
2. downloadFile.py is a utility to download mmCIF-format file for coordinates, ligand definition, and validation report files
3. parseLigandOfInterestSimple.py demos cross-category mapping to find Ligand Of Interest (LOI) within a coordinates file
4. parsePdbx.py constructs a class for parsing coordinates file
5. parseCcd.py constructs a class for parsing ligand definition file
6. parseVal.py constructs a class for parsing validation file
7. checkLOI.py uses the above classes to do cross-file parsing and mapping to find information for LOI
8. sortBySource.py demos parsing source of polymer from coordinates file, and find the human proteins
