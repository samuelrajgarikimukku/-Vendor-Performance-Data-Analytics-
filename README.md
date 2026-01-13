# Vendor Performance, Pricing, and Inventory Efficiency Analysis

This repository contains a full analytical study of vendor performance, pricing behavior, inventory turnover, bulk purchasing effects, and profitability behavior within a retail and wholesale environment. The work uses real multi-source transactional datasets and answers concrete business questions around margin dynamics, vendor dependency, slow-moving inventory, and pricing decisions.

## 1. Project Overview

I analyzed purchase, pricing, sales, and inventory data to evaluate how vendors, brands, and products contribute to profitability and operational efficiency. The output includes exploratory analysis, statistical validation, computed metrics, vendor segmentation, and dashboards.

The primary objective is to understand how purchasing behavior, price strategies, and inventory movement affect profit and supply chain stability.

## 2. Business Context

Retail and wholesale businesses depend on optimized pricing, diversified vendor relationships, efficient turnover, and cost-aware procurement. Operational weaknesses cause locked working capital, reduced margins, and high supply exposure. This analysis identifies where those weaknesses occur.

## 3. Data Sources

The datasets used represent the core retail lifecycle from procurement to sale:

- Vendor_invoice (5,543 records)
- Begin_inventory (206,529 records)
- End_inventory (224,489 records)
- Purchase (2,372,474 records)
- Purchase_price (12,261 records)
- Sales (12,825,363 records)

These datasets include quantities, unit prices, vendor identifiers, freight, total purchase values, revenue, and inventory states.

## 4. Analytical Approach

The analysis includes:

- Data cleaning, merging, and anomaly removal
- Computation of profit, margin, turnover, and unsold capital
- Vendor segmentation based on volume and margin
- Bulk purchasing cost comparison
- Correlation analysis between price, margin, turnover, and profitability
- Statistical validation between vendor segments
- Dashboard and visualization outputs for interpretation

## 5. Key Metrics and Insights

Examples of insights derived:

- Top 10 vendors contribute 65.69% of total purchases, indicating supply concentration risk.
- Large purchase orders achieve approximately 72% lower unit cost, confirming bulk cost advantage.
- Low-volume vendors have higher margins (mean ~41.55%) than high-volume vendors (mean ~31.17%).
- Unsold inventory capital approximates $2.71M, indicating slow-moving stock.
- 198 brands identified with high margins but low volumes suitable for promotion or pricing actions.
- Price increases compress margins due to competitive pressure.
- Turnover speed does not guarantee profitability.

## 6. Visual Outputs and Explanations

All referenced images are part of the analysis and should be placed in the repository root for direct display.

**Vendor Contribution Distribution**\
The chart below visualizes total purchase contribution by vendor, highlighting the concentration in the top 10 vendors.
<img width="1492" height="490" alt="image" src="https://github.com/user-attachments/assets/6d04188d-a32e-4db6-a812-11f5afbc4879" />
This image demonstrates that a small vendor set drives most of the purchase volume, creating dependency risk.

**Brand Margin vs Volume Behavior**\
The plot below shows brand-level margin against volume, identifying brands with low volume but high profitability potential.
<img width="1181" height="590" alt="image" src="https://github.com/user-attachments/assets/00f9caff-3fb3-4867-b4e1-38abdd7d2497" />
Brands in the top-left region represent targets for promotional intervention or pricing adjustments.

**Bulk Purchasing Unit Cost Comparison**\
This visualization compares unit purchase cost for large versus small order quantities.
<img width="1061" height="667" alt="image" src="https://github.com/user-attachments/assets/68f3846d-0806-4e24-9b9b-ceacd2863df2" />
The unit cost reduction supports procurement strategies that leverage quantity-driven discounts.

**Inventory Turnover and Unsold Capital**\
The chart below illustrates inventory turnover behavior and capital locked in slow-moving stock.
![Unsold Inventory Capital](unsold_inventory_capital.png)
This represents approximately $2.71M in working capital tied up in unsold stock.

**Margin Distribution Across Vendor Segments**\
This visualization shows statistical margin distribution for high-volume vs low-volume vendors.
<img width="1005" height="547" alt="image" src="https://github.com/user-attachments/assets/3b77a82d-1c35-4b38-a594-eb5c6e07c669" />
The lower distribution for high-volume vendors confirms volume-over-margin sales models.

**Statistical Validation Summary**\
A summary visualization or table shows margin confidence intervals and hypothesis test results.
<img width="1496" height="990" alt="image" src="https://github.com/user-attachments/assets/a43078e6-d8cf-4d3f-b1b5-84b6a9176e3f" />

This supports the finding that the vendor groups operate under distinct profitability models.

## 7. Business Questions Answered

Examples of questions addressed:

- Which brands require promotional or pricing adjustments?
- Which vendors contribute most to purchase volume?
- Does bulk purchasing provide financial benefit?
- How much capital is locked in slow-moving inventory?
- Do high-performing vendors share the same profit model as low-performing vendors?
- How do pricing changes affect margins?
- Does turnover speed correlate with profitability?

Each of these is supported by metrics, visuals, or statistical evidence in the repository notebooks.

## 8. Notebooks Included

The core analysis is contained in:

- EDA.ipynb
- Vendor_performance_Analysis.ipynb

These notebooks contain metric computation, joins, segmentation logic, statistical tests, and visual output.

## 9. Technologies Used

The environment uses:

- Python 3.x
- Pandas, NumPy for data processing
- Matplotlib / Seaborn / Plotly for visualization
- SciPy / Statsmodels for statistical testing
- Jupyter Notebook for interactive analysis

## 10. Relevance and Use Cases

This work is relevant for:

- Vendor management teams
- Category managers
- Pricing analysts
- Merchandising
- FP&A and supply chain
- BI teams

The findings support decisions in vendor diversification, promotional planning, pricing optimization, procurement strategy, and inventory control.

## 11. Current Status and Next Steps

Extensions include:

- Automated vendor scoring
- Predictive demand models
- Dashboard port to BI platforms
- Integration with procurement or POS systems
