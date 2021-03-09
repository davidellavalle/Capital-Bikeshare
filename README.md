# -Capital-Bikeshare

![alt text](https://thumbs.dreamstime.com/b/september-washington-dc-close-up-capital-bikeshare-bike-rental-system-residents-tourists-district-columbia-141486725.jpg)

## Introduction

The project analysis is based on data pulled from Capital Bikeshare, a company that offers a bicycle sharing system in Washington, D.C.   
The goal of the project is to find interesting paths about the User behaviour and the demand of services in the different seasons and months of the year, as well as day of the week or hours of the day. The data and results will be then used to provide the company with useful and meaningful insights on their business and give KPI's suggestions to measure the business and ensure future growth.  

Finally a prototype App (developed with the Flask framework and deployed by using Heroku) was developed to predict the demand of bike in the different days of the year depending on the day and time of pickup.  
At first we were provided with a dataset containing hourly and daily count of rental bikes along with the weather information for a period of 24 months (2011-12). Gradually more current data (2018-2019, March 2020) was downloaded from the company's website.

The project will focus on the following bulletpoints:

- Contribution of weather condition on bike demands  
- Season wise hourly distribution of bike rentals
- Casual users vs Member users, customer behaviour on usage of bikeshare
- Peaks during time - monthly, weekly, hourly (most requested hour of the days)
- Ride Duration - mean over day
- Most used Dock stations
- The Impact of Covid on bike demand

## Bikesharing

Bike sharing is a concept originating back to the 1960s when in Amsterdam the first bike share system "White Bikes" was implemented. 

The concept of bike share is easy to understand: a shared transport service in which bicycles are made available for shared use to individuals on a short term basis for a price or free. 
The first bike share systems where allowing people to borrow a bike from a "dock" (special bike racks that lock the bike, and only release it by computer control) and return it at another dock belonging to the same system. At the beginning of the century new systems of dockless bike, which do not require a docking station, were made available and bikes could be locked or unlocked with a digital authentication code. Bikes can now be picked up and dropped off anywhere, as per the convenience of the riders, which makes them more popular than the older station-based.

With environmental issues and health becoming trending topics, usage of bicycles as a mode of transportation has then gained more and more popularity in recent years pushing cities across the world to invest considerable sums of money on the implementation of bike sharing programs.

The development of this business model was anyway slow to catch on until better technology was developed, which could provide real-time information about the bike share scheme, track the bikes and help safeguard against theft.
Nowadays the bike sharing is booming at an unprecedented rate, largely due to the reasonably low cost of the schemes, and how easy they are to implement compared with other transport infrastructure.
The bike sharing market size has been valued at over $4 billion in 2018 with an estimated growth of 15% CAGR(Compounded Average Growth Rate) from 2019 to 2025.

## Data sources

All data was retrieved directly from [Capital bikeshare](https://www.capitalbikeshare.com/system-data) website.

## Exploratory analysis

At first the focus was on the data for the years 2011-12, then more current data (2018, 2019 and March 2020) was downloaded. After some basic cleaning I have proceeded with several visualizations using different plots that lead me to discover the following paths:

1. Weather conditions and temperatures have a great impact on the use of Bike sharing.  
While the demand is high with sunny or cloudy days, there is a significant drop in case of rain and no use at all in case of storms.  
This is confirmed as well from the analysis on the different seasons of the year showing winter as the season during which bikes are rarely used.  
At last a temperature analysis show how most of the rides are taking place when temperatures are above 10 degrees Celsius.
2. Most of the rides are performed by Members of Capital Bikeshare who use them mostly for commuting purposes (home to work, station, schools...). The use of bikes during the different hour of the day show infact that the most requested time are to be found between 7am-9am and 4pm-7pm.   
Casual members show instead a much more touristic use of bikes since their rides are taking place between 10am-8pm.
3. By observing number of bike rentals on each weekday, we can conclude that Member users tend to ride a bike from Monday to Friday (confirming the commutation theory), while Casual users are most active during weekends (bike trips).
4. The Duration of the rides doesn't show any particular trend during normal working days but it is significantly longer during weekends.  
Finally most of the rides seem to have a duration between 3 and 14 minutes.
5. Covid brought a notable decrease in number of rides (-40% March 19 to March 20). The main drops are to be found after 15th of March when remote work was introduced in Washington Dc and 24th of March when all "Non-essential" Dc Businesses were ordered closed by the Mayor.


2020 to be added - More casual than members

## Timeseries - Facebook Prophet

Facebook’s Prophet is a library designed to do Time Series forecasting and supports R and Python. 
The predicting model has been fed with the data of 2018 and 2019 and it is providing predictions for the first 6 months of 2020.  
This data was picked because Covid had not yet affected our society and I wanted to show the power of this tool in a standard/normal situation, where no unpredictable events had happened yet. This could be as well seen as a limit of predicting models.

## Flask App

Flask is a micro web framework written in python and used in web development. The term 'microframework' means it does not require particular tools or libraries.

For this project I developed a simple app that predicts the bikes demand in the different hours and days of the year depending on the month, weekday, time, wether the day is a holiday or not and type of customers (member or casual). The app was then deployed using Heroku and can be found easily by clicking on this link.



## File description:
[Data from 2011-12](https://github.com/davidellavalle/Capital-Bikeshare/tree/main/2011-12): hourly and daily count of rental bikes along with the weather information for a period of 24 months (2011-12)

### Legal Terms:

All data has been used only for educational purposes