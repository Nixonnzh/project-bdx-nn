"""Load config variables."""
import yaml


def load_config(config_file="config.yaml"):
    """
    Load the configuration from a YAML file.

    Args:
        config_file (str): Path to the YAML configuration file.

    Returns:
        dict: Configuration dictionary.
    """
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)
    return config
