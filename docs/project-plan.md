# 🗓️ One-Week Build Plan

## Day 1 — Setup & Exploration
- Install Power BI Desktop
- Load `retail_sales_data.csv` via Get Data → Text/CSV
- Explore each column, check data types
- Note questions you want the dashboard to answer

## Day 2 — Data Cleaning (Power Query)
- Open Power Query Editor (Home → Transform Data)
- Confirm `Order_Date` / `Ship_Date` are typed as Date
- Confirm `Sales`, `Profit`, `Discount` are typed as Decimal Number
- Check for duplicates or blanks (there shouldn't be many — this is a clean synthetic dataset, but practice the checks anyway)
- Add a calculated column: `Shipping_Days = Ship_Date - Order_Date`

## Day 3 — Data Modeling
- Create a dedicated **Date table** using DAX:
  ```DAX
  DateTable = CALENDAR(MIN(retail_sales_data[Order_Date]), MAX(retail_sales_data[Order_Date]))
  ```
- Add Year, Month, Month Name, Quarter columns to the Date table
- Mark it as a Date Table (Table tools → Mark as Date Table)
- Relate `DateTable[Date]` → `retail_sales_data[Order_Date]`

## Day 4 — DAX Measures
See [`dax-measures.md`](dax-measures.md) for the full list. Build:
- Total Sales, Total Profit, Total Orders
- Profit Margin %
- Average Order Value
- Year-over-Year Sales Growth

## Day 5 — Core Visuals
- KPI cards: Total Sales, Total Profit, Total Orders, Profit Margin %
- Line chart: Sales trend by month
- Bar chart: Sales by Category / Sub-Category
- Bar chart: Profit by Region
- Table: Top 10 customers by Sales

## Day 6 — Interactivity & Polish
- Add slicers: Date range, Region, Category, Segment
- Add tooltips showing Profit when hovering over Sales bars
- Apply a consistent color theme (View → Themes)
- Align visuals to a grid, add a title and page background

## Day 7 — Review & Presentation
- Write 3–5 key insights you found (e.g., "Technology has the highest sales but thinnest margin")
- Export as PDF (File → Export → PDF)
- If using Power BI Service, publish and share the link
- Prepare a short walkthrough explaining your findings
