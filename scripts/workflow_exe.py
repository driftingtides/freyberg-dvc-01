import os
import flopy
import pyemu
import shutil

# disable depreciation warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def get_executables():
    bindir = os.path.join("bin")
    if os.path.exists(bindir):
        print("bin dir exists, skipping download")
        return
    os.mkdir(bindir)
    flopy.utils.get_modflow(bindir,repo='modflow6')
    pyemu.utils.get_pestpp(bindir)
    prefixes = [f.split(".")[0] for f in os.listdir(bindir)]
    assert "mf6" in prefixes
    assert "zbud6" in prefixes
    assert "pestpp-glm" in prefixes
    fnames = os.listdir(bindir)
    print(fnames)
    with open(os.path.join(bindir, "exe.txt"), "w") as f:
        for fname in prefixes:
            f.write(fname + "\n")
    return

def copy_executables_to_dir(ws,prefixes = ["mf6","zbud6","pestpp-glm"]):
    # copy executables to dir
    bindir = os.path.join("bin")
    fnames = [f for f in os.listdir(bindir) if f.split(".")[0] in prefixes]
    for f in fnames:
        shutil.copy2(os.path.join(bindir,f),os.path.join(ws,f))
    with open(os.path.join(ws, "exe.txt"), "w") as f:
        for fname in fnames:
            f.write(fname + "\n")


if __name__ == "__main__":
    
    # gets things ready...
    get_executables()
    

