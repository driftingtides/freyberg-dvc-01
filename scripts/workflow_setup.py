import os
import flopy
import shutil
from ruamel.yaml import YAML
import dvc.api

params = dvc.api.params_show()

def model_setup(org_ws, sim_ws):
    # org_ws = os.path.join("data", "models", "freyberg")

    if os.path.exists(sim_ws):
        shutil.rmtree(sim_ws)
    shutil.copytree(org_ws, sim_ws)


    # Change well package


    # write the simulation
    sim = flopy.mf6.MFSimulation.load(sim_ws=sim_ws, exe_name=os.path.join("bin", "mf6"))
    sim.write_simulation()


if __name__ == "__main__":
    # Load YAML configuration
    model_setup(params["model"]["org_ws"], params["model"]["sim_ws"])
