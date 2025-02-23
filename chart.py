import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

models = ["Stevens\net al.\n(2013)", "Zhong\net al.\n(2021)",
          "Tsimpouris\net al.\n(2021)",
          "Liu\net al.\n(2023)","SAE-1DCNN\n(2025)","Proposed\n(2025)"]
accuracy = [0.67,0.96,0.88,0.71, 0.78,0.91]
efficiency = [0,0,0,0,1000/945,1000/297]

x = np.arange(len(models))
width = 0.4

fig, ax1 = plt.subplots(figsize=(6, 5))
ax1.set_xlabel("Models", color="#0C2C48", fontsize=14)
ax1.set_ylabel("Accuracy (%)", color="#0C2C48", fontsize=14)
ax1.bar(x - width/2, accuracy, width, color="#0C2C48", label="Accuracy")
ax1.tick_params(axis='y', labelcolor="#0C2C48")
ax1.set_ylim(0, 1.1)


ax1.set_xticks(x)
ax1.set_xticklabels(models,fontsize=8, color="#0C2C48")
bold_font = FontProperties(weight='bold')
for label in ax1.get_xticklabels()[-1:]:
    label.set_fontproperties(bold_font)

ax2 = ax1.twinx()
ax2.set_ylabel("Efficiency (1000/second)", color="#A6CE39", fontsize=14)
ax2.bar(x + width/2, efficiency, width, color="#A6CE39", label="Efficiency")
ax2.tick_params(axis='y', labelcolor="#A6CE39")
ax2.set_ylim(0, 4)

ax1.legend(loc="upper left")
ax2.legend(loc="upper right")



plt.savefig("chart.png", dpi=300, bbox_inches='tight')
