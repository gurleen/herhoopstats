import requests
from bs4 import BeautifulSoup
import pandas as pd


cookies = {}


BASE_URL = "https://herhoopstats.com"


def format_url(path: str, options: dict = None):
    full_path = f"{BASE_URL}{path}"
    query_string = "&".join([f"{k}={v}" for k, v in options.items()])
    return f"{full_path}?{query_string}"


def make_request(path: str, table_idx: int = 0) -> pd.DataFrame:
    request = requests.get(path, cookies=cookies)
    df = pd.read_html(request.text)[table_idx]
    soup = BeautifulSoup(request.text, features="lxml")
    links = [x["href"] for x in soup.find("table").find_all("a")]
    df["link"] = links
    return df