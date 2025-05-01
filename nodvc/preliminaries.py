#%% Import Flopy files 


#https://github.com/modflowpy/flopy/blob/2e452ba15dff94b0cf0a37387c9e023b8c714772/.docs/Notebooks/feat_working_stack_examples.py
from pathlib import Path
from tempfile import TemporaryDirectory

import git
import pooch

# First create a temporary workspace.

sim_name = "freyberg_multilayer_transient"
temp_dir = TemporaryDirectory()
workspace = Path(temp_dir.name)

# Check if we are in the repository and define the data path.

try:
    root = Path(git.Repo(".", search_parent_directories=True).working_dir)
except:
    root = None

data_path = root / "nodvc" / "examples" / "data" if root else Path.cwd()

# Download files if needed.

file_names = {
    "freyberg.bas": "781585c140d40a27bce9369baee262c621bcf969de82361ad8d6b4d8c253ee02",
    "freyberg.cbc": "d4e18e968cabde8470fcb7cb8a1c4cc57fcd643bd63b23e7751460bfdb651ea4",
    "freyberg.ddn": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "freyberg.dis": "1ef61a467a219c036e58902ce11297e06b4eeb5f2f9d2ea40245b421a248a471",
    "freyberg.drn": "93c22ab27d599938a8c2fc5b420ec03e5251b11b050d6ae1cb23ce2aa1b77997",
    "freyberg.hds": "0b3e911ef35f625d2d046e05a20bc1300341b41028220c5b25ace6f5a267ceef",
    "freyberg.list": "14ec36c22b48d253d6b82c44f36c5bad4f0785b3a3384b386f6b69c4ee2e31bf",
    "freyberg.nam": "9e3747ce6d6229caec55a9357285a96cb4608dae11d90dd165a23e0bb394a2bd",
    "freyberg.nwt": "d66c5cc255d050a0f871639af4af0cef8d48fa59c1c64217de65fc6e7fd78cb1",
    "freyberg.oc": "faefd462d11b9a21c4579420b2156fb616ca642bc1e66fc5eb5e1b9046449e43",
    "freyberg.rch": "93a12742a2d37961d53df0405e39cbecf0e6f14d45b5ca8cbba84a2d90828258",
    "freyberg.upw": "80838be7af2f97c92965bad1d121c252b69d9c66e4885c5f3f49a6e99582deac",
    "freyberg.wel": "dd322655eadff3f618f0835c9277af30720197bd48328aae2d6772f26eef2686",
}
for fname, fhash in file_names.items():
    pooch.retrieve(
        url=f"https://github.com/modflowpy/flopy/raw/develop/examples/data/{sim_name}/{fname}",
        fname=fname,
        path=data_path / sim_name,
        known_hash=fhash,
    )

    
# %%
