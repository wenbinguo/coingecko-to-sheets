import os
import requests
import pandas as pd
from sheets import get_sheet

SHEET_ID = os.environ['SHEET_ID']


def fetch_market_data() -> pd.DataFrame:
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': '50',
        'page': '1',
        'price_change_percentage': '24h'
    }

    headers = {
        'User-Agent': 'CryptoMarketDataBot/1.0',
        'x-cg-demo-api-key': os.environ.get('COINGECKO_API_KEY', '')
    }
    resp = requests.get(url, params=params, headers=headers, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    df = pd.DataFrame(data)[['market_cap_rank', 'name', 'symbol', 'current_price',
                             'price_change_percentage_24h', 'market_cap', 'total_volume'
                             ]]

    df["price_change_percentage_24h"] = df["price_change_percentage_24h"].fillna(0)
    df = df.where(pd.notnull(df), "")
    return df


def push_to_sheet(df: pd.DataFrame, sheet_id: str) -> None:
    ws = get_sheet(sheet_id, 'Market')
    ws.clear()
    ws.update([df.columns.to_list()] + df.values.tolist())


def main():
    df = fetch_market_data()
    push_to_sheet(df, SHEET_ID)
    print(f'Updated {len(df)} rows')


if __name__ == '__main__':
    main()
