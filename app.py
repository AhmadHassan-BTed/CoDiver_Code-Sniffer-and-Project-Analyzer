import sys
from pathlib import Path

# Add src to sys.path to allow importing the internal package
sys.path.append(str(Path(__file__).parent / "src"))

from software_metrics.ui.dashboard import run_app

if __name__ == "__main__":
    run_app()
