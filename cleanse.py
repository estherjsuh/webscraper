from app import product_title, prices
import pandas as pd
from datetime import date
from config import brand

cleansed_prices = []
cleansed_titles = []

for p in prices:
    cleansed_prices.append(int(p.strip().replace('$','')))

for t in product_title:
    cleansed_titles.append(t.strip())

availability = pd.DataFrame(
    {'date': date.today().strftime("%m/%d/%y"),
    'brand': brand,
    'product_title': cleansed_titles,
    'price': cleansed_prices}
)
