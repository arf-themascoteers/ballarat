import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

file_path = "summary.csv"
df = pd.read_csv(file_path)
df["train_size"] = (df["train_size"]*100).astype(int)

df_pivot = df.pivot(index="train_size", columns="target_size", values="execution_time")

plt.figure(figsize=(10, 6))
heatmap = sns.heatmap(df_pivot.round(3), annot=True, fmt=".3f", cmap="coolwarm",norm=LogNorm(),
    cbar_kws={'label': r"Execution time (second)"}
            )

cbar = heatmap.collections[0].colorbar
cbar.ax.set_ylabel(r"Execution time (second)", fontsize=20, color="#0C2C48")
cbar.ax.xaxis.set_label_coords(0.5, -0.2)
#plt.title("Heatmap of Train Size vs Target Size")
plt.ylabel("Train Size (%)", fontsize=20, color="#0C2C48")
plt.xlabel("Number of bands", fontsize=20, color="#0C2C48")



plt.savefig("heatmap3.png")