# Zillow Regression Project

### Author: Austin Aranda and Luke Becker

## Description: 
The purpose of this project is, using the Zillow dataset, develop a model that is able to predict property tax values. In addition, we plan on creating a report laying out:
    1. Where the properties are located (by state and county)
    2. distribution of tax rates for each county
    3. 

## Project Organization

Generated with [ryans_codeup_data_science_mvp](https://github.com/RyanMcCall/ryans_codeup_data_science_mvp)

Modified from [datasciencemvp](https://github.com/cliffclive/datasciencemvp/)

```
├── README.md               <- The top-level README for developers using this project.
│
├── data                    <- All of the data for the project
│   ├── modeling            <- The prepared, processed and split datasets for modeling.
│   ├── prepared            <- The prepared datasets for exploration
│   └── raw                 <- The original, immutable data
│
├── main.py                 <- The main python script that calls all src scripts
│
├── mvp.ipynb               <- The main notebook for the project
│
├── src                     <- The source code for use in this project
│   ├── __init__.py         <- Makes src a Python module
│   ├── acquire.py          <- The script to download or generate data and store it in
│   │                          data/raw/
│   ├── explore.py          <- The script for creating any visuals that need to be stored
│   │                          in visuals/generated_graphics/
│   ├── model.py            <- The script for preprocessing, modeling, and interpreting
│   └── prepare.py          <- The script for preparing the raw data and storing it in
│                              data/prepared/
│
└── visuals                 <- All project visuals
    ├── external_visuals    <- Visuals brought from outside the project
    ├── generated_graphics  <- Visuals generated from the project
    └── presentation        <- A copy of your presentation
```

## Project Planning

Questions:
- Does number of bedrooms matter to the tax valuation?
- Does location within the state or county affect tax valuation?
- Is total square footage independent of tax valuation?
- Does a combined bedroom/bathroom square footage feature have better correlation with the target variable than the separate features?
- Does lot size have a better correlation with tax valuation than house square footage?


### Hypothesese:
- $H_0$: Property square footage is not related to tax valuation
- $H_a$: Property square footage is related to tax valuation

- $H_0$: The number of bedrooms is not related to tax valuation
- $H_a$: The number of bedrooms is related to tax valuation


## Data Dictionary

| Feature | Definition |
| --- | --- |
| Feature 1 | Definition 1 |
| Feature 2 | Definition 2 |

| Target | Definition |
| --- | --- |
| Target 1 | Definition 1 |