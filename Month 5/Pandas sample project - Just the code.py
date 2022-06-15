"""
A copy of the code parts from the sample project notebook, without
any of the digressions or markdown cells.  This code has been slighly
re-organized for better readability.  I've also omitted some of the
steps where columns are dropped--this doesn't affect anything,
but it does cut down on the amount of code here.  If you're working
with really large datasets, though, and doing a lot of stuff to them,
then dropping unneeded columns can actually have a pretty big impact.
"""

import os
import pandas as pd

def load_county_data():
    """Load the county data and do necessary cleanup on it
    in peparation for joining to the census data."""
    counties = pd.read_csv("County FIPS codes.csv")
    counties["FIPS Code"] = counties["FIPS Code"] - 48000
    return counties
    
def load_naics():
    """Load the NAICS industry code data and do necessary
    cleanup on it in preparation for joining to the census
    data."""
    # Get the NAICS code data
    naics = pd.read_excel(
        "https://www.census.gov/naics/2022NAICS/2022_NAICS_Structure.xlsx",
        skiprows=[0, 1]
    )
    
    # Convert the 6-digit codes to "/"-padded strings.
    naics["2022 NAICS Code"] = [f"{i:/<6}" for i in naics["2022 NAICS Code"]]

    # Remove trailing "T"s and remove any rows with missing titles.
    naics = naics[~pd.isnull(naics["2022 NAICS Title"])]
    naics["2022 NAICS Title"] = [
        i[:-1] if i.endswith("T") else i
        for i in naics["2022 NAICS Title"].apply(lambda x: x.strip())
    ]
    
    return naics


def load_census_data():
    """Load the census bureau payroll data and do necessary
    transformations in preparation for joining with the NAICS/
    county FIPS code data."""
    # Get the census data if it hasn't been downloaded.
    if not os.path.isfile("Census Data.csv"):
        census_data = pd.read_csv(
            r"https://www2.census.gov/programs-surveys/cbp/datasets/2020/cbp20co.zip",
            compression="zip"
        )
        census_data.to_csv("Census Data.csv", index=False)
    else:
        census_data = pd.read_csv("Census Data.csv")

    # Rename some columns for better readability.
    census_data = (
        census_data
        .rename(
            columns={
                "fipstate": "State FIPS Code",
                "fipscty": "County FIPS Code",
                "naics": "Industry NAICS Code",
                "emp": "Number of Employees",
                "ap": "Annual Payroll",
                "est": "Number of Establishments"
            }
        )
    )

    # Just Texas rows
    census_data = census_data[census_data["State FIPS Code"] == 48]

    return census_data


# Load the three datasets
census = load_census_data()
county_names = load_county_data()
naics_codes = load_naics()

# Join everything!
# This uses `DataFrame.merge()` rather than `pd.merge()`.
# The only real difference is that `x.merge(y)` is equivalent
# to `pd.merge(left=x, right=y)`.  ALl the other arguments,
# e.g. "how" and the varion "on" keywords, are identical.
census = (
    census
    .merge(
        county_names,
        left_on="County FIPS Code",
        right_on="FIPS Code",
        how="left"
    )
    .merge(
        naics_codes,
        left_on="Industry NAICS Code",
        right_on="2022 NAICS Code",
        how="left",
    )
)

print("Highest paid counties:")
print(
    census
    .groupby("County Name")
    ["Annual Payroll"]
    .mean()
    .sort_values()
    [-10:]
)
print()

print("Highest paid industry-county combinations:")
print(
    census
    .groupby(["County Name", "2022 NAICS Title"])
    ["Annual Payroll"]
    .mean()
    .sort_values()
    [-10:]
)
