# Zscaler Domain Category Lookup

## Overview

This Python script automates the process of querying Zscaler's SiteReview service to retrieve domain classification results. It is useful for categorizing and assessing web domains based on security and policy filters, especially in enterprise environments.

## Features

- Sends batch POST requests to Zscaler SiteReview to get category info
- Extracts both `ZURLDB` and `ThirdParty` category tags
- Outputs results into a clean Excel file (`.xlsx`)
- Handles basic exceptions and API errors
- Adds delay between requests to avoid rate limiting

## Requirements

- Python 3.x
- `requests` and `pandas` libraries (`pip install requests pandas`)
- Internet access (no authentication required for public API usage)

## Input

The input file should be a simple `.txt` file with one domain per line:

