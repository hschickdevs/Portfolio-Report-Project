from os import getenv

MANDATORY_VARS = ['FINNHUB_APIKEY']
def handle_env():
    """Checks if the .env file exists in the current working dir, and imports the variables if so"""
    try:
        envpath = find_dotenv(raise_error_if_not_found=True, usecwd=True)
        load_dotenv(dotenv_path=envpath)
    except:
        pass
    finally:
        for var in MANDATORY_VARS:
            if getenv(var) is None:
                raise ValueError(f"Missing environment variable: {var}")