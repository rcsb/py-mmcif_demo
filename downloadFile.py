#!/usr/bin/env python3
# =============================================================================
# Author:  Chenghua Shao
# Date:    2023-02-17
# Updates:
# =============================================================================
"""
download utility for PDBx/mmCIF files
"""

import os
import gzip
import shutil
import urllib.request


def downloadFile(id, file_type="pdb-model", folder="/tmp"):
    """download file from PDB

    Args:
        id (str): id
        file_type (str, optional): id type. Defaults to "pdb-model".
        folder (str, optional): local folder to save the file. Defaults to "/tmp".

    Returns:
        filepath_local: local filepath. None if download fails.
    """
    file_type = file_type.strip().lower()
    if file_type == "pdb-model":
        id = id.strip().lower()
        url = f"https://files.wwpdb.org/pub/pdb/data/structures/divided/mmCIF/{id[1:3]}/{id}.cif.gz"
    elif file_type == "pdb-validation":
        id = id.strip().lower()
        url = f"https://files.wwpdb.org/pub/pdb/validation_reports/{id[1:3]}/{id}/{id}_validation.cif.gz"
    elif file_type == "ccd-definition":
        id = id.strip().upper()
        url = f"https://files.wwpdb.org/pub/pdb/refdata/chem_comp/{id[-1]}/{id}/{id}.cif"
    else:
        return None

    filepath_local = os.path.join(folder, url.split('/')[-1])

    try:
        urllib.request.urlretrieve(url, filepath_local)
    except urllib.error.HTTPError as err_http:
        print(err_http)
        print("%s file doesn't exist for id %s, check id" % (file_type, id))
    except OSError as err_os:
        print(err_os)
        print("cannot write file to the designated folder %s, check privilege" % folder)
    except Exception as err_other:
        print(err_other)
        print("fail to download %s file for id %s" % (file_type, id))
    else:
        if filepath_local.endswith(".gz"):
            filepath_local_unzipped = filepath_local.strip(".gz")
            try:
                with gzip.open(filepath_local, 'rb') as file_in:
                    with open(filepath_local_unzipped, 'wb') as file_out:
                        shutil.copyfileobj(file_in, file_out)
                        os.remove(filepath_local)
                return filepath_local_unzipped
            except Exception as err_unzip:
                print(err_unzip)
                print("cannot unzip %s, check file format or privilege in the folder" % filepath_local)
        else:
            return filepath_local
    return None  #return None for if any exception is encountered


def main():
    print(downloadFile("2hyv"))
    print(downloadFile("7r2y", file_type="pdb-validation"))
    print(downloadFile("ATP", file_type="ccd-definition"))


if __name__ == "__main__":
    main()
