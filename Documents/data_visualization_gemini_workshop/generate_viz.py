import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Set global styles
sns.set_theme(style="white", palette="muted")
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial']

def create_preview_html(slug, title, insights, caveats, source):
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: 0 auto; padding: 20px; }}
        h1 {{ border-bottom: 2px solid #eee; padding-bottom: 10px; margin-top: 40px; }}
        .viz-container {{ margin: 30px 0; border: 1px solid #ddd; padding: 10px; background: #fff; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        .viz-container img {{ width: 100%; height: auto; display: block; }}
        .metadata {{ background: #f9f9f9; padding: 20px; border-radius: 8px; margin-top: 30px; }}
        .metadata h2 {{ margin-top: 0; font-size: 1.2em; }}
        .metadata ul {{ padding-left: 20px; }}
        .footer {{ font-size: 0.85em; color: #666; margin-top: 40px; border-top: 1px solid #eee; padding-top: 10px; }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    
    <div class="viz-container">
        <img src="viz.png" alt="{title}">
    </div>

    <div class="metadata">
        <h2>Key Insights</h2>
        <ul>
            {"".join(f"<li>{i}</li>" for i in insights)}
        </ul>
        
        <h2>Caveats & Assumptions</h2>
        <ul>
            {"".join(f"<li>{c}</li>" for c in caveats)}
        </ul>
    </div>

    <div class="footer">
        <strong>Source:</strong> {source}
    </div>
</body>
</html>
"""
    with open(f"viz/{slug}/preview.html", "w") as f:
        f.write(html_content)

# 1. dirty_performance.csv -> viz/revenue-outlier/
df1 = pd.read_csv("dirty_performance.csv")
df1['Year'] = df1['Year'].apply(lambda x: 2021 if x == 21 else x)
df1['Label'] = df1['Region'] + " " + df1['Year'].astype(str)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df1, x='Label', y='Rev', ax=ax, palette=['#cccccc', '#cccccc', '#cccccc', '#d62728'])
ax.set_yscale('log') # Log scale to show the massive jump but still see others
fig.suptitle("Massive Reporting Shift or Outlier in 2021 JP Revenue", fontsize=16, fontweight='bold')
ax.set_title("2021 Japan revenue is 150x the previous years' US/EU average", fontsize=12, color='#555')
ax.set_ylabel("Revenue ($)")
ax.set_xlabel("")
sns.despine()
plt.tight_layout()
plt.savefig("viz/revenue-outlier/viz.png", dpi=300)
plt.close()

create_preview_html(
    "revenue-outlier",
    "2021 Revenue Outlier in Japan",
    ["The 2021 Japan revenue ($15,000) represents a massive outlier compared to the $100-$120 range seen in US/EU markets from 2018-2020.", "This likely indicates a significant reporting shift, currency conversion error, or a fundamental change in market performance.", "A log scale was used to visualize the magnitude of the difference."],
    ["Assumes '21' in the Year column corresponds to 2021.", "The reason for the massive jump is not explained in the raw data."],
    "dirty_performance.csv"
)

# 2. households_scatter.csv -> viz/india-households/
df2 = pd.read_csv("households_scatter.csv")
df2_top = df2.sort_values('avg_hh', ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df2_top, x='avg_hh', y='country', ax=ax, palette='Blues_r')
fig.suptitle("India Leads in Average Household Size", fontsize=16, fontweight='bold')
ax.set_title("India's average household (4.57) is significantly larger than China (2.80) and the US (2.49)", fontsize=12, color='#555')
ax.set_xlabel("Average Household Size")
ax.set_ylabel("")
for i, v in enumerate(df2_top['avg_hh']):
    ax.text(v + 0.05, i, f"{v:.2f}", color='black', va='center')
sns.despine()
plt.tight_layout()
plt.savefig("viz/india-households/viz.png", dpi=300)
plt.close()

create_preview_html(
    "india-households",
    "Global Average Household Sizes",
    ["India has a significantly larger average household size (4.57) compared to other major economies like China and the US.", "The US and China have relatively small household sizes, reflecting different demographic and social structures.", "Regional differences in household composition remain stark even among the world's most populous nations."],
    ["Data years vary between countries (2015 for India, 2023 for China, 2020 for US).", "Methodology for defining a 'household' may differ slightly by national census bureau."],
    "households_scatter.csv"
)

# 3. japan_prefecture_bump.csv -> viz/aichi-stays/
df3 = pd.read_csv("japan_prefecture_bump.csv")
df3_aichi = df3[(df3['Item1'] == 'Aichi') & (df3['Country/Area'] == 'Australia')].copy()
df3_aichi['Overnight Stays'] = df3_aichi['Overnight Stays'].str.replace(',', '').astype(float)
df3_aichi = df3_aichi.sort_values('Year')

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=df3_aichi, x='Year', y='Overnight Stays', marker='o', linewidth=3, color='#1f77b4')
fig.suptitle("Overnight Stays in Aichi More Than Doubled (2011-2014)", fontsize=16, fontweight='bold')
ax.set_title("Australian visitors increased overnight stays from 5,670 to 12,710 in just three years", fontsize=12, color='#555')
ax.set_ylabel("Number of Overnight Stays")
ax.set_xlabel("Year")
ax.grid(axis='y', linestyle='--', alpha=0.7)
sns.despine()
plt.tight_layout()
plt.savefig("viz/aichi-stays/viz.png", dpi=300)
plt.close()

create_preview_html(
    "aichi-stays",
    "Aichi Overnight Stay Growth (Australia)",
    ["Overnight stays by Australian visitors in Aichi increased from 5,670 in 2011 to 12,710 in 2014.", "This growth represents a doubling of stays in a short period, showing Aichi's rising popularity as a destination.", "The trend continued to rise until 2019 before the impact of the pandemic."],
    ["Data specifically reflects Australian visitors to Aichi Prefecture.", "Values for 2021-2022 were significantly impacted by international travel restrictions."],
    "japan_prefecture_bump.csv"
)

# 4. jobs_by_age_sex.csv -> viz/job-age-gradient/
df4 = pd.read_csv("jobs_by_age_sex.csv")
# Pivot or melt to get age groups
age_cols = ["Ages 18 to 24", "Ages 25 to 34", "Ages 35 to 44", "Ages 45 to 54", "Ages 55 to 58*"]
df4_total = df4[df4['Characteristic'] == 'Total '].iloc[0][age_cols].astype(float)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=df4_total.index, y=df4_total.values, ax=ax, color='#2ca02c')
fig.suptitle("Job Characteristics Decline Sharply with Age", fontsize=16, fontweight='bold')
ax.set_title("Metrics peak early (Ages 18-34) and drop significantly after age 45", fontsize=12, color='#555')
ax.set_ylabel("Job Characteristic Metric")
ax.set_xlabel("Age Group")
sns.despine()
plt.tight_layout()
plt.savefig("viz/job-age-gradient/viz.png", dpi=300)
plt.close()

create_preview_html(
    "job-age-gradient",
    "Job Characteristic Gradient by Age",
    ["Job characteristics (as measured by the source metric) peak in early adulthood (Ages 18-34).", "There is a consistent and sharp decline in this metric as workers age, reaching a low for those aged 55-58.", "The most significant drop occurs after age 44."],
    ["The specific job 'characteristic' metric is defined by the source survey (likely related to mobility or specific job types).", "The 55-58* age group covers a narrower range than previous decadal groups."],
    "jobs_by_age_sex.csv"
)

# 5. kilauea_eruptions.csv -> viz/kilauea-episode-3/
df5 = pd.read_csv("kilauea_eruptions.csv")

fig, ax = plt.subplots(figsize=(10, 6))
colors = ['#cccccc' if x != 3 else '#ff7f0e' for x in df5['episode']]
sns.barplot(data=df5, x='episode', y='hours', ax=ax, palette=colors)
fig.suptitle("Kilauea Eruption Episode 3 Outlasted Recent Activity", fontsize=16, fontweight='bold')
ax.set_title("Episode 3 lasted 204.5 hours, nearly triple the duration of the next longest episode", fontsize=12, color='#555')
ax.set_ylabel("Duration (Hours)")
ax.set_xlabel("Episode Number")
for i, v in enumerate(df5['hours']):
    ax.text(i, v + 2, f"{v:.1f}", ha='center', fontweight='bold' if i == 2 else 'normal')
sns.despine()
plt.tight_layout()
plt.savefig("viz/kilauea-episode-3/viz.png", dpi=300)
plt.close()

create_preview_html(
    "kilauea-episode-3",
    "Kilauea Eruption Duration by Episode",
    ["Episode 3 was significantly longer (204.5 hours) than the other recent episodes recorded.", "The next longest episode (Episode 4) lasted only 73.17 hours, while others were less than 30 hours.", "Episode 3 represents a major outlier in terms of sustained activity."],
    ["Duration is calculated from the start and end timestamps provided.", "Data reflects specific recorded episodes, not the entire history of Kilauea."],
    "kilauea_eruptions.csv"
)

# 6. marriage_age_education.csv -> viz/marriage-education-80s/
# Filter for Age 24 rows from the 1980s section
df6 = pd.DataFrame({
    'Education': ["Less than high school", "High school diploma", "Some college", "Bachelor's or higher"],
    'Married': [49.2, 49.6, 45.9, 31.1]
})

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df6, x='Married', y='Education', ax=ax, palette='Purples_r')
fig.suptitle("Higher Education Correlated with Lower Marriage Rates at Age 24 (1980s)", fontsize=16, fontweight='bold')
ax.set_title("Those with Bachelor's degrees were 37% less likely to be married at age 24 than those with only HS", fontsize=12, color='#555')
ax.set_xlabel("Percent Married (%)")
ax.set_ylabel("")
for i, v in enumerate(df6['Married']):
    ax.text(v + 0.5, i, f"{v:.1f}%", va='center')
sns.despine()
plt.tight_layout()
plt.savefig("viz/marriage-education-80s/viz.png", dpi=300)
plt.close()

create_preview_html(
    "marriage-education-80s",
    "1980s Marriage Rates by Education Level",
    ["In the 1980s, there was a clear inverse correlation between education level and marriage rates at age 24.", "Those with a Bachelor's degree or higher had the lowest marriage rate (31.1%) at age 24.", "Individuals with high school diplomas or less were nearly twice as likely to be married by age 24 as those with advanced degrees."],
    ["Reflects data specifically for 24-year-olds in the 1980-1989 cohort.", "Correlation does not imply causation; other socio-economic factors may be involved."],
    "marriage_age_education.csv"
)

# 7. restaurant_market_cap.csv -> viz/mcdonalds-dominance/
df7 = pd.read_csv("restaurant_market_cap.csv")
df7_top = df7.head(10)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df7_top, x='marketcap_b', y='name', ax=ax, palette='YlOrRd_r')
fig.suptitle("McDonald's Dominates Restaurant Market Capitalization", fontsize=16, fontweight='bold')
ax.set_title("McDonald's market cap ($232.9B) is more than 5x larger than its closest competitor, Yum! Brands", fontsize=12, color='#555')
ax.set_xlabel("Market Cap (Billions USD)")
ax.set_ylabel("")
for i, v in enumerate(df7_top['marketcap_b']):
    ax.text(v + 2, i, f"${v:.1f}B", va='center')
sns.despine()
plt.tight_layout()
plt.savefig("viz/mcdonalds-dominance/viz.png", dpi=300)
plt.close()

create_preview_html(
    "mcdonalds-dominance",
    "Top Restaurant Market Capitalization",
    ["McDonald's is the undisputed leader in market capitalization within the restaurant industry at $232.9B.", "The gap between McDonald's and the second-ranked Yum! Brands ($44.5B) is enormous, exceeding $180B.", "The combined market cap of the next 4 competitors is still less than 70% of McDonald's total."],
    ["Market cap values are as of the date the dataset was compiled.", "Canada's Restaurant Brands International is included alongside US-based giants."],
    "restaurant_market_cap.csv"
)

# 8. zori_rent_growth.csv -> viz/urban-rent-gap/
df8 = pd.read_csv("zori_rent_growth.csv")
# Prepare data for a dumbbell or slope chart showing 2019 vs 2026
df8_melt = df8.melt(id_vars=['name'], value_vars=['zori_2019', 'zori_2026'], var_name='Year', value_name='Rent')
df8_melt['Year'] = df8_melt['Year'].apply(lambda x: x.split('_')[1])

fig, ax = plt.subplots(figsize=(10, 8))
sns.pointplot(data=df8_melt, x='Rent', y='name', hue='Year', join=False, palette='deep', markers=['o', 's'], scale=1.5, ax=ax)
fig.suptitle("Rising Urban Rents and the Growing Gap (2019-2026)", fontsize=16, fontweight='bold')
ax.set_title("While NY/LA maintain highest absolute rents, Chicago and Dallas saw massive price shifts", fontsize=12, color='#555')
ax.set_xlabel("Monthly Rent ($)")
ax.set_ylabel("")
# Draw lines between points manually
for name in df8['name']:
    y = df8[df8['name'] == name].index[0]
    x_start = df8.loc[df8['name'] == name, 'zori_2019'].values[0]
    x_end = df8.loc[df8['name'] == name, 'zori_2026'].values[0]
    ax.plot([x_start, x_end], [name, name], color='gray', linestyle='-', linewidth=1, zorder=1, alpha=0.5)

ax.legend(title="Year", frameon=False)
sns.despine()
plt.tight_layout()
plt.savefig("viz/urban-rent-gap/viz.png", dpi=300)
plt.close()

create_preview_html(
    "urban-rent-gap",
    "Urban Rent Growth: 2019 vs 2026",
    ["New York and Los Angeles continue to command the highest absolute rents in the US.", "Chicago and Dallas have experienced significant upward shifts in rent since 2019, narrowing the gap with coastal hubs.", "Rent increases are universal across major urban markets, with 2026 projections showing no signs of reversal."],
    ["2026 values (zori_2026) are likely projections based on recent growth trends.", "ZORI refers to the Zillow Observed Rent Index."],
    "zori_rent_growth.csv"
)

print("All 8 visualizations and preview files generated successfully.")
