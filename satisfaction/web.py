from flask import Flask,render_template,request
import pickle
import numpy as np
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/feedback',methods=['POST'])
def feedback():
    ## we did one hot encoding, so for each encoded we initialze a zero filled array
    ## there are three classes so 3 is used
    
    Class_arr=list()
    Customer_Type_arr=list()
    Type_Of_Travel_arr=list()
    Gender_arr=list()
    if request.method=='POST':
        Class=request.form['Class']
        if Class=='Business':
            Class_arr=Class_arr+[1,0,0]
        elif Class=='Eco':
            Class_arr=Class_arr+[0,1,0]
        elif Class=='EcoPlus':
            Class_arr=Class_arr+[0,0,1]
        Customer_Type=request.form['Customer_Type']
        if Customer_Type=='Yes':
            Customer_Type_arr=Customer_Type_arr+[1,0]
        elif Customer_Type=='No':
            Customer_Type_arr=Customer_Type_arr+[0,1]
        Type_Of_Travel=request.form['Type_of_Travel']
        if Type_Of_Travel=='Business':
            Type_Of_Travel_arr=Type_Of_Travel_arr+[1,0]
        elif Type_Of_Travel=='Personal':
            Type_Of_Travel_arr=Type_Of_Travel_arr+[0,1]
        Gender=request.form['Gender']
        if Gender=='Female':
            Gender_arr=Gender_arr+[1,0]
        elif Gender=='Male':
            Gender_arr=Gender_arr+[0,1]
        
        ## rest all columns
        Age=int(request.values['Age'])
        Flight_Distance=int(request.values['Flight_Distance'])
        Departure_Delay_in_Minutes=float(request.values['Departure_Delay_in_Minutes'])
        Arrival_Delay_in_Minutes=float(request.values['Arrival_Delay_in_Minutes'])

        ## all ratings
        Inflight_wifi_service=int(request.values['Inflight_wifi_service'])
        Departure_Arrival_time_convenient=int(request.values['Departure/Arrival_time_convenient'])
        Ease_of_Online_booking=int(request.values['Ease_of_Online_booking'])
        Gate_location=int(request.values['Gate_location'])
        Food_and_drink=int(request.values['Food_and_drink'])
        Online_boarding=int(request.values['Online_boarding'])
        Seat_comfort=int(request.values['Seat_comfort'])
        Inflight_entertainment=int(request.values['Inflight_entertainment'])
        On_board_service=int(request.values['On_board_service'])
        Leg_room_service=int(request.values['Leg_room_service'])
        Baggage_handling=int(request.values['Baggage_handling'])
        Checkin_service=int(request.values['Checkin_service'])
        Inflight_service=int(request.values['Inflight_service'])
        Cleanliness=int(request.values['Cleanliness'])

        ## now create the final input structure
        row=list()
        temp=[]
        temp.extend([Age,Flight_Distance, Inflight_wifi_service, Departure_Arrival_time_convenient, Ease_of_Online_booking, Gate_location, Food_and_drink, Online_boarding, Seat_comfort, Inflight_entertainment, On_board_service, Leg_room_service, Baggage_handling, Checkin_service, Inflight_service, Cleanliness, Departure_Delay_in_Minutes, Arrival_Delay_in_Minutes])
        row=row+temp+Gender_arr+Customer_Type_arr+Type_Of_Travel_arr+Class_arr
        output=int(model.predict([row])[0])
        if(output==0):
            return render_template ('predict.html',prediction_text="Thank you for your time. We will work on our best to improve ourselves".format(output))
        elif(output==1):
            return render_template ('predict.html',prediction_text="Thank you for your time. We are glad that we could satisfy your needs. We will surely try to maintain our reputation everytime you travel by our airlines.".format(output))
if __name__=='__main__':
    app.run(port=8000,debug=True)
