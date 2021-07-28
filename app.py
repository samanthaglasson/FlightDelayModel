from flask import Flask, request, render_template, json, jsonify
import pickle
import trims 
import pandas as pd
import project_lists


app = Flask(__name__)
# temp value - to be filled in
numColumns = 3
delayed = {0:'On Time',1:'Delayed'}

airports = {}
airportsList = project_lists.airports
count = 0
for airport in airportsList:
    airports[airport] = count
    count+=1

airlines = {}
count = 0
airlinesList =project_lists.airlines
for airline in airlinesList:
    airlines[airline] = count
    count +=1

tail_numbers = {}
count = 0 
tailNumbersList = project_lists.tail_numbers
for tailNumber in tailNumbersList:
    tail_numbers[tailNumber] = count
    count +=1

days_of_week = {}
count = 1
daysOfWeekList = project_lists.DOW
for day in daysOfWeekList:
    days_of_week[day] = count
    count+=1

@app.route('/',methods=["GET","POST"])
def home():
    message = "Welcome to my flask based web application ... !!!"
    return render_template("home.html", message = message)





@app.route('/getResponseLinearReg',methods=["GET","POST"])
def getResponseLinearReg():
    
    MONTH = request.form["MONTH"]
    DAY = request.form["DAY"]
    DAY_OF_WEEK = request.form["DAY_OF_WEEK"]
    DAY_OF_WEEK = days_of_week[DAY_OF_WEEK]
    print("DAY_OF_WEEK: ", DAY_OF_WEEK)
    AIRLINE = request.form["AIRLINE"]
    AIRLINE = airlines[AIRLINE]
    print("AIRLINE: ", AIRLINE)
    FLIGHT_NUMBER = request.form["FLIGHT_NUMBER"]
    TAIL_NUMBER = request.form["TAIL_NUMBER"]
    TAIL_NUMBER = tail_numbers[TAIL_NUMBER]
    print("TAIL_NUMBER: ",TAIL_NUMBER)
    ORIGIN_AIRPORT = request.form["ORIGIN_AIRPORT"]
    ORIGIN_AIRPORT = airports[ORIGIN_AIRPORT]
    print("ORIGIN_AIRPORT:", ORIGIN_AIRPORT)
    DESTINATION_AIRPORT = request.form["DESTINATION_AIRPORT"]
    DESTINATION_AIRPORT = airports[DESTINATION_AIRPORT]
    print("DESTINATION AIRPORT:", DESTINATION_AIRPORT)
    SCHEDULED_DEPARTURE = request.form["SCHEDULED_DEPARTURE"]
    SCHEDULED_TIME = request.form["SCHEDULED_TIME"]
    DISTANCE = request.form["DISTANCE"]
    SCHEDULED_ARRIVAL = request.form["SCHEDULED_ARRIVAL"]
    holiday_season_dummy = request.form["holiday_season_dummy"]
    origin_latitude = request.form["origin_latitude"]
    origin_longitude = request.form["origin_longitude"]
    destination_longitude = request.form["destination_longitude"]
    destination_latitude = request.form["destination_latitude"]
    inputList = [MONTH, DAY, DAY_OF_WEEK, AIRLINE, FLIGHT_NUMBER, TAIL_NUMBER, ORIGIN_AIRPORT, DESTINATION_AIRPORT, SCHEDULED_DEPARTURE, SCHEDULED_TIME, DISTANCE, SCHEDULED_ARRIVAL, holiday_season_dummy, origin_latitude, origin_longitude, destination_latitude, destination_longitude] #Survived,DIS,RAD,TAX,PT,B,LSTAT]
    with open("DecisionTreeDelayModel15.pkl", 'rb') as file:
            pickle_model = pickle.load(file)
    cols = [MONTH, DAY, DAY_OF_WEEK, AIRLINE, FLIGHT_NUMBER, TAIL_NUMBER, ORIGIN_AIRPORT, DESTINATION_AIRPORT, SCHEDULED_DEPARTURE, SCHEDULED_TIME, DISTANCE, SCHEDULED_ARRIVAL, holiday_season_dummy, origin_latitude, origin_longitude, destination_latitude, destination_longitude]
    y_pred_from_pkl = pickle_model.predict(pd.DataFrame([inputList], columns=cols))
    print(y_pred_from_pkl)
    return delayed[y_pred_from_pkl[0]]



@app.route('/getAirports',methods=["GET","POST"])
def getAirports():
    print("airpots" , project_lists.airports)
    print("airports json" , json.dumps(project_lists.airports))
    return json.dumps(project_lists.airports)



@app.route('/getTailNumbers',methods=["GET","POST"])
def getTailNumbers():
    return jsonify(project_lists.tail_numbers)

if __name__ == '__main__':
    app.run(debug=True)