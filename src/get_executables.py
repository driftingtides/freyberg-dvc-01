import os
import flopy
import pyemu


def get_executables():
    """Checks if executables are in the bin directory, if not, downloads them. Does this for MF6 and PESTPP"""
    bindir = os.path.join("bin")
    if os.path.exists(bindir):
        print("bin dir exists, skipping download")
        return
    os.mkdir(bindir)
    # flopy.utils.get_modflow(bindir,repo='executables')
    flopy.utils.get_modflow(bindir, repo='executables')
    pyemu.utils.get_pestpp(bindir)
    prefixes = [f.split(".")[0] for f in os.listdir(bindir)]
    # assert "mf2005" in prefixes, "error getting mf2005"
    # assert "pestpp-ies" in prefixes, "error getting pestpp"
    print(os.listdir(bindir))
    return


if __name__ == "__main__":
    get_executables()
