# Databanks

humdata.org  
democracymatrix.com/ranking  
wid.world/data/  
worldvaluesservey.org  
databank.worldbank.org  
https://www.hofstede-insights.com/country-comparison/denmark,france,germany,sweden/

## Epic Databanks
https://databank.worldbank.org/source/world-development-indicators#
https://freedomhouse.org/ (excel file uploaded to repo)

## Data on Democracy (political rights and civil liberties)
1.  Electoral Integrity Project, which provides a global dataset of election quality indicators)
2. Civil liberties (freedom house invludes this)
3. Rule of law (e.g. World Justice Project Rule of Law Index, which provides a global ranking of countries based on their adherence to the rule of law.)
4. Political accountability (Varieties of Democracy project, which provides a global dataset of political accountability indicators.)
5. The Democracy Matrix Ranking (Index from German homepage)
    - Basically a simple version of Freedom House, I presume.
6. The Economist Intelligence Unit's Democracy Index: This index provides a ranking of 167 countries based on five categories: electoral process and pluralism, functioning of government, political participation, political culture, and civil liberties.
7. The Varieties of Democracy (V-Dem) Project: This project produces a dataset that measures democracy based on seven different principles: electoral, liberal, participatory, deliberative, egalitarian, majoritarian, and consensual.
8. The Polity Project: This project provides a rating of countries' democracy levels based on the competitiveness of political participation, the openness and transparency of the government, and the constraints placed on the executive.
9. Bertelsmann Transformation Index: This index assesses the quality of democracy in countries based on political management, social inclusion, and economic transformation.
10. World Press Freedom Index: This index ranks countries based on the level of freedom journalists and media organizations have to report news without fear of censorship, harassment, or physical harm.
11. UNESCO Global Democracy Index https://www.eiu.com/n/campaigns/democracy-index-2020/
12. The Human Freedom Index https://www.cato.org/human-freedom-index/2022
13. The Worldwide Governance Indicators: This set of indicators measures the quality of governance in countries based on factors such as voice and accountability, political stability and absence of violence, government effectiveness, regulatory quality, rule of law, and control of corruption.


# Idea Brainstorm

## Scoring Democracy On Various Parameters

Scoring democracy amongst other parameters on pr adult GDP and income inequality in European countries in 2021.
Perhaps scoring is a sum of weighted averages.
Visualisation could be barplot or index.
https://wid.world/data/
Tried to add data, but couldn't support .csv file type.

## Democracy and Economic development
Use data on economic indicators such as GDP and income inequality, as well as data on political institutions and measures of democracy, to explore the relationship between democracy and economic development.

1. Investigate the relationship between democracy and economic development.
2. Use open data sources such as the World Bank's World Development Indicators or the Freedom House dataset to analyze measures of political rights, civil liberties, and economic indicators such as GDP, inflation, and unemployment rates. We could just use the Freedom House score as it seems like a great dataset to work with.
3. Use R to create scatterplots and regression models that investigate the relationship between measures of democracy and economic outcomes such as GDP growth rates or levels of foreign direct investment.
4. Use R to perform cluster analysis to identify groups of countries that share similar characteristics in terms of their democratic institutions and economic outcomes. This can help identify patterns and trends in the data that may not be immediately apparent from looking at individual countries or variables. For example, cluster analysis may identify groups of countries with similar levels of democracy and economic growth, or it may reveal differences in economic outcomes between countries with similar levels of democracy.

### Economic Variables to Regress On
Human Development Index (HDI): This composite index measures indicators such as life expectancy, education, and income to provide a broader picture of human development in a country.

1. Income inequality (GINI)

2. Economic growth rate

3. Abundance of Natural resources (I presume that is a negative correlation)

4. Gross National Income (GNI) per capita: This is a measure of a country's economic output per person.

5. Employment rate: This measures the percentage of the population that is employed.

6. Poverty rate: This measures the percentage of the population living below the poverty line.

7. Inflation rate: This measures the rate at which prices for goods and services are increasing in a country.

8. Education level: This measures the average level of education among a country's population, typically measured by the percentage of the population that has completed primary, secondary, or tertiary education.

9. Health indicators: Measures such as life expectancy, infant mortality rate, and access to healthcare can provide insight into a country's overall level of development and well-being.

## Historical trends in democracy
Analyze data on historical trends in democratic institutions, such as measures of political rights and civil liberties, to explore how democracy has evolved over time across different regions of the world. Use R to create visualizations that highlight key trends and patterns in the data.
We could group countries by region. Really easy if we use the dataset from Freedom House.

## Democracy and Social Inequality
Danalyze data on social indicators such as education and health outcomes, as well as measures of democratic institutions, to explore the relationship between democracy and social inequality. Use R to create visualizations that highlight differences in democratic outcomes across countries with varying levels of social inequality.

## Global Migration Patterns
Use data on migration patterns to explore trends in international migration, including the reasons people migrate and the impact of migration on both sending and receiving countries. Use R to create visualizations that highlight differences in migration patterns across regions and countries.

 ##  Cultural values and economic outcome
 Analyze data on cultural values and economic outcomes to explore how cultural factors influence economic development. Use R to perform regression analysis that examines the relationship between cultural values and economic outcomes such as GDP and employment rates.

  ## Income inequality and education
 Analyze the relationship between income inequality and educational outcomes using data on income distribution and education levels across countries. Use R to perform regression analysis to determine the effect of income inequality on educational outcomes.

## Income mobility and social inequality
 Analyze data on income mobility and social inequality to explore the extent to which social and economic mobility is possible across different countries and regions.

 ## Human development and environmental sustainability
 Analyze data on human development and environmental indicators such as carbon emissions and renewable energy use to explore the relationship between economic development and environmental sustainability. Use R to create linear regression models to examine the impact of economic development on environmental sustainability.