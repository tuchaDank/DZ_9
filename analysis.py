import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt

with open("events.json",  "r", encoding="utf-8") as file:
    data = json.load(file)

df = pd.DataFrame(data["events"])

counts = df["signature"].value_counts()

print(counts)

sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.barplot(x=counts.values, y=counts.index)
plt.xlabel("Количество событий")
plt.ylabel("Сигнатура")
plt.title("Распределение событий ИБ")
plt.tight_layout()
plt.savefig("distribution.png", dpi=150)
plt.show()
