import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("toy_hr_data.csv")
salary = df["salary"]

mean_salary = salary.mean()
median_salary = salary.median()

fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(salary, bins=15, color="#89CFF0", edgecolor="black", alpha=0.8)

ax.axvline(mean_salary, color="red", linestyle="--", linewidth=2,
           label=f"Mean: ${mean_salary:,.0f}")
ax.axvline(median_salary, color="blue", linestyle="--", linewidth=2,
           label=f"Median: ${median_salary:,.0f}")

ax.set_title("Distribution of Salary")
ax.set_xlabel("Salary")
ax.set_ylabel("Frequency")
ax.legend()

fig.tight_layout()
fig.savefig("salary_distribution.png", dpi=150)
print(f"Mean: {mean_salary}, Median: {median_salary}")
