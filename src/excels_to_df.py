import csv
import os
import numpy as np
import pandas as pd
import csv

def excels_to_df():
    # Create dataframe
    main_df = pd.read_csv("../hackathon_data/companies.csv")
    print(main_df)

    # NEED TO CHANGE THIS FOR TESTING
    os.chdir("../hackathon_data/company_prices_returns")
    curr_path = os.getcwd()
    files = os.listdir(curr_path)
    csv_files = [f for f in files if f[-3:] == 'csv']

    # create dict with ticker to company's df of price and returns
    ticker_to_df = {}
    company_tickers = []
    for csv in csv_files:
        start = csv.find("_adj_close.csv")
        company_tickers.append(csv[:start])

    for i in range(len(company_tickers)):
        ticker = company_tickers[i]
        ticker_to_df[ticker] = pd.read_csv(csv_files[i])

    print(ticker_to_df)


if __name__ == "__main__":
    excels_to_df()

