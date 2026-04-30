# Shared Seaborn and Matplotlib Patterns

Use these defaults unless the dataset needs something more specific:

- high resolution (e.g., `dpi=300`) for all exports
- prominent title using `fig.suptitle()` and supporting subtitle using `ax.set_title()` (or a second `suptitle` call with smaller font)
- concise source line using `fig.text()` at the bottom
- tight or constrained layout to minimize unused whitespace
- consistent figure sizes (e.g., `figsize=(10, 6)`)
- font selection that favors readability (e.g., sans-serif like 'DejaVu Sans' or 'Arial')
- color palettes defined via `sns.set_palette()` or specific hex codes
- direct labeling of data points using `ax.annotate()` or `ax.text()` instead of heavy legends
- minimalist axis lines using `sns.despine()`
