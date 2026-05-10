import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from src.ui.dashboard import run_app

if __name__ == "__main__":
    run_app()
