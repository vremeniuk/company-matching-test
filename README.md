# company-matching-test

## Description
This project matches companies between two datasets based on company name and location.

## Project Structure
- data/raw — input CSV datasets
- data/output — merged dataset output
- src/ — data processing logic
- main.py — entry point of the application

## Approach
1. Loaded both datasets into pandas DataFrames.
2. Normalized company names and location fields to handle formatting inconsistencies.
3. Matched datasets using the normalized company name with a left join to preserve all records from Dataset 1.
4. Identified overlapping locations based on normalized city and country fields.
5. Calculated matching metrics on a company (entity) level.

## Matching approach
Companies were matched using normalized company names.
After name matching, city and country were compared to identify overlapping locations.
A left join was used to ensure that all companies from Dataset 1 are preserved,
even if no matching company exists in Dataset 2.

## Normalization and transformations
The following normalization steps were applied:
- Converted company names, cities, and countries to lowercase
- Trimmed leading and trailing whitespace
- Removed common legal suffixes such as "ltd" and "inc"
- Removed punctuation characters

This helped reduce inconsistencies caused by formatting differences.

## Data quality issues
During analysis, the following data quality issues were identified:
- Inconsistent company name formatting
- Missing or mismatched location information
- Companies appearing multiple times with different locations
- Partial matches where company names matched but locations did not


## Calculated metrics
The following metrics were calculated:
- Match rate: percentage of companies from Dataset 1 with at least one matching location
- Unmatched rate: percentage of companies with no matching locations
- One-to-many rate: percentage of companies matched to multiple records
- Partial match rate: companies with matched names but no overlapping locations

## How to run
1. Install dependencies:
   pip install -r requirements.txt
2. Run the project:
   python main.py
