# CoinGecko to Google Sheets

Automatically fetch daily crypto market data from the CoinGecko public API and update a Google Sheets spreadsheet via GitHub Actions. No server required.

## Tech Stack
- Python 3
- requests
- pandas
- gspread
- google-auth
- GitHub Actions

## Features
- Fetch top 50 coins by market cap from CoinGecko
- Clean and format data with pandas
- Write to Google Sheets automatically
- Run daily via GitHub Actions
- Manual trigger supported

## Data Fields
- market_cap_rank
- name
- symbol
- current_price
- price_change_percentage_24h
- market_cap
- total_volume

## Setup

### 1. Google Service Account
1. Create a project in Google Cloud Console
2. Enable Google Sheets API
3. Create a Service Account and download th JSON key
4. Share your Google Sheet with the Service Account email as Editor

### 2. Environment Variables
Set these locally or in GitHub Secrets:
- `SHEET_ID`: your Google Sheet ID
- `GOOGLE_CREDENTIALS`: the full JSON key content

### 3. Run Locally
```bash
pip install -r requirements.txt
export SHEET_ID=your_sheet_id
python main.py
```
### 4. GitHub Actions
Add SHEET_ID and GOOGLE_CREDENTIALS to repository Secrets. The workflow runs daily at 00:00 UTC.

## Output
a Google Sheet with 50 rows of crypto market data, updated daily.

## Notes
- Uses CoinGecko free public API, subject to rate limits
- No trading, wallet, or private key functionality
