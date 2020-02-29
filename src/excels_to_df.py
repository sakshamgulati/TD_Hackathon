import os
import pandas as pd


# Creates main dataframe and a dictionary with key: ticker and value: company's price and returns data
def excels_to_df():
    # dataframe for companies.csv
    companies_df = pd.read_csv("../hackathon_data/companies.csv")

    # NEED TO CHANGE THIS FOR TESTING
    os.chdir("../hackathon_data/company_prices_returns")
    curr_path = os.getcwd()
    files = os.listdir(curr_path)
    csv_files = [f for f in files if f[-3:] == 'csv']

    # Define a dataframe with the required column names
    column_names = ('Ticker', 'Date', 'Close', 'Returns')
    price_returns_df = pd.DataFrame(columns=column_names)

    for csv_files in csv_files:
        company = pd.read_csv(csv_files)
        date = company["Date"]
        close = company["Close"]
        returns = company["Returns"]
        ticker = csv_files.strip('_adj_close.csv')
        d = {'Ticker': ticker, 'Date': date, 'Close': close, 'Returns': returns}
        company_df = pd.DataFrame(data=d)
        price_returns_df = price_returns_df.append(company_df, ignore_index=True)

    return [companies_df, price_returns_df]



if __name__ == "__main__":
    data = excels_to_df()
    companies_df = data[0]
    price_returns_df = data[1]
    companies_df.to_csv("companes_df.csv")
    price_returns_df.to_csv("price_returns_df.csv")


