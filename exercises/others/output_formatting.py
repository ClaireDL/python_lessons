#!/usr/bin/env python

import json
import csv
import requests


def test(json_file, comparison, entry):
    # selects values for the test
    output = []
    output.append(comparison)
    expected_return = json_file[comparison][entry]["performance"]["expected_return"]
    output.append(expected_return)
    sharpe_ratio = json_file[comparison][entry]["performance"]["sharpe_ratio"]
    output.append(sharpe_ratio)
    volatility = json_file[comparison][entry]["performance"]["volatility"]
    output.append(volatility)
    return output

def header():
    csv_file.write("portfolio,")
    csv_file.write("expected_return,")
    csv_file.write("sharpe_ratio,")
    csv_file.write("volatility,")
    csv_file.write('\n')



# generates output for test1: efficient_risk_2p
with open("C:/Users/chdell/Downloads/result-3funds-ema_historical_return-exp_cov-1.00.json") as json_file:
    data = json.load(json_file)
    with open("efficient_risk_2p.csv", "w+") as csv_file:
        # adds header
        header()

        # collects values in the portfolios
        for portfolio in data:
            result = test(data, portfolio, "efficient_risk_2p")
            json.dump(result, csv_file, separators = (",", ":"))
            csv_file.write('\n')

    with open("efficient_risk_4p.csv", "w+") as csv_file:
        # adds header
        header()

        # collects values in the portfolios
        for portfolio in data:
            result = test(data, portfolio, "efficient_risk_4p")
            json.dump(result, csv_file, separators = (",", ":"))
            csv_file.write('\n')

    with open("max_sharpe.csv", "w+") as csv_file:
        # adds header
        header()

        # collects values in the portfolios
        for portfolio in data:
            result = test(data, portfolio, "max_sharpe")
            json.dump(result, csv_file, separators = (",", ":"))
            csv_file.write('\n')

    with open("min_volatility.csv", "w+") as csv_file:
        # adds header
        header()

        # collects values in the portfolios
        for portfolio in data:
            result = test(data, portfolio, "min_volatility")
            json.dump(result, csv_file, separators = (",", ":"))
            csv_file.write('\n')

# opens the output file
# with open("efficient_risk_2p.csv") as csv_file:
#     for line in csv_file:
#         print(line)