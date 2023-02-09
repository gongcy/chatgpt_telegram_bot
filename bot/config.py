import yaml
import dotenv
from pathlib import Path

MONGODB_IP = "localhost"
MONGODB_PORT = 27017  # MongoDB port

config_dir = Path(__file__).parent.parent.resolve() / "conf"

# load yaml config
with open(config_dir / "config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# load .env config
config_env = dotenv.dotenv_values(config_dir / "config.env")

# config parameters
telegram_token = config_yaml["telegram_token"]
openai_api_key = config_yaml["openai_api_key"]
allowed_telegram_usernames = config_yaml["allowed_telegram_usernames"]
new_dialog_timeout = config_yaml["new_dialog_timeout"]
mongodb_uri = f"mongodb://{MONGODB_IP}:{MONGODB_PORT}"
