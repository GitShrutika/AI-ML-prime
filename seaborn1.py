pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()
sns.get_dataset_names()
tips=sns.load_dataset("tips")
print(type(tips))
print(tips.head())

sns.set_theme(style="darkgrid")#whitegrid,white
sns.relplot(
    data=tips,
    kind="line",
    x="total_bill",
    y="tip",
    hue="smoker",
    size="size",
    style="smoker"
)
 x_vals=[1,2,3,4,5,6,7,8,9]
y_sq=[i**2 for i in x_vals]
sns.set_theme(style="ticks")

sns.relplot(
    x=x_vals,
    y=y_sq,
    kind="line"
)
