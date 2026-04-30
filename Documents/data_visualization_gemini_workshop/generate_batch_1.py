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

# 2. Households Scatter
def plot_households():
    df = pd.read_csv('households_scatter.csv')
    setup_style()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x='population', y='avg_hh', size='households', sizes=(20, 1000), alpha=0.6, ax=ax)
    
    # Label a few major countries
    for i in range(len(df)):
        if df.country.iloc[i] in ['India', 'China', 'United States', 'Nigeria']:
            ax.text(df.population.iloc[i], df.avg_hh.iloc[i]+0.1, df.country.iloc[i], fontsize=9)
            
    ax.set_xscale('log')
    finalize_plot(ax, "Population vs. Average Household Size", "Avg. Household Size", "Total Population (Log Scale)", "households_scatter.csv", "viz/population-household-size/viz.png")

# 3. Japan Prefecture Bump
def plot_japan():
    df = pd.read_csv('japan_prefecture_bump.csv')
    # Filter for Overall purpose and specific years
    df = df[df['Purpose'] == 'Overall']
    df['Overnight Stays'] = df['Overnight Stays'].str.replace(',', '').astype(float)
    
    # Focus on top regions or specifically Aichi
    top_regions = df.groupby('Item1')['Overnight Stays'].sum().nlargest(5).index.tolist()
    if 'Aichi' not in top_regions:
        top_regions.append('Aichi')
    
    df_plot = df[df['Item1'].isin(top_regions)]
    
    setup_style()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=df_plot, x='Year', y='Overnight Stays', hue='Item1', marker='o', ax=ax)
    
    finalize_plot(ax, "Growth of Overnight Stays in Top Japanese Prefectures", "Overnight Stays", "Year", "japan_prefecture_bump.csv", "viz/japan-overnight-stays/viz.png")

# 4. Job Participation
def plot_jobs():
    df = pd.read_csv('jobs_by_age_sex.csv')
    # Reshape for seaborn
    # Characteristic is Total, Men, Women.
    # We want participation rates by Age and Gender.
    df_melt = df.melt(id_vars=['Characteristic'], var_name='Age Group', value_name='Rate')
    df_melt = df_melt[df_melt['Characteristic'].isin(['Men', 'Women'])]
    df_melt = df_melt[df_melt['Age Group'] != 'Total ']
    
    setup_style()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df_melt, x='Age Group', y='Rate', hue='Characteristic', palette={'Men': '#3498db', 'Women': '#e74c3c'}, ax=ax)
    
    finalize_plot(ax, "Job Participation Rates by Gender and Age", "Participation Rate (%)", "Age Group", "jobs_by_age_sex.csv", "viz/job-participation/viz.png")

if __name__ == "__main__":
    plot_households()
    plot_japan()
    plot_jobs()
