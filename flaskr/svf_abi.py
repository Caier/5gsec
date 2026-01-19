from ctypes import CDLL, create_string_buffer
from pathlib import Path

class SVFException(Exception):
    """Exception for OGS_ERROR returns"""

class SVF_O5GS:
    def __init__(self, path: Path = Path("../build/libsvfd.so")) -> None:
        self.lib = CDLL(path)

    def initialize(self, conf_path: Path = Path("../config/svf.yaml")):
        self.lib.init_open5gs(str(conf_path).encode("ascii"))

    def get_enc_k(self, imsi: str) -> bytes:
        buf = create_string_buffer(128)
        buf[0] = 0
        rv = self.lib.svf_get_enc_k(imsi.encode("ascii"), buf)
        if rv != 0:
            raise SVFException(f"Got return code: {rv}")
        
        return buf.value
