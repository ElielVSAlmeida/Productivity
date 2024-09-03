from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
import functionsOne as one

# Import Models
modelClassifier = pickle.load(open(r'machines/productivity_classifier.p', 'rb'))
modelRegressor = pickle.load(open(r'machines/productivity_regressor.p', 'rb'))
scalerC = pickle.load(open(r'machines/scaler.p', 'rb'))
scalerR = pickle.load(open(r'machines/scalerReg.p', 'rb'))

# Creating flask app object

app = Flask(__name__)

# The main route - Homepage

@app.route('/', methods= ['POST', 'GET'])
def homepage():
    if request.method == 'POST':
        try:
            # Bool Columns
            quarter = str(request.form["quarter"])
            department = str(request.form["department"])
            week_day = str(request.form["week_day"])

            # Getting input for Raw columns
            team = int(request.form["team"]) or 8
            targeted_productivity = float(request.form["targeted_productivity"]) or 0.70
            smv = float(request.form["smv"]) or 3.90
            wip = float(request.form["wip"]) or 0.0
            over_time = float(request.form["over_time"]) or 960.0
            incentive = float(request.form["incentive"]) or 0.0
            idle_time = float(request.form["idle_time"]) or 0.0
            idle_men = float(request.form["idle_men"]) or 0.0
            no_of_style_change = float(request.form["no_of_style_change"]) or 0
            no_of_workers = float(request.form["no_of_workers"]) or 8.0
            day = int(request.form["day"]) or 15
            month = int(request.form["month"]) or 2
            quarter_1 = one.quarter_11(quarter) or 0
            quarter_2 = one.quarter_21(quarter) or 1
            quarter_3 = one.quarter_31(quarter) or 0
            quarter_4 = one.quarter_41(quarter) or 0
            department_finishing = one.department_finishing1(department) or 1
            department_sweing = one.department_sweing1(department) or 0
            week_day_Monday = one.week_day_Monday1(week_day) or 0
            week_day_Saturday = one.week_day_Saturday1(week_day) or 0
            week_day_Sunday = one.week_day_Sunday1(week_day) or 0
            week_day_Thursday = one.week_day_Thursday1(week_day) or 0
            week_day_Tuesday = one.week_day_Tuesday1(week_day) or 0
            week_day_Wednesday = one.week_day_Wednesday1(week_day) or 1
            itsVH= False
            itsH= False
            itsL= False
                
            # Create Array
            inputClassifier = np.array([[team, targeted_productivity, smv, wip, over_time, incentive,
                                        idle_time, idle_men, no_of_style_change, no_of_workers, day,
                                        month, quarter_1, quarter_2, quarter_3, quarter_4,
                                        department_finishing, department_sweing, week_day_Monday,
                                        week_day_Saturday, week_day_Sunday, week_day_Thursday,
                                        week_day_Tuesday, week_day_Wednesday, itsVH, itsH, itsL]])
            df = pd.DataFrame(inputClassifier, columns=['team', 'targeted_productivity', 'smv', 'wip', 'over_time', 'incentive',
                                                        'idle_time', 'idle_men', 'no_of_style_change', 'no_of_workers', 'day',
                                                        'month', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4',
                                                        'department_finishing', 'department_sweing', 'week_day_Monday',
                                                        'week_day_Saturday', 'week_day_Sunday', 'week_day_Thursday',
                                                        'week_day_Tuesday', 'week_day_Wednesday', 'itsVH', 'itsH', 'itsL'])

            df = df.apply(one.flager, axis=1)
            df1 = scalerC.transform(df)
            result1 = modelClassifier.predict(df1)

            actual_productivity_Low = one.actual_productivity_Low1(result1[0]) or 0
            actual_productivity_Mid = one.actual_productivity_Mid1(result1[0]) or 1
            actual_productivity_High =one.actual_productivity_High1(result1[0]) or 0
            actual_productivity_Very_H = one.actual_productivity_Very_H1(result1[0]) or 0

            inputRegressor = np.array([[team, targeted_productivity, smv, wip, over_time, incentive,
                                        idle_time, idle_men, no_of_style_change, no_of_workers, day,
                                        month, quarter_1, quarter_2, quarter_3, quarter_4,
                                        department_finishing, department_sweing, week_day_Monday,
                                        week_day_Saturday, week_day_Sunday, week_day_Thursday,
                                        week_day_Tuesday, week_day_Wednesday, actual_productivity_Low,
                                        actual_productivity_Mid, actual_productivity_High,
                                        actual_productivity_Very_H]])
            dfR = pd.DataFrame(inputRegressor, columns=['team', 'targeted_productivity', 'smv', 'wip', 'over_time', 'incentive',
                                                        'idle_time', 'idle_men', 'no_of_style_change', 'no_of_workers', 'day',
                                                        'month', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4',
                                                        'department_finishing', 'department_sweing', 'week_day_Monday',
                                                        'week_day_Saturday', 'week_day_Sunday', 'week_day_Thursday',
                                                        'week_day_Tuesday', 'week_day_Wednesday', 'actual_productivity_Low',
                                                        'actual_productivity_Mid', 'actual_productivity_High',
                                                        'actual_productivity_Very H.'])
            
            dfR1 = scalerR.transform(dfR)
            result2 = modelRegressor.predict(dfR1)

            stringC = f"Based on the on the chossen parameters the productivity is {result1[0]}!"
            
            stringR = f"Prodictivity Estimate : {round(result2[0], 4)*100}%"

            return render_template('main.html', my_result = stringC, result = stringR)
        except:
            return render_template('second.html')
    else:
        stringC = ""
        stringR = ""

        return render_template('main.html', my_result = stringC, result = stringR)
    

if __name__ == '__main__':
    app.run(debug=True)
