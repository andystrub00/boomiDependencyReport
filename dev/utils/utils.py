import os
from dotenv import dotenv_values


def fetch_env_variables(env_filename=".env", env_path=None):

    if env_path is None:
        base_dir = os.path.dirname(
            os.path.dirname(os.path.realpath(__file__))
        )  # Gets /dev
        env_path = os.path.join(base_dir, "env", ".env")

    return dotenv_values(env_path)
