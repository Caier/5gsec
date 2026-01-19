import flasksrv
from flasksrv import app
from svf_abi import SVF_O5GS

if __name__ == "__main__":
    svf = SVF_O5GS()
    svf.initialize()
    flasksrv.ogs_api = svf
    app.run("0.0.0.0", 5000)
