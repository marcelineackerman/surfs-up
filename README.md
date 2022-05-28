# Surf's Up!

## Overview
An analysis using advanced data storage and retrieval with SQLite, Python, and Python on precipitation and temperature on Oahu, Hawaii in advance of a new business venture, honing in on temperature statistics in June and December to determine if the ice cream/surf shop venture is viable year-round.

## Results

 - Using the ```describe()``` function on the temperature data of the month of June from the years 2010 to 2017, we can see that the mean temperature throughout the years is roughly 75 degrees F, with a minimum temperature of 64 degrees and a max of 85 degrees. All of these are comfortable temperatures to both surf in the ocean, and encourages eating frozen treats like ice cream. This is a comfortable range for opening the surf/ice cream shop.
 
![image](https://user-images.githubusercontent.com/100869713/170831381-c49cf9ea-ef7e-4a57-82c8-8a55a11815d5.png)

 - Using the ```describe()``` function on the temperature data of the month of December from the years 2010 to 2017, we can see that the mean temperature throughout the years is roughly 71 degrees F, with a minimum temperature of 56 degrees and a max of 83 degrees. While the very minimum temperature is a little low to expect much business, the first quartile is greater than three standard deviations away at 69 degrees, indicating that the 56 degrees is an outlier and the true temperature most days will be in a comfortable range for opening the surf/ice cream shop.

![image](https://user-images.githubusercontent.com/100869713/170831532-1cdb9a00-7702-4cc9-a1b2-5429727a01ab.png)

 - The analysis of both June and December demonstrates that the temperature ranges are comfortable both in the middle of the year and at the end of the year. The difference in average temperature is negligible and the lower temp in December is likely influenced by the lower outlier. This means the surf/ice cream shop can be open year round with no issue in regards to temperature.

## Summary

The temperature analysis of June and December from 2010-2017 reveals a very favorable pattern in weather year-round for this budding business venture. People like to surf, swim, and eat ice cream when it's warm, and according to the analysis, December and June are both very warm on average. As these are considered "opposite seasons" and the weather remains consistent suggests year-round favorable conditions temperature-wise.

  - Unfortunately, temperature is not the only weather variable that could affect ice cream and surf supplies sales. For a better picture, we should also look at precipitation data for June and December. We can do so using the following queries to filter out the precipitation data for June and December:
  ```
  june_results = session.query(Measurement.date, Measurement.prcp).\
    filter(extract('month', Measurement.date) == 6).all()
    
  dec_results = session.query(Measurement.date, Measurement.prcp).\
    filter(extract('month', Measurement.date) == 12).all()
    
   june_df = pd.DataFrame(june_results)
   dec_df = pd.DataFrame(dec_results)
   ```   
And then from there, use the ```describe()``` function again on those dataframes to retrieve the summary statistics for these months over the course of 2010-2017.

With precipitation and temperature data, the picture will be much clearer on the conditions and viability of the potential venture.

## Tools

 - Python 3.9.2
 - Pandas
 - SQLite
 - Jupyer Notebook
 - Flask
