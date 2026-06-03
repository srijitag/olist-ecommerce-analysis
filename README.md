# Olist E-Commerce Analysis

I wanted to work through a real-world e-commerce dataset end to end - messy joins, missing data, the whole thing. The Olist dataset from Kaggle has 9 related tables covering orders, customers, sellers, payments and reviews from a Brazilian marketplace between 2016 and 2018. I used it to dig into two questions: how well does Olist actually deliver on its promised dates, and what does the customer base look like in terms of loyalty and value?

## What I found

- About 7.4% of orders arrive late. That sounds low until you notice that Olist builds a very generous buffer into estimates - 91% of orders actually arrive *early*. The late ones that slip through tend to be concentrated in specific states: Alagoas (AL) has a 23% late rate, Maranhão (MA) is at 19.6%.
- Late delivery has a real impact on customer satisfaction. Orders that arrive late average a review score of 2.45 out of 5, while on-time or early deliveries average 4.21. A t-test confirmed this gap is statistically significant, not just noise.
- The repeat purchase rate is about 3% across 93,000+ unique customers. Most people buy once and don't come back. The RFM segmentation puts around 7,900 customers in the "Champions" tier - they're a small group but likely driving a disproportionate share of revenue.

## Project structure

```
data/
    raw/          original CSVs from Kaggle
    processed/    cleaned master table and RFM output
notebooks/        all 4 analysis notebooks
outputs/
    charts/       saved chart PNGs
    reports/      for any Excel exports
src/
    load_data.py  helper to load all 9 tables
    utils.py      small utility functions
```

## Notebooks

1. **01_data_loading_and_schema** - loading all 9 tables and figuring out how they connect
2. **02_data_cleaning** - dates were strings, some orders were cancelled - fixed all of that and built the master joined table
3. **03_delivery_experience** - on-time vs late rate by state, and whether being late actually hurts review scores (with a t-test)
4. **04_customer_rfm_segmentation** - repeat purchase rate (very low as it turns out) and full RFM segmentation

## How to run it

```bash
git clone <repo-url>
cd olist-ecommerce-analysis
pip install -r requirements.txt
```

Download the [Olist dataset from Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) and put all 9 CSV files in `data/raw/`.

Then start JupyterLab from the project root and run the notebooks in order (01 through 04).

```bash
jupyter lab
```

## Tools used

pandas, numpy, matplotlib, seaborn, scipy, plotly, openpyxl

## Data source

Brazilian E-Commerce Public Dataset by Olist - https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
