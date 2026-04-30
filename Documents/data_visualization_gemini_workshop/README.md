# Storytelling Data Visualization with Python & Gemini

This repository contains a collection of Python scripts, datasets, and a specialized AI "skill" designed to transform raw data into polished, story-driven static visualizations using **Seaborn** and **Matplotlib**.

## Overview

The goal of this project is to implement a **story-first workflow**. Instead of just plotting data, we focus on:
- **Storytelling**: Each chart must have a clear, one-sentence takeaway.
- **Intuition**: A first-time viewer should understand the main claim quickly without needing to hover or read complex legends.
- **Concision**: Removing unnecessary elements to sharpen the focus.
- **Honesty**: Ensuring the framing matches the actual data, scope, and caveats.

## Contents

- **`storytelling-viz-python/`**: The core skill repository containing:
  - `SKILL.md`: Canonical instructions for the AI assistant.
  - `scripts/`: Helper scripts for visualization.
  - `references/`: Style guides and pattern libraries.
- **`generate_viz.py` & `generate_*.py`**: Python scripts to automate the creation of high-quality charts.
- **`viz/`**: Directory for generated artifacts (PNG/SVG visualizations and HTML previews).
- **Data**: Various CSV and XLSX datasets covering migration, demographics, market trends, and more.

## Key Features

- **Automated QA**: Built-in checks for clipping, overlap, and label readability.
- **Local Review Artifacts**: Generates `viz.png` and a `preview.html` wrapper for immediate stakeholder review.
- **Editorial Styling**: Focuses on professional, presentation-ready aesthetics with restrained color palettes and clear hierarchies.

## Getting Started

1. Ensure you have Python installed with `seaborn`, `matplotlib`, and `pandas`.
2. Run any of the `generate_*.py` scripts to see the workflow in action.
3. Use the `storytelling-viz-python` skill with a compatible AI assistant to build your own story-driven charts.

---
*Created for the Data Visualization Gemini Workshop.*
