# company-matching-test

## Description
This project matches companies between two datasets based on company name and location.

## Project Structure
- data/ — input CSV datasets
- src/ — data processing logic
- main.py — entry point of the application

## Approach
1. Loaded both datasets.
2. Normalized company names.
3. Matched datasets using normalized name, city and country.
4. Identified matched and unmatched companies.

## How to run
1. Install dependencies:
   pip install -r requirements.txt
2. Run the project:
   python main.py