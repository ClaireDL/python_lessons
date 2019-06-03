#!/usr/bin/env python

import json
import csv
import requests


def test(input_file, comparison, entry):
    # selects values of the test that have to be exported
    output = []
    output.append(comparison)
    expected_return = input_file[comparison][entry]["performance"]["expected_return"]
    output.append(expected_return)
    sharpe_ratio = input_file[comparison][entry]["performance"]["sharpe_ratio"]
    output.append(sharpe_ratio)
    volatility = input_file[comparison][entry]["performance"]["volatility"]
    output.append(volatility)

    output_csv = ",".join(map(str, output))

    return output_csv

def header(name):
    name.write("portfolio,")

    header_efficient_risk_2p = "2p_expected_return, 2p_sharpe_ratio, 2p_volatility,"
    header_efficient_risk_4p = "4p_expected_return, 4p_sharpe_ratio, 4p_volatility,"
    header_max_sharpe = "maxS_expected_return, maxS_sharpe_ratio, maxS_volatility,"
    header_min_volatility = "minV_expected_return, minV_sharpe_ratio, minV_volatility"

    name.write(header_efficient_risk_2p)
    name.write(header_efficient_risk_4p)
    name.write(header_max_sharpe)
    name.write(header_min_volatility)
    name.write('\n')



# generates output for test1: efficient_risk_2p
with open("C:/Users/chdell/Downloads/result-3funds-ema_historical_return-exp_cov-1.00.json") as json_file:
    data = json.load(json_file)
    with open("result.csv", "w+") as csv_file:
        # adds header
        header(csv_file)

        # collects values in the portfolios and writes the output
        for portfolio in data:
            result = test(data, portfolio, "efficient_risk_2p")
            csv_file.write(result)
            result = test(data, portfolio, "efficient_risk_4p")
            csv_file.write(result)
            result = test(data, portfolio, "max_sharpe")
            csv_file.write(result)
            result = test(data, portfolio, "min_volatility")
            csv_file.write(result)
            csv_file.write('\n')

# opens the output file
# with open("efficient_risk_2p.csv") as csv_file:
#     for line in csv_file:
#         print(line)
