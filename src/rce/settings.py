import pathlib
import logging

logger = logging.getLogger(__name__)

project_root = pathlib.Path(__file__).parents[2]
data_dir = project_root / 'data'
config_json_path = project_root / 'config.json'
