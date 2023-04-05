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


def getSource(pdb_id):
    """_summary_

    Args:
        pdb_id (str): pdb id

    Returns:
        dict: dictionary of the polymers and their sources
    """
    filepath = downloadFile(pdb_id)
    io = IoAdapterCore()
    l_dc = io.readFile(filepath)
    dc0 = l_dc[0]

    d_polymer = {}

    entity = dc0.getObj("entity")
    for i in range(entity.getRowCount()):
        d_row_ent = entity.getRowAttributeDict(i)
        if d_row_ent["type"] == "polymer":  #check macromolecule polymer only
            d_polymer[d_row_ent["id"]] = {}
            d_polymer[d_row_ent["id"]]["source_method"] = d_row_ent["src_method"]  #get source method
            d_polymer[d_row_ent["id"]]["name"] = d_row_ent["pdbx_description"]  #get molecule name

    for id in d_polymer:
        d_polymer[id]["source"] = []

        # the source info is stored in different category based on source method
        if d_polymer[id]["source_method"] == "man":  #for genetically manipulated
            src = dc0.getObj("entity_src_gen")
            for j in range(src.getRowCount()):
                d_row_src = src.getRowAttributeDict(j)
                if d_row_src["entity_id"] == id:
                    source = d_row_src["pdbx_gene_src_scientific_name"].lower()
                    if source not in d_polymer[id]["source"]:
                        d_polymer[id]["source"].append(source)
        if d_polymer[id]["source_method"] == "nat":  #for naturally obtained
            src = dc0.getObj("entity_src_nat")
            for j in range(src.getRowCount()):
                d_row_src = src.getRowAttributeDict(j)
                if d_row_src["entity_id"] == id:
                    source = d_row_src["pdbx_organism_scientific"].lower()
                    if source not in d_polymer[id]["source"]:
                        d_polymer[id]["source"].append(source)
        if d_polymer[id]["source_method"] == "syn":  #for synthetic molecule
            src = dc0.getObj("pdbx_entity_src_syn")
            for j in range(src.getRowCount()):
                d_row_src = src.getRowAttributeDict(j)
                if d_row_src["entity_id"] == id:
                    source = d_row_src["organism_scientific"].lower()
                    if source not in d_polymer[id]["source"]:
                        d_polymer[id]["source"].append(source)
        else:
            pass

    return d_polymer


def main():
    pdb_ids = """
    1FDH, 2DHB, 1HCO, 2HCO, 1HDS, 1HBS, 2MHB, 1HHO, 4HHB, 2HHB, 
    3HHB, 1COH, 1THB, 1NIH, 1PBX, 1BBB, 1CMY, 1DXT, 1DXU, 1DXV, 
    1ITH, 1BAB, 1HBA, 1HBB, 1HGA, 1HGB, 1HGC, 1HDA, 1CBL, 1CBM, 
    1FLP, 2PGH, 2HHD, 2HHE, 2HBC, 2HBD, 2HBE, 2HBF, 1HBH, 1HDB, 
    1GLI, 1MOH, 1SDK, 1SDL, 1CLS, 1IBE, 1GBU, 1GBV, 1OUT, 1OUU, 
    1SPG, 2HBS, 1HAB, 1HAC, 1ABY, 1VHB, 2VHB, 1A00, 1A01, 1A0U, 
    1A0Z, 1RVW, 1VWT, 1A3N, 1A3O, 1A4F, 1AJ9, 1A9W, 1ABW, 1BUW, 
    6HBW, 1BZ0, 1BZ1, 1BZZ, 1B86, 1HBR, 1BIJ, 1CG5, 1CG8, 1CH4, 
    1T1N, 1QPW, 1QSH, 1QSI, 1QI8, 1C40, 3VHB, 4VHB, 1EBT, 1B0B, 
    1DKE, 1C7B, 1C7C, 1C7D, 1GCV, 1GCW, 1DLW, 1DLY, 1G9V, 1G08
    """
    l_pdb_id = []
    for each in pdb_ids.strip().split(','):
        l_pdb_id.append(each.strip())

    l_pdb_id_human = []
    for pdb_id in l_pdb_id:
        d_polymer = getSource(pdb_id)
        for entity_id in d_polymer:
            if "homo sapiens" in d_polymer[entity_id]["source"]:
                l_pdb_id_human.append(pdb_id)
                l_line = [pdb_id, entity_id, "from human",
                          d_polymer[entity_id]["name"]]
                print('\t'.join(l_line))
    print("=========================")
    print(f"{len(list(set(l_pdb_id_human)))} strcutrues have human proteins")


if __name__ == "__main__":
    main()
