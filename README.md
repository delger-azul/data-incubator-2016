# The Data Incubator 2016 semifinalist project

## Motivation

Public misinformation about foreign aid and development assistance seems to undermine its public support in developed countries. More than 30 billion dollars is allocated to aid for Africa by the Development Assistance Committee (USA, EU etc.) every year. The public seems to think much more is allocated towards aid as a share of GDP, and systematically think the US should provide lower levels of aid. 

The lack of transparency may not allow the public to demand aid to be used according to citizens' will, and to have an informed debate on how to allocate aid. To help with this, this project aims to:
* Improve transparency of aid to countries in Africa, and tell citizens what aid is buying
* Show the periods and places where foreign aid has been the most effective/most costly
* Provide tools for policy makers on how to inform the audience on aid

## Data Source

[All data post-scraping, post-querying and post-processing made available through Tableau: just click on download data](http://data-incubator-delger.herokuapp.com/tableau)
I use the following open data sources:
* GDELT (the Global Database of Events, Language and Tone) database
  * Regarded as "the largest, most comprehensive, and highest resolution open database of human society ever created".
  * Interesting for capturing news about events across time and space
  * I use it to capture news (intensity of news) about aid and conflict intensity
* UN Voting database to gauge alignment with US
    * [Original data link](http://dataverse.harvard.edu/dataset.xhtml?persistentId=hdl:1902.1/12379)
* Development Assistance Committee: aid commitments to countries and regions
    * [Original data link](http://stats.oecd.org/Index.aspx?DataSetCode=TABLE3A)

## Modeling and Analysis

* Use Tableau to connect to Google BigQuery
* Regression analysis for favouritism and aid, aid and conflict

## Plots
Plot 1: Aid and its media coverage
I aim to show discrepancy between actual aid disbursed and news about aid and development assistance.

Plot 2: Alignment with US and Aid
* American aid is an important tool for American foreign policy: it is part of the system through which countries aligned with the US get additional benefits, and potentially important in getting countries to be aligned with the US to start with.
* Maintaining the American prominence in foreign policy might require active aid policies 
* Evolution over time: 
  * Harder to buy support during Bush years (Iraq War conducted in a unilateral way against the will of many countries), and more foreign aid went to relatively less aligned countries
  * Easier to buy support during Obama years, when the same amount of foreign aid was related to much higher levels of coherence with US votes in the UN

* Where has this worked

Plot 3: Aid and conflict
* American development aid is either going to countries with significant levels of conflict, or breeding conflict
* Understanding periods and countries for which this was less prominent might allow us to reduce the potential for aid to bring conflict

Plot 4: Tableau dashboard embedded, allowing for interactivity (filter by regime, sentiment and eras)
* Conflict and its media coverage
* Conflict and Aid (included above)
* US alignmend and Aid (included above)

## Video
