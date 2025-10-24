import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import os

# Set up the figure and axis
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='polar')

# Define the categories (geographic regions)
categories = ['United States', 'Instanbul', 'Other', 'Yemen', 'China', 'Great Britain']
num_vars = len(categories)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the circle

# Data for each business unit (number of cases per region)
business_unit_1 = [4, 12, 16, 3, 1, 5]
business_unit_2 = [12, 8, 19, 9, 2, 13]
business_unit_3 = [6, 15, 5, 9, 13, 2]

# Calculate totals and rank
total_1 = sum(business_unit_1)
total_2 = sum(business_unit_2)
total_3 = sum(business_unit_3)

# Find max value for scaling
max_value = max(max(business_unit_1), max(business_unit_2), max(business_unit_3))

# Complete the circle for each dataset
business_unit_1 += business_unit_1[:1]
business_unit_2 += business_unit_2[:1]
business_unit_3 += business_unit_3[:1]

# Plot data with rankings
ax.plot(angles, business_unit_2, 'o-', linewidth=2.5, label=f'Business Unit 2 (Total: {total_2})', color='#FF8C00', markersize=8)
ax.fill(angles, business_unit_2, alpha=0.15, color='#FF8C00')

ax.plot(angles, business_unit_3, 'o-', linewidth=2.5, label=f'Business Unit 3 (Total: {total_3})', color='#4A90E2', markersize=8)
ax.fill(angles, business_unit_3, alpha=0.15, color='#4A90E2')

ax.plot(angles, business_unit_1, 'o-', linewidth=2.5, label=f'Business Unit 1 (Total: {total_1})', color='#DC3545', markersize=8)
ax.fill(angles, business_unit_1, alpha=0.15, color='#DC3545')

# Fix axis to go in the right order and start at 12 o'clock
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Set the labels for each axis
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=18, weight='bold')

# Set y-axis limits and labels to accommodate case numbers
y_max = int(np.ceil(max_value / 5) * 5)  # Round up to nearest increment
ax.set_ylim(0, y_max)

# Create evenly spaced ticks
num_ticks = 5
tick_values = np.linspace(0, y_max, num_ticks)
ax.set_yticks(tick_values)
ax.set_yticklabels([f'{int(v)}' for v in tick_values], size=16, color='gray')

# Add grid
ax.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Add title
plt.title('Regional Impact Profile\nNew Incidents by Business Unit',
          size=24, weight='bold', pad=20, loc='center')

# Add legend
legend = ax.legend(loc='upper right', bbox_to_anchor=(1.3, 0.95),
                   frameon=True, fontsize=11,
                   markerscale=1.2, fancybox=True, shadow=True)
legend.get_frame().set_facecolor('white')
legend.get_frame().set_edgecolor('gray')
legend.get_frame().set_linewidth(1.5)

# Adjust layout to prevent label cutoff
plt.tight_layout()
plt.subplots_adjust(top=0.85, bottom=0.05)

# Create outputs directory if it doesn't exist
output_dir = 'outputs'
os.makedirs(output_dir, exist_ok=True)

# Save the figure
output_path = os.path.join(output_dir, 'business_unit_cases_by_region.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')

print("Radar chart created successfully!")
print(f"Saved to: {output_path}")

# Display the plot
plt.show()
