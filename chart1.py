import matplotlib.pyplot as plt
import numpy as np
import os

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Define the categories (geographic regions)
regions = ['United States', 'Istanbul', 'Other', 'Yemen', 'China', 'Great Britain']
num_regions = len(regions)

# Data for each business unit (number of cases per region)
business_unit_1 = [4, 12, 16, 3, 1, 5]
business_unit_2 = [12, 8, 19, 9, 2, 13]
business_unit_3 = [6, 15, 5, 9, 13, 2]

# Calculate totals
total_1 = sum(business_unit_1)
total_2 = sum(business_unit_2)
total_3 = sum(business_unit_3)

# Business units (divisions) - these will be the bars
divisions = ['Business Unit 1', 'Business Unit 2', 'Business Unit 3']
x_pos = np.arange(len(divisions))

# Organize data by region for stacking
# Each row represents a region, columns are business units
data = np.array([
    [business_unit_1[i], business_unit_2[i], business_unit_3[i]]
    for i in range(num_regions)
])

# Colors for each region
colors = ['#DC3545', '#FF8C00', '#4A90E2', '#28A745', '#9B59B6', '#17A2B8']

# Create stacked bars
bar_width = 0.6
bottom = np.zeros(len(divisions))

bars = []
for i, (region_data, color) in enumerate(zip(data, colors)):
    bar = ax.bar(x_pos, region_data, bar_width, bottom=bottom,
                 label=regions[i], color=color, edgecolor='white', linewidth=1.5)
    bars.append(bar)
    bottom += region_data

# Customize the chart
ax.set_ylabel('Number of Cases', fontsize=14, weight='bold')
ax.set_xlabel('Business Units', fontsize=14, weight='bold')
ax.set_title('Regional Impact Profile\nNew Incidents by Business Unit',
             fontsize=20, weight='bold', pad=20)

# Set x-axis labels
ax.set_xticks(x_pos)
ax.set_xticklabels([f'{div}\n(Total: {total})'
                     for div, total in zip(divisions, [total_1, total_2, total_3])],
                    fontsize=12, weight='bold')

# Add grid
ax.grid(True, axis='y', linestyle='--', linewidth=0.7, alpha=0.5, zorder=0)
ax.set_axisbelow(True)

# Add legend
legend = ax.legend(loc='upper right', frameon=True, fontsize=11,
                   fancybox=True, shadow=True, ncol=2)
legend.get_frame().set_facecolor('white')
legend.get_frame().set_edgecolor('gray')
legend.get_frame().set_linewidth(1.5)

# Adjust layout
plt.tight_layout()

# Create outputs directory if it doesn't exist
output_dir = 'outputs'
os.makedirs(output_dir, exist_ok=True)

# Save the figure
output_path = os.path.join(output_dir, 'business_unit_cases_by_region.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')

print("Stacked bar chart created successfully!")
print(f"Saved to: {output_path}")

# Display the plot
plt.show()
