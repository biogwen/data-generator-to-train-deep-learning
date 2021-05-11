import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

covid = pd.read_csv('covid.csv')
covid = covid.drop(['source'], axis=1)
covid = covid.dropna()
covid_grouped = covid.groupby(covid.continent)

asia = covid_grouped.get_group('Asia')
africa = covid_grouped.get_group('Africa')
europe = covid_grouped.get_group('Europe')
america = covid_grouped.get_group('America')
oceania = covid_grouped.get_group('Oceania')

sns.lineplot(x="year_week", y="cumulative_count",
             hue="country", data=oceania,sizes=)
