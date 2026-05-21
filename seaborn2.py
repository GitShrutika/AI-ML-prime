tips=sns.load_dataset("tips")

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="time"
)
flights=sns.load_dataset("flights")
sns.lineplot(
    data=flights,
    x="year",
    y="passengers"
)
print(tips.head())
sns.barplot(
    data=tips,
    x="day",
    y="tip",
    hue="sex"
)
penguins=sns.load_dataset("penguins")
sns.histplot(
    data=penguins,
    x="body_mass_g",
    bins=15
)
flights_pivoit=flights.pivot(index="month",columns="year",values="passengers")

sns.heatmap(
    flights_pivoit,
    cmap="coolwarm"
)
    
