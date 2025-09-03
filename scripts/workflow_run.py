import os
import flopy
import shutil
import dvc.api
from dvclive import Live

params = dvc.api.params_show()

def model_run(sim_ws):
    # run the simulation
    sim = flopy.mf6.MFSimulation.load(sim_ws=sim_ws, exe_name=os.path.join("..", "bin", "mf6"))
    success, _ = sim.run_simulation()

    # Get things to save 
    gwf = sim.get_model()
    mf_list = gwf.output.list()
    print(mf_list.get_model_runtime())

    # Save to DVC metrics
    with Live() as live:
        live.log_metric("simulation/name", sim.name)
        live.log_metric("simulation/nnodes", gwf.modelgrid.nnodes)
        live.log_metric("simulation/totim", mf_list.get_times()[-1])
        live.log_metric("simulation/runtime", mf_list.get_model_runtime())
        live.log_metric("simulation/success", success)

if __name__ == "__main__":
    # Load YAML configuration
    model_run(params["sim"]["sim_ws"])
