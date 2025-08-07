import os
import flopy
import shutil
from ruamel.yaml import YAML
from box import ConfigBox

yaml = YAML(typ="safe")

def model_setup(org_ws, sim_ws):
    org_ws = os.path.join("data", "models", "freyberg")

    if os.path.exists(sim_ws):
        shutil.rmtree(sim_ws)
    shutil.copytree(org_ws, sim_ws)

    sim = flopy.mf6.MFSimulation.load(sim_ws=sim_ws)
    sim.write_simulation()


if __name__ == "__main__":
    params = ConfigBox(yaml.load(open("params.yaml", encoding="utf-8")))
    # gets things ready...
    model_setup(params.model.org_ws, params.model.sim_ws)
    