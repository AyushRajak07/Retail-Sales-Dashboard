# 📊 Retail Sales Dashboard — Power BI Project

A beginner-friendly Power BI project built in one week. It covers data cleaning, modeling, DAX measures, and interactive dashboard design using a synthetic retail sales dataset.

![Status](https://img.shields.io/badge/status-complete-brightgreen)
![Tool](https://img.shields.io/badge/tool-Power%20BI-yellow)
![Level](https://img.shields.io/badge/level-beginner-blue)

---

## 🎯 Project Goal

Analyze retail sales data to answer core business questions:

- What are our total sales and profit, and how are they trending over time?
- Which regions, categories, and sub-categories perform best?
- How does discounting affect profit margins?
- Who are our top customers and products?

---

## 🗂️ Repository Structure

```
retail-sales-dashboard/
├── data/
│   ├── generate_data.py        # Script to generate the sample dataset
│   └── retail_sales_data.csv   # Sample dataset (3,000 orders, 2023–2025)
├── docs/
│   ├── project-plan.md         # Day-by-day 1-week build plan
│   └── dax-measures.md         # All DAX measures used, explained
├── screenshots/
│   └── (dashboard screenshots go here)
├── RetailSalesDashboard.pbix   # Power BI file (add after building locally)
└── README.md
```

> **Note:** Power BI Desktop files (`.pbix`) are binary and can't be created outside of Power BI Desktop itself. This repo includes everything you need (dataset + instructions) to build the `.pbix` yourself in Power BI Desktop, then commit it here.

---

## 📁 Dataset

`data/retail_sales_data.csv` — 3,000 synthetic retail orders (2023–2025) with:

| Column | Description |
|---|---|
| Order_ID | Unique order identifier |
| Order_Date / Ship_Date | Dates for time intelligence |
| Ship_Mode | Shipping method |
| Customer_ID | Customer identifier |
| Segment | Consumer / Corporate / Home Office |
| Region / City | Geography |
| Category / Sub_Category | Product hierarchy |
| Quantity | Units sold |
| Sales | Revenue after discount |
| Discount | Discount rate applied |
| Profit | Profit earned on the order |

Regenerate or modify the dataset anytime:
```bash
cd data
python generate_data.py
```

---

## 🛠️ How to Build This Project

1. **Install** [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (free, Windows only).
2. **Import data**: Get Data → Text/CSV → select `retail_sales_data.csv`.
3. Follow the day-by-day build plan in [`docs/project-plan.md`](docs/project-plan.md).
4. Use the measures in [`docs/dax-measures.md`](docs/dax-measures.md) to build your KPIs.
5. Save your `.pbix` file in the repo root and push it to GitHub (use [Git LFS](https://git-lfs.com/) if the file is large).
6. Export dashboard screenshots into `screenshots/` and link them below.

---

## 📈 Dashboard Preview

> Add screenshots here once you've built your dashboard.

```
screenshots/overview.png
screenshots/sales-by-region.png
screenshots/profitability.png
```

---

## 🧠 Skills Demonstrated

- Power Query — data cleaning & transformation
- Data modeling — star schema, relationships, date tables
- DAX — measures, time intelligence, calculated columns
- Data visualization — KPI cards, trend lines, maps, matrices
- Dashboard UX — slicers, tooltips, consistent theming

---

## 📄 License

This project uses synthetic data generated for educational purposes. Free to use, modify, and share.
