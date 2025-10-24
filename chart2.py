import matplotlib.pyplot as plt
import numpy as np
import os

# Data for the charts (6 month lookback)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
month_numbers = np.arange(len(months))

# New Incidents by Business Unit Over Time
incidents_bu1 = [12, 15, 13, 18, 16, 14]
incidents_bu2 = [18, 22, 20, 24, 26, 23]
incidents_bu3 = [15, 17, 19, 21, 18, 20]

# Response Actions by Business Unit Over Time
actions_bu1 = [35, 42, 38, 51, 45, 40]
actions_bu2 = [52, 65, 58, 70, 75, 68]
actions_bu3 = [44, 48, 55, 60, 52, 58]

# False Positives by Business Unit Over Time
fp_bu1 = [8, 10, 9, 12, 11, 10]
fp_bu2 = [14, 16, 15, 18, 20, 17]
fp_bu3 = [11, 13, 14, 16, 14, 15]

# Create figure with 3 subplots
fig, axes = plt.subplots(3, 1, figsize=(10, 14))
fig.suptitle('Historical Impact Profile\nKey Metrics by Business Unit',
             fontsize=24, fontweight='bold', y=0.995)

# Define colors for each business unit
colors = {
    'BU1': '#DC3545',
    'BU2': '#FF8C00',
    'BU3': '#4A90E2'
}

# Chart 1: New Incidents by Business Unit Over Time
ax1 = axes[0]
ax1.plot(month_numbers, incidents_bu1, marker='o', color=colors['BU1'],
         linewidth=2.5, markersize=7, label='Business Unit 1')
ax1.plot(month_numbers, incidents_bu2, marker='o', color=colors['BU2'],
         linewidth=2.5, markersize=7, label='Business Unit 2')
ax1.plot(month_numbers, incidents_bu3, marker='o', color=colors['BU3'],
         linewidth=2.5, markersize=7, label='Business Unit 3')

ax1.fill_between(month_numbers, 0, 30, color='lightgray', alpha=0.3)
ax1.set_xticks(month_numbers)
ax1.set_xticklabels(months, fontsize=18, fontweight='bold')
ax1.set_ylabel('New Incidents', fontsize=16, fontweight='bold')
# ax1.set_title('New Incidents', fontsize=20, fontweight='bold', pad=10)
ax1.legend(loc='upper left', frameon=False, fontsize=11)
ax1.set_ylim(0, 30)
ax1.tick_params(axis='y', labelsize=16)
ax1.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Chart 2: Response Actions by Business Unit Over Time
ax2 = axes[1]
ax2.plot(month_numbers, actions_bu1, marker='s', color=colors['BU1'],
         linewidth=2.5, markersize=7, label='Business Unit 1')
ax2.plot(month_numbers, actions_bu2, marker='s', color=colors['BU2'],
         linewidth=2.5, markersize=7, label='Business Unit 2')
ax2.plot(month_numbers, actions_bu3, marker='s', color=colors['BU3'],
         linewidth=2.5, markersize=7, label='Business Unit 3')

ax2.fill_between(month_numbers, 0, 80, color='lightgray', alpha=0.3)
ax2.set_xticks(month_numbers)
ax2.set_xticklabels(months, fontsize=18, fontweight='bold')
ax2.set_ylabel('Response Actions', fontsize=16, fontweight='bold')
# ax2.set_title('Response Actions by Business Unit Over Time', fontsize=20, fontweight='bold', pad=10)
ax2.legend(loc='upper left', frameon=False, fontsize=11)
ax2.set_ylim(0, 80)
ax2.tick_params(axis='y', labelsize=16)
ax2.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# Chart 3: False Positives by Business Unit Over Time
ax3 = axes[2]
ax3.plot(month_numbers, fp_bu1, marker='^', color=colors['BU1'],
         linewidth=2.5, markersize=7, label='Business Unit 1')
ax3.plot(month_numbers, fp_bu2, marker='^', color=colors['BU2'],
         linewidth=2.5, markersize=7, label='Business Unit 2')
ax3.plot(month_numbers, fp_bu3, marker='^', color=colors['BU3'],
         linewidth=2.5, markersize=7, label='Business Unit 3')

ax3.fill_between(month_numbers, 0, 25, color='lightgray', alpha=0.3)
ax3.set_xticks(month_numbers)
ax3.set_xticklabels(months, fontsize=18, fontweight='bold')
ax3.set_xlabel('Month', fontsize=16, fontweight='bold')
ax3.set_ylabel('False Positives', fontsize=16, fontweight='bold')
# ax3.set_title('False Positives by Business Unit Over Time', fontsize=20, fontweight='bold', pad=10)
ax3.legend(loc='upper left', frameon=False, fontsize=11)
ax3.set_ylim(0, 25)
ax3.tick_params(axis='y', labelsize=16)
ax3.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

plt.tight_layout()
plt.subplots_adjust(hspace=0.4, top=0.90)

# Create outputs directory if it doesn't exist
output_dir = 'outputs'
os.makedirs(output_dir, exist_ok=True)

# Save the figure
output_path = os.path.join(output_dir, 'business_unit_metrics_6month.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Timeline charts saved to {output_path}")
plt.show()
