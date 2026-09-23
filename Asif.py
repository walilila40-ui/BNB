import sys
import importlib.util
from pathlib import Path

base = Path(__file__).parent

if sys.version_info[:2] == (3, 11):
    so_file = base / "BNBM.cpython-311.so"
elif sys.version_info[:2] == (3, 13):
    so_file = base / "BNBM.cpython-313-aarch64-linux-android.so"
else:
    raise RuntimeError(f"Unsupported Python version: {sys.version}")

spec = importlib.util.spec_from_file_location("BNBM", so_file)
BNBM = importlib.util.module_from_spec(spec)
spec.loader.exec_module(BNBM)

BNBM.main()
