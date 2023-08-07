---
title-block-stytle: default
title-block-banner: false
callout-appearance: simple
editor:
  render-on-save: true
execute:
  freeze: true
title: Climate Variables
---






## Temperature (Annual)

Each climate model generates temperature readings every 3 hours, or 8
temperature readings per day.

The maximum daily temperature refers to the highest of these 8 readings, which
often occurs in the middle of the daytime and is comparable to the 'high
temperature' in a daily weather forecast.

Similarly, the minimum daily temperature refers to the lowest of these 8
readings, which often occurs overnight and is comparable to the 'low
temperature' in a daily weather forecast.

Argonne calculated the annual average of both the maximum and minimum daily
temperatures. 

These daily high / low readings were then used to calculate the annual average
maximum or minimum daily temperature for that scenario's model year (e.g. the
average max daily temperature for 2045 using the CCSM model under RCP4.5).

This process was repeated for each year within a given time period / scenario
(e.g. 2046, 2047, and so forth) across all three climate models (CCSM, GFDL,
and HadGEM).

Finally, the 30 individual annual averages for a given time period/scenario
were themselves averaged, producing a multi-model ensemble mean that represents
the annual average of the maximum or minimum daily temperature for a given time
period / scenario.

## Temperature (Seasonal)

Each climate model generates temperature readings every 3 hours, or 8
temperature readings per day.

The maximum daily temperature refers to the highest of these 8 readings, which
often occurs in the middle of the daytime and is comparable to the 'high
temperature' in a daily weather forecast.

Similarly, the minimum daily temperature refers to the lowest of these 8
readings, which often occurs overnight and is comparable to the 'low
temperature' in a daily weather forecast.

Argonne calculated the seasonal average of both the maximum and minimum daily
temperatures; the seasons are segmented as 

- Winter (Dec, Jan, Feb)
- Spring (March, April, May)
- Summer (June, July, Aug)
- Autumn (Sep, Oct, Nov)

These calculations involved extracting the highest temperature reading and
lowest temperature reading for each individual day of a year (e.g. 2045) within
a given time period / scenario (e.g. mid-century RCP4.5) and for a given
climate model (e.g. CCSM).

These daily high / low readings were then classified by season and used to
calculate the seasonal average maximum or minimum daily temperature for that
scenario's model year (e.g. the average daily max temperature for summer of
2045 using the CCSM model under RCP4.5).

This process was repeated for each year within a given time period / scenario
(e.g. 2046, 2047, and so forth) across all three climate models (CCSM, GFDL,
and HadGEM).

Finally, the 30 individual seasonal averages for a given time period / scenario
were themselves averaged, producing a multi-modal ensemble mean that represents
the seasonal average of the maximum or minimum daily temperature for a given
time period / scenario.

## Precipitation

Each climate model estimates an amount of precipitation (whether rain, snow,
sleet, or ice) that occurs every 3 hours across the entire modeled time period
(i.e. every 3 hours, of every day, for all modeled years).

These 3-hour precipitation estimates can be used to calculate the total
precipitation over a designated period of time, ranging from daily to annually.

Argonne calculated total annual precipitation by adding all 3-hour
precipitation estimates for a given year (e.g. 2045) within a given time period
/ scenario (e.g. mid-century RCP4.5) and for a given climate model (e.g. CCSM),
which produced the total annual precipitation for that scenario's model year,
such as CCSM's estimate of annual precipitation in 2045 under climate scenario
RCP4.5.

This process was repeated for each year within a given time period / scenario
(e.g. 2046, 2047, and so forth) and across all three climate models (CCSM,
GFDL, and HadGEM), producing a total of 30 estimates of total annual
precipitation for a given time period / scenario.

The average of these values was taken to produce the ensemble mean of the total
annual precipitation (in inches) for each time period / scenario.

## Wind Speed

Each climate model generates estimated wind speed readings (in miles per hour,
or `mph`) every 3 hours, or 8 wind speed readings per day.

