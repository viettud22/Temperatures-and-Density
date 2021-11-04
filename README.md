# Temperatures-and-Density
Assignments for Computational Data Science (CMPT 353) at Simon Fraser University

This question will combine information about cities from Wikidata with a different subset of the Global Historical Climatology Network data.

The question I have is: is there any correlation between population density and temperature? I admit it's an artificial question, but one we can answer. In order to answer the question, we're going to need to get population density of cities matched up with weather stations.

To compile: 

python3 temperature_correlation.py stations.json.gz city_data.csv output.svg

Output:

Produce a scatterplot of average maximum temperature against population density 

