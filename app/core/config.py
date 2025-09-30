from pydantic import BaseSettings
import os
import yaml

class Settings(BaseSettings):
    database_url: str
    api_prefix: str = "/api/v1"
    nlp_model_path: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

def load_yaml_config(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

config = load_yaml_config(os.path.join(os.path.dirname(__file__), 'config.yaml'))
settings = Settings(**config)