These values are irrespective of wind direction and only represent the
magnitude of wind speed.

Using these readings, Argonne calculated the average daily wind speed (the
average of each day's 8 wind speed readings) for every day within a given time
period / scenario (e.g. mid-century RCP4.5) and for each climate model (CCSM,
GFDL, and HadGEM).

Argonne then took the average of each daily average wind speed for a given year
(e.g. 2045) and within a given time period / scenario (e.g. mid-century RCP4.5)
and for a given climate model (e.g. CCSM), which produced the annual average
wind speed for that scenario's model year, such as CCSM's estimate of annual
average wind speeds in 2045 under climate scenario RCP4.5.

This process was repeated for each year within a given time period / scenario.

The average of these values was taken to produce the ensemble mean of the
annual average wind speed (in `mph`) for each time period / scenario.

## Consecutive Days With No Precipitation

Each climate model estimates an amount of precipitation (whether rain, snow,
sleet, or ice) that occurs every 3 hours across the entire modeled time period
(i.e. every 3 hours, of every day, for all modeled years).

These 3-hour precipitation estimates were used to calculate the daily
precipitation quantities by adding all 8 precipitation readings for each day of
a given year (e.g. 2045) within a given time period / scenario (e.g.
mid-century RCP4.5) and for a given climate model (e.g. CCSM).

This process produced the total daily precipitation for every day in a
scenario's model year, such as CCSM's daily estimates of total precipitation
for the year 2045 under climate scenario RCP4.5.

Using this information, Argonne identified the greatest number of _consecutive_
days in which _no_ precipitation occurred (i.e. the total daily precipitation
quantity equaled zero) for that scenario's model year (e.g. for the year 2045
under scenario RCP4.5, the highest number of consecutive days without any
precipitation was X).

This process was repeated for each year within a given time period / scenario
(e.g. 2046, 2047 and so forth) across all three climate models (CCSM, GFDL, and
HadGEM) producing 10 yearly values for each model, with each value representing
the longest consecutive span with no precipitation for that year.

Of the 10 yearly values for each climate model, the maximum value was selected
(e.g. the decadal maximum). This resulted in 3 values for each climate model's
10 years of data.

The average of these maximum of the maxima was then taken to produce the
ensemble mean of the decade's highest number of consecutive days without
precipitation in a single year.


## Degree Days

Degree days measure how cold or warm a location is by comparing the daily
average temperature to a reference temperature, usually $65\degree$ F
($18.33\degree$ C).

Heating or cooling degree days roughly correlate with building heating or
cooling needs, providing a simple useful estimate in energy planning.

Heating degree days (HDD) measure how cold the temperature was on a given day
or a period of days,which shapes the need for a certain amount of building
heating.

For example, a day with an average temperature of $40\degree$ F has 25 HDD ($65
- 40 = 25$ HDD).

Similarly, cooling degree days (CDD) measure how hot the temperature was on a
given day; a day with an average temperature of $90\degree$ F has 25 CDD ($90 -
65 = 25$ CDD).

The calculations of HDD and CDD for this portal began with each climate model,
which generates temperature readings every 3 hours, or 8 temperature readings
per day.

For each, the maximum temperature (the daily high) and the minimum temperature
(daily low) were extracted and used to estimate the daily average temperature. 

This daily average temperature was then used to calculate that day's HDD (if
the average temperature was below $65\degree$ F) or CDD (above $65\degree$ F).

This process was conducted for each individual day of a year (e.g. 2045) within
a given time period / scenario (e.g. mid-century RCP4.5) and for a given
climate model  (e.g. CCSM).

These daily HDD/CDD values were then used to calculate the total number of
HDD/CDD for that scenario's model year (e.g. the total HDD for 2045 using CCSM
model under RCP4.5).

This process was repeated for each year within a given time period / scenario
(e.g. 2046, 2047, ...) across all three climate models (CCSM, GFDL, and
HadGEM).

Finally, the 30 annual total HDD / CDD estimates for a given time period /
scenario were themselves arranged, producing a multi-model ensemble mean that
represents the annual total HDD or CDD for a given time period / scenario.


