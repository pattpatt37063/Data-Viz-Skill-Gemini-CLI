import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def setup_style():
    sns.set_theme(style="whitegrid", font="Arial")
    plt.rcParams['figure.dpi'] = 300
    plt.rcParams['savefig.dpi'] = 300

def finalize_plot(ax, title, ylabel, xlabel, source, filename):
    ax.set_title(title, loc='left', fontsize=16, fontweight='bold', pad=20)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_xlabel(xlabel, fontsize=12)
    sns.despine(left=True, bottom=False)
    plt.figtext(0.1, 0.02, f"Source: {source}", fontsize=8, alpha=0.7)
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    plt.savefig(filename)
    plt.close()

# 5. Kilauea Eruptions
def plot_kilauea():
    df = pd.read_csv('kilauea_eruptions.csv')
    df['start'] = pd.to_datetime(df['start'])
    
    setup_style()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=df, x='start', y='hours', marker='o', color='#c0392b', ax=ax)
    
    finalize_plot(ax, "Duration of Kilauea Eruption Episodes", "Duration (Hours)", "Start Date", "kilauea_eruptions.csv", "viz/kilauea-eruptions/viz.png")

# 6. Marriage Education
def plot_marriage():
    df = pd.read_csv('marriage_age_education.csv')
    # Focus on "Married" rate
    # Filter rows that are actual education levels (ignore the first one which is total)
    df = df[1:] 
    df['Married'] = df['Married'].astype(float)
    
    setup_style()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df, x='Married', y='Characteristic', palette="viridis", ax=ax)
    
    finalize_plot(ax, "Marriage Rates by Education Level (Age 24)", "Education Level", "Marriage Rate (%)", "marriage_age_education.csv", "viz/marriage-education/viz.png")

# 7. Restaurant Market Cap
def plot_restaurants():
    df = pd.read_csv('restaurant_market_cap.csv')
    
    setup_style()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df, x='marketcap_b', y='name', palette="rocket", ax=ax)
    
    finalize_plot(ax, "Top Restaurant Chains by Market Capitalization", "Chain Name", "Market Cap (USD Billion)", "restaurant_market_cap.csv", "viz/restaurant-market-cap/viz.png")

# 8. Rent Growth
def plot_rent():
    df = pd.read_csv('zori_rent_growth.csv')
    # Slope chart-ish: 2019 to 2026
    df_plot = df[['name', 'zori_2019', 'zori_2026']].copy()
    df_plot = df_plot.melt(id_vars='name', var_name='Year', value_name='Rent')
    df_plot['Year'] = df_plot['Year'].str.replace('zori_', '')
    
    setup_style()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.lineplot(data=df_plot, x='Year', y='Rent', hue='name', marker='o', ax=ax)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
    
    finalize_plot(ax, "Projected Rent Growth in U.S. Metros (2019–2026)", "Average Monthly Rent (USD)", "Year", "zori_rent_growth.csv", "viz/rent-growth/viz.png")

if __name__ == "__main__":
    plot_kilauea()
    plot_marriage()
    plot_restaurants()
    plot_rent()
