import pandas as pd

columns = ["company_name","city","country"]

# 1. read data
df_1 = pd.read_csv("data/raw/dataset_1.csv")
df_2 = pd.read_csv("data/raw/dataset_2.csv")

# 2. normalize
df_1["company_name_norm"] = df_1["company_name"].str.lower().str.strip()
df_2["company_name_norm"] = df_2["company_name"].str.lower().str.strip()

df_1["company_name_norm"] = (
    df_1["company_name_norm"]
    .str.replace('ltd', '', regex=False)
    .str.replace('inc', '', regex=False)
    .str.replace(',', '', regex=False)
    .str.replace('.', '', regex=False)
    .str.strip()
)

df_2["company_name_norm"] = (
    df_2["company_name_norm"]
    .str.replace('ltd', '', regex=False)
    .str.replace('inc', '', regex=False)
    .str.replace(',', '', regex=False)
    .str.replace('.', '', regex=False)
    .str.strip()
)

df_1["country_norm"] = (
    df_1["country"]
    .str.lower()
    .str.strip()
)

df_2["country_norm"] = (
    df_2["country"]
    .str.lower()
    .str.strip()
)

df_1["city_norm"] = (
    df_1["city"]
    .str.lower()
    .str.strip()
)

df_2["city_norm"] = (
    df_2["city"]
    .str.lower()
    .str.strip()
)

# 3. match
merged_companies = (
    df_1
    .merge(df_2, on='company_name_norm', how='left')
)

merged_companies['overlapping_locations'] = (
    (merged_companies["city_norm_x"] == merged_companies["city_norm_y"]) &
    (merged_companies["country_norm_x"] == merged_companies["country_norm_y"])
)

# 4. metrics

## company match rate
company_match = (
    merged_companies
    .groupby("company_name_norm")["overlapping_locations"]
    .any()
)

match_rate = company_match.mean() * 100

## company unmatched rate
unmatched_companies = company_match[company_match == False]
unmatched_rate = len(unmatched_companies) / len(company_match) * 100

## one-to-many rate
company_counts = (
    merged_companies
    .groupby("company_name_norm")
    .size()
)

one_to_many_rate = (company_counts > 1).mean() * 100

## partial match rate
partial_match = (
    merged_companies
    .groupby("company_name_norm")["overlapping_locations"]
    .any() == False
)

partial_match_rate = partial_match.mean() * 100


# 5. save output
merged_companies.to_csv("data/output/merged_companies.csv", index=False)