## Fire Weather Index

The Fire Weather Index (FWI), also known as the Canadian Forest Fire Weather Index, was developed by the Canadian Forest Service.

It estimates the wildfire danger using information on weather conditions that influence the spread of wildfires. 

The FWI is comprised of multiple components that are developed using daily readings of temperature, relative humidity, wind speed, and 24-hour precipitation.

This weather information is used to estimate the dryness of soils and organic materials (which act as fuel for wildfires) and the rate of fire spread.

The FWI is useful for evaluating weather-based conditions that heighten the danger of wildfire spread _once ignition has occurred_; it does not account for sources of ignition, which can have both natural and human causes.

The FWI rangers from zero to $\infty$, with higher numbers corresponding to greater fire danger.

The level of wildfire danger, as represented by FWI, varies based on regional characteristics, such as a region's typical level of fire danger and its land cover.

For example, areas in the U.S. Southwest, which are often exceptionally dry, will have a higher average daily FWI values than areas in the Northeast.

A relatively high FWI that suggests a heightened level of fire danger in the Northeast might correspond to average fire danger in the Southwest.

Despite this variation, FWI values in excess of 20 typically represent high levels of fire danger, with levels above 30 representing very high to potentially extreme levels of fire danger.

A representative example of fire danger classes used by the European Forest Fire Information System can be found [here](https://effis.jrc.ec.europa.eu/about-effis/technical-background/fire-danger-forecast).

### Components of the FWI

The FWI is comprised of six components that are developed using daily readings
of temperature, relative humidity, wind speed, and 24-hour precipitation.

These readings are taken at solar noon and reflect fire danger at early- to mid-afternoon, typically the time of day in which fire weather conditions are more conducive to fire spread.

Three of the FWI's components estimate the amount of moisture on and beneath the forest floor.

These include measures of the moisture content of:

1. Fine fuels or forest litter (e.g. dried leaves) on top of the forest floor;
2. Intermediate organic layers, such as decomposing plant matter;
3. Deep organic layers and soils, which correspond to drought measures.

These moisture content components feed into the two primary subindices that generate the FWI.

The first of these is the Initial Spread Index, which measures the expected rate of fire spread; it is based on wind speeds and the moisture content of fine fuels (1. above).

The second is the Buildup index,w hich represents the total amount of forest fuel available for consumption, as measured via moisture in intermediate and deep organic layers (2. and 3. above).

The Initial Spread Index and the Buildup Index combine to generate the Fire Weather Index, or the index depicted in ClimRR.

For more information on the FWI and its methodology, please visit the [National Wildfire Coordinating Group](https://www.nwcg.gov/publications/pms437/cffdrs/fire-weather-index-system) or the [Canadian Forestry Service's report](https://cfs.nrcan.gc.ca/pubwarehouse/pdfs/19927.pdf) detailing FWI's development and structure.

### Calculating Seasonal Averages

Daily FWI values were calculated using daily weather readings from Argonne's
downscaled 12km climate data.

For a detailed description of each weather variable included in the
calculations, along with the formulas used to calculate FWI, see [Van Wagner
and Pickett](https://cfs.nrcan.gc.ca/pubwarehouse/pdfs/19973.pdf)

Argonne calculated the average daily FWI value by season for each year within a
given scenario (e.g. mid-century RCP4.5) and climate model (e.g. CCSM).

The seasons are segmented as

1. Winter (Dec, Jan, Feb)
2. Spring (March, April, May)
3. Summer (June, July, Aug)
4. Autumn (Sep, Oct, Nov)

Each year's seasonal average daily FWI was used to calculate a decadal average
daily FWI value for that season (e.g. the average daily FWI value in winter at
mid-century under RCP4.5)

This process was repeated across all scenarios and all three climate models
(CCSM, GFDL, and HadGEM), followed by calculating the multi-model ensemble mean
of each scenario's seasonal average daily FWI value.


