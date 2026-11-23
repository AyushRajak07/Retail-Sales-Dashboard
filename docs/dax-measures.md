# 📐 DAX Measures Reference

Create these as **Measures** (Modeling → New Measure), not calculated columns, unless noted otherwise.

## Core Measures

```DAX
Total Sales = SUM(retail_sales_data[Sales])

Total Profit = SUM(retail_sales_data[Profit])

Total Orders = DISTINCTCOUNT(retail_sales_data[Order_ID])

Total Quantity = SUM(retail_sales_data[Quantity])
```

## Ratios & Averages

```DAX
Profit Margin % = DIVIDE([Total Profit], [Total Sales])

Average Order Value = DIVIDE([Total Sales], [Total Orders])

Average Discount = AVERAGE(retail_sales_data[Discount])
```

## Time Intelligence
(Requires the `DateTable` from the project plan, related on Order_Date)

```DAX
Sales PY =
CALCULATE([Total Sales], SAMEPERIODLASTYEAR(DateTable[Date]))

YoY Sales Growth % =
DIVIDE([Total Sales] - [Sales PY], [Sales PY])

Sales MTD =
TOTALMTD([Total Sales], DateTable[Date])

Sales YTD =
TOTALYTD([Total Sales], DateTable[Date])
```

## Ranking & Top N

```DAX
Customer Sales Rank =
RANKX(ALL(retail_sales_data[Customer_ID]), [Total Sales])
```

## Tips
- Always use `DIVIDE()` instead of `/` to avoid divide-by-zero errors.
- Keep measures organized in a dedicated "Measures" table for cleanliness (optional but good practice).
- Format measures appropriately (currency for Sales/Profit, percentage for ratios).
