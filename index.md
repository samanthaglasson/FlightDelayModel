# Predicting Flight Delays

Prior to the 2020 coronavirus pandemic, the United States airline industry was a steadily growing industry earning a revenue stream of $248 billion in 2019 alone. Millions more Americans were boarding planes each year; in 2019 811 million people boarded a US plane. In 2020, the airline industry suffered along with many others. Now in 2021, as air travel begins to pick up again, airlines need to regain the trust of travelers as being the best, most reliable airline. Now more than ever it is important that United States airline companies operate effectively by getting travelers from point A to point B with minimal delays.

When airlines are able to predict delays in advance they will have more time to come up with a solution for their travelers, such as buffering the next flight's departure time or having an extra team and aircraft available at airports with an increased chance of delays. The model below is a tool designed for airline companies to use when building flight schedules in order to predict and plan for delays. 



## Flight Delays Predictor ##
- A model designed to predict if a commercial plane will be delayed.
- Based on origin and destination airport information, the aircraft, flight times and holiday season. 
- Currently predicting with 75% accuracy. 



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




<p align="center">
  <img width="400" height="325" src="https://user-images.githubusercontent.com/87782980/126994078-e4798bff-b38d-4bcf-839a-1bf8619adeb7.png">
</p> 

<p align="center">
  <img width="200" height="100" src="https://user-images.githubusercontent.com/87782980/126998135-4015be51-4e3d-45e0-ace2-677000e29379.png">
</p> 

 
Exploratory data analysis and data preprocessing performed in Jupyter Notebook:

            - Encoded all categorical data using LabelEncoder. 
            - Dropped redundant columns. 
            - Created the target variable column, result15.
            

### Visualizing Data

<p align="center">
  <img src="https://user-images.githubusercontent.com/87782980/126912942-0c7c4a89-4713-4277-a50b-2628cef4f2b3.png">
</p>  

<p align="center">
  <img src="https://user-images.githubusercontent.com/87782980/127028934-d873b913-132c-4640-9af7-48b6d8ce5f34.png">
</p>  

<p align="center">
  <img src="https://user-images.githubusercontent.com/87782980/127028874-8ffd684d-b221-492a-9037-85e0860b7848.png">
</p>  

<p align="center">
  <img src="https://user-images.githubusercontent.com/87782980/127033101-86c5c1bb-00e4-47ca-9084-9bd68b8ee991.png">
</p>  



(additional feature charts here) 


### Model Building
#### Decision Tree Classifier 

<p align="center">
  <img src="https://user-images.githubusercontent.com/87782980/127001252-bb303241-eb97-467f-86cd-82fe2a400def.png">
</p> 


<p align="center">
  <img width="500" height="450" src="https://user-images.githubusercontent.com/87782980/127000720-ea2c7b54-3029-4ef1-a93c-aac239b07154.png">
</p>

(graph of  feature importance)

At first, the model was predicting a moderately high accuracy, however, the data was very imbalanced. The model also carried features with no siginificant importance, but these were dropped to improve the model's accuracy. 


#### Steps to improve model

To address the imbalance of data, a sample of the majority class - on time data - was randomly taken. Additionally, a pipeline was constructed using Synthestic Minority Oversampling Technique, SMOTE, to duplicate examples within in the minority class - delayed data - and randomly dropped rows in the majority class. 

<p align="center">
  <img src="https://user-images.githubusercontent.com/87782980/127027240-0a71533a-7ad0-4624-b186-20fee4b99962.png">
</p>

As you can see, these steps were successful in balancing the data. 

<p align="center">
  <img src="https://user-images.githubusercontent.com/87782980/127002784-6361bff0-2eac-44e4-8d16-d20794b8f94b.png">
</p> ![image]()


<p align="center">
  <img src="https://user-images.githubusercontent.com/87782980/127003149-1c7404ae-8dbc-4d5e-af73-b953c9d307c1.png">
</p>




<p align="center">
  <img width="500" height="450" src="https://user-images.githubusercontent.com/87782980/126912887-81b716e8-fbca-4291-94d5-bd4583c7d765.png">
</p>

<p align="center">
  <img width="500" height="450" src="https://user-images.githubusercontent.com/87782980/127030761-e06ac2e7-251d-41a2-8d7e-7b3f17e4071c.png">
</p>

![image](https://user-images.githubusercontent.com/87782980/126912898-5c03a885-aeb8-4e39-ab89-9f656b9760c9.png)




## Next Steps:
Given more time I would like to implement data based on the weather averages at each airport based on the time of year. I would also like to review additional flight data from other years and build a model that takes into account other various factors or reasons for delays. With this data we may be able to construct a model that not only predicts delays, but also determines the duration of the delay. 



## Acknowledgements:
Oswald Vinueza & Connor Fryar for consistent guidance and encouragement as well as their willingness to run my models on their computers. 
Drew Jones for his patience and constructive feedback. 
Justin Moon for guidance and brainstorming at a vital turning point in my project. 



