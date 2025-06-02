
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw" / "irds"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
RESULTS_DIR = PROJECT_ROOT / "results"

# IRDS Dataset Configuration
IRDS_CONFIG = {
    'subjects': 29,
    'patients': 15,
    'healthy_controls': 14,
    'gestures': 9,
    'joints': 25,
    'positions': ['sitting', 'standing'],
    'data_format': 'kinect_skeleton'
}

# ML Configuration
ML_CONFIG = {
    'algorithms': ['RandomForest', 'SVM', 'KNN'],
    'test_size': 0.2,
    'cv_folds': 5,
    'random_state': 42
}
