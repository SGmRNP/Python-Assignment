# In order to run this code,
# installation of three librarries
# requests, csv and pandas is necessary

# Importing Libraries
import requests
import csv
import pandas as pd
# calling the API
data = requests.get("https://api.coinmarketcap.com/v1/ticker/")
d = data.json()
# Opening a new csv file
outputFile = open("new.csv", 'w')
output = csv.writer(outputFile)
# writing the rowname for csv file
output.writerow(d[0].keys())
# writing the rows in csv file
for row in d:
    output.writerow(row.values())
outputFile.close()
# reading tha saves csv file
ans2 = pd.read_csv("new.csv")
# finding the max value of 24h_volume_use
hrmx = max(ans2['24h_volume_usd'])
# finding the name coin coin correspoding to maximum value
coin = ans2['name'][ans2['24h_volume_usd'] == hrmx].values
# printing the result
print("coin had highest 24 hour volume: {}".format(coin))
