# Documentation

## Overview

This script fetches and processes exchange rate data for a specified currency pair over a given period, providing key insights such as the best, worst, and average exchange rates. It also includes visualisation of the exchange rates over time. The script incorporates error handling, logging, caching, and command-line arguments for flexibility and robustness.

## Approach

Fetch Exchange Rates: Connect to the Exchange Rates API to retrieve exchange rate data for a specified date range.
Preprocess Data: Convert the API response to a pandas DataFrame, ensuring proper formatting and sorting.
Analyse Data: Calculate the best, worst, and average exchange rates for the given period.
Visualisation: Plot the exchange rates over time using matplotlib.
Error Handling: Handle various potential errors such as network issues, invalid inputs, and missing data.
Caching: Implement caching to avoid redundant API calls within a short period.



## Architecture

API Layer: Handles API requests and responses.
Data Processing Layer: Converts and preprocesses data for analysis.
Analysis Layer: Performs calculations to find key statistics (best, worst, and average rates).
Visualisation Layer: Plots the exchange rate data.
Error Handling and Logging: Captures and logs errors for troubleshooting.
Caching: Stores API responses temporarily to optimise performance.

## Best Practices Followed

Modular Code: The script is divided into distinct functions for fetching, preprocessing, and analysing data, making it easier to maintain and extend.
Error Handling: Comprehensive error handling is implemented to manage different failure scenarios gracefully.
Logging: Detailed logging provides visibility into the script's operations and helps in debugging.
Caching: Caching improves performance by reducing redundant API calls.
Documentation: Clear and concise documentation helps in understanding the script's functionality and usage.
Testing: Unit tests ensure the script handles various scenarios correctly.
Code Readability: Code is written in a clear and consistent style, following PEP 8 guidelines where applicable.