import logging
import sys

import yaml

CONFIG = {

}

def load_config() -> dict[str, str]:
    """Loads the config file """
    try:
        with open("config.yaml", "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        logging.warning("Config file not found")
        return {}
    except yaml.YAMLError as e:
        logging.error(f"Config parsing error: {e}")
    except Exception as e:
        logging.error(f"Unknown error: {e}")

    sys.exit(1)

user_config = load_config()

CONFIG.update(user_config)
