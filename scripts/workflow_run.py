import os
import flopy
import shutil
import dvc.api

params = dvc.api.params_show()

def model_run(sim_ws):
    # run the simulation
    sim = flopy.mf6.MFSimulation.load(sim_ws=sim_ws, exe_name=os.path.join("..", "bin", "mf6"))
    sim.run_simulation()

    # Save 

if __name__ == "__main__":
    # Load YAML configuration
    model_run(params["model"]["sim_ws"])
