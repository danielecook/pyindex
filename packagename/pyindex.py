import requests
import csv
import pandas as pd

NASDAQ
NYSE
AMEX


exchange = requests.get("http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download")
header = [x.strip("\"") for x in exchange.text.splitlines()[0].split(",")][:-1]
m = list(csv.DictReader(exchange.text.splitlines()))

m = pd.read_csv("http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download")