import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Load data
file_path = '/Users/pattarawatdhanespramoj/Documents/data_visualization_gemini_workshop/state_migration_balance.xlsx'
df = pd.read_excel(file_path, sheet_name='California movement')

# Filter and Sort
df_filtered = df[(df['From'] == 'California') & (df['To'] != 'California')]
df_top10 = df_filtered.sort_values(by='Population movement', ascending=False).head(10)

# Styling
sns.set_theme(style="white", font='DejaVu Sans')
color = '#4a7c9d' # Restrained blue

fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

# Plot
bars = sns.barplot(
    data=df_top10,
    x='Population movement',
    y='To',
    color=color,
    ax=ax
)

# Titles
fig.suptitle('The California Exodus: Texas is the Top Destination', 
             fontsize=16, fontweight='bold', x=0.125, ha='left')
ax.set_title('Migration from California to other US states in 2023', 
             fontsize=12, pad=20, loc='left', color='#555555')

# Remove axis labels and clean up
ax.set_xlabel('')
ax.set_ylabel('')
sns.despine(left=True, bottom=True)
ax.set_xticks([]) # Remove x-axis ticks as we have direct labels

# Direct labels
for i, p in enumerate(ax.patches):
    width = p.get_width()
    ax.text(
        width + 1000, 
        i, 
        f'{int(width):,}', 
        va='center', 
        fontsize=10, 
        fontweight='bold',
        color='#333333'
    )

# Source text
fig.text(0.125, 0.02, 'Source: US Census Bureau, State-to-State Migration Flows 2023', 
         fontsize=8, color='#888888', ha='left')

plt.tight_layout(rect=[0, 0.05, 1, 0.95])

# Export
output_path = '/Users/pattarawatdhanespramoj/Documents/data_visualization_gemini_workshop/viz/california-exodus/viz.png'
plt.savefig(output_path, bbox_inches='tight')
print(f"Visualization saved to {output_path}")
