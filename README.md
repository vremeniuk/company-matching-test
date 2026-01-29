# company-matching-test

## Description
This project matches companies between two datasets based on company name and location.

## Project Structure
- data/ — input CSV datasets
- src/ — data processing logic
- main.py — entry point of the application

## Approach
1. Loaded both datasets into pandas DataFrames.
2. Normalized company names and location fields to handle formatting inconsistencies.
3. Matched datasets using the normalized company name with a left join to preserve all records from Dataset 1.
4. Identified overlapping locations based on normalized city and country fields.
5. Calculated matching metrics on a company (entity) level.

## Metrics
- **Match rate** — percentage of companies from Dataset 1 that have at least one matching company with overlapping location in Dataset 2.
- **Unmatched rate** — percentage of companies from Dataset 1 with no matching location.
- **One-to-many rate** — percentage of companies that have multiple potential matches after merging datasets.
- **Partial match rate** — percentage of companies where company names matched, but no overlapping location was found.  
  This metric helps identify cases such as companies with multiple offices or inconsistent location data.

## How to run
1. Install dependencies:
   pip install -r requirements.txt
2. Run the project:
   python main.py
