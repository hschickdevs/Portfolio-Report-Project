import requests


def get_stock_price(symbol: str) -> float:
    pass

def handle_env():
    """Checks if the .env file exists in the current working dir, and imports the variables if so"""
    try:
        envpath = find_dotenv(raise_error_if_not_found=True, usecwd=True)
        load_dotenv(dotenv_path=envpath)
    except:
        pass
    finally:
        mandatory_vars = ['FINNHUB_APIKEY']
        for var in mandatory_vars:
            val = getenv(var)
            if val is None:
                raise ValueError(f"Missing environment variable: {var}")