import os

def get_config():
    return {
        "ENV": os.environ.get("APP_ENV", "dev"),
        "VERSION": os.environ.get("APP_VERSION", "1.0"),
        "DEBUG": os.environ.get("DEBUG", "false"),
        "FEATURE_FLAG": os.environ.get("FEATURE_FLAG", "off")
    }