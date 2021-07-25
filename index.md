# Predicting Flight Delays

Prior to the 2020 coronavirus pandemic, the United States airline industry was a steadily growing industry earning a revenue stream of $248 billion in 2019 alone. Millions more Americans were boarding planes each year; in 2019 811 million people boarded a US plane. In 2020, the airline industry suffered along with many others. Now in 2021, as air travel begins to pick up again, airlines need to regain the trust of travelers as being the best, most reliable airline. Now more than ever it is important that United States airline companies operate effectively by getting travelers from point A to point B with minimal delays.

When airlines are able to predict delays in advance they will have more time to come up with a solution for their travelers, such as buffering the next flight's departure time or having an extra team and aircraft available at airports with an increased chance of delays. The model below is a tool designed for airline companies to use when building flight schedules in order to predict and plan for delays. 


## Flight Delays Predictor ##
- A model designed to predict if a commercial plane will be delayed.
- Based on origin and destination airport information, the aircraft, flight times and holiday season. 
- Currently predicting with 75% accuracy. 

insert link here
pull up actual 2021 flight info
have values in model alreayd


## Model Construction:

### Data Preprocessing
<p align="center">
  <img width="400" height="275" src="https://user-images.githubusercontent.com/87782980/126913160-c034aa5f-d6bf-4bd6-a62c-a0c2c24a2852.png">
</p>

Exploratory data analysis and data preprocessing performed in postgreSQL:

             - Imputed values for some nulls in ARRIVAL_DELAY using SCHEDULED_ARRIVAL - ARRIVAL_TIME.
             - Dropped 92,513 rows (or 1.6% of the dataset) containing nulls in all 6 columns.
             - Replaced the remaining 12,558 nulls by imputing AIR_TIME and ELAPSED_TIME based on data in other columns. 
             - Inserted values into LATITUDE and LONGITUDE columns for the airports with nulls.
             - Joined data tables (flight data, airport data and holiday season calendar). 
             - Dropped data where the flight route had less than 700 flights.
             - Used SQLAlchemy to import the joined data from pgAdmin into Jupyter Notebook. 



 ![image](https://user-images.githubusercontent.com/87782980/126912942-0c7c4a89-4713-4277-a50b-2628cef4f2b3.png) ![image](https://user-images.githubusercontent.com/87782980/126913244-ecfb0826-04b1-4c45-9159-d997f357aafa.png)

 
 ![image](https://user-images.githubusercontent.com/87782980/126913180-5ecc81ff-80f2-4c53-ad58-4c4d00dadbe2.png)![image](https://user-images.githubusercontent.com/87782980/126913191-209ede74-67d1-4deb-890a-209b2f76a0c5.png)


![image](https://user-images.githubusercontent.com/87782980/126913308-79cb758f-a31d-4bed-80ed-6f95cbab44be.png)


Exploratory data analysis and data preprocessing performed in Jupyter Notebook:

            - Dropped _
            - Created result15 column...

visual, result column code 

### Visualizing Data
#### Chart 

![image](http://localhost:8888/view/Documents/Capstones/Flight%20Data%20Capstone/ODC_chart.png)

Chart description....



### Model Building
#### Decision Tree Classifier 

![image]() graph of imablanced data

#### Steps to improve model

![image]()


![image](https://user-images.githubusercontent.com/87782980/126912898-5c03a885-aeb8-4e39-ab89-9f656b9760c9.png)


![image](https://user-images.githubusercontent.com/87782980/126912887-81b716e8-fbca-4291-94d5-bd4583c7d765.png)

## Next Steps:
- Data from other years, data for reasons of delays, etc
- Given more time I would implement data based on the weather averages at each airport based on the time of year

make sure to annotate! address underscores in title, could include graph of distibutions of variables


## Acknowledgements:




You can use the [editor on GitHub](https://github.com/samanthaglasson/FlightDelayModel/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3
## Samanntha 
- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

