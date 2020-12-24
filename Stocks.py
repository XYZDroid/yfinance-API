import yfinance as yf
import os
data_file = ("Stocks.txt")
AllStocks = ["AAPL", "GOOGL", "AMZN", "FB", "TWTR",]

def FindPrices(AllStocks):
    item = 0
    print("Initializing...")
    for price in AllStocks:
        ticker = AllStocks[item]
        print(f"Fetching prices for {AllStocks[item]}.")
        stock = yf.Ticker(ticker)
        indata = (str(round(stock.history(period="1d"), 2)))
        send_data = open(data_file, 'a')
        send_data.write("-" * 100)
        send_data.write("\r\n")
        send_data.write(AllStocks[item])
        send_data.write("\r\n")
        send_data.write(indata)
        send_data.write("\r\n")
        print(f"Fetched data for {AllStocks[item]}.")
        item += 1
    # Translates the bytes into a specific file size.
    def identify_filesize():
        if Bytes >= 10 ** 3:
            Kilobytes = Bytes/10 ** 3
            print(f"\n\rThe following file: {data_file}, contains {Kilobytes} Kilobytes.")
        elif Bytes >= 10 ** 6:
            Megabytes = Bytes/10 ** 6
            print(f"\n\rThe following file: {data_file}, contains {Megabytes} Megabytes.")
        elif Bytes >= 10 ** 9:
            Gigabytes = Bytes/10 ** 9
            print(f"\n\rThe following file: {data_file}, contains {Gigabytes} Gigabytes.")
        elif Bytes >= 10 ** 12:
            Terabytes = Bytes/10 ** 12
            print(f"\n\rThe following file: {data_file}, contains {Terabytes} Terabytes.")
        else:
            print(f"\n\rThe following file: {data_file}, contains {Bytes} Bytes.")
    Bytes = len("Stock.txt")
    send_data.close()
    identify_filesize()
    print(f"Fetched prices and data for a total # of {item} stocks.")

FindPrices(AllStocks)
print("Operation Complete.")
