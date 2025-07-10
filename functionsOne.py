
def department_finishing1(x):
    if x == 'department_finishing':
        y = 1
    else:
        y = 0
    return y

def department_sweing1(x):
    if x == 'department_sweing':
        y = 1
    else:
        y = 0
    return y

def quarter_11(x):
    if x == 'quarter1':
        y = 1
    else:
        y = 0
    return y

def quarter_21(x):
    if x == 'quarter2':
        y = 1
    else:
        y = 0
    return y

def quarter_31(x):
    if x == 'quarter3':
        y = 1
    else:
        y = 0
    return y

def department_finishing1(x):
    if x == 'department_finishing':
        y = 1
    else:
        y = 0
    return y

def quarter_41(x):
    if x == 'quarter4':
        y = 1
    else:
        y = 0
    return y

def week_day_Monday1(x):
    if x == 'option1':
        y = 1
    else:
        y = 0
    return y

def week_day_Tuesday1(x):
    if x == 'option2':
        y = 1
    else:
        y = 0
    return y

def week_day_Wednesday1(x):
    if x == 'option3':
        y = 1
    else:
        y = 0
    return y

def week_day_Thursday1(x):
    if x == 'option4':
        y = 1
    else:
        y = 0
    return y

def week_day_Saturday1(x):
    if x == 'option5':
        y = 1
    else:
        y = 0
    return y

def week_day_Sunday1(x):
    if x == 'option6':
        y = 1
    else:
        y = 0
    return y

def actual_productivity_Low1(x):
    if x == 'Low':
        y = 1
    else:
        y = 0
    return y

def actual_productivity_Mid1(x):
    if x == 'Mid':
        y = 1
    else:
        y = 0
    return y

def actual_productivity_High1(x):
    if x == 'High':
        y = 1
    else:
        y = 0
    return y

def actual_productivity_Very_H1(x):
    if x == 'Very H.':
        y = 1
    else:
        y = 0
    return y
    
def flager(row):
    row['itsVH'] = row['incentive'] >= 70
    row['itsH'] = row['department_sweing'] == 1
    row['itsL'] = row['incentive'] == 0
    row['itsH'] = row['incentive'] == 50
    
    return row

def theLastFunction_OnlyObjectsForNowOn(value) -> str:
    if value == 'Mid':
        value = 'Average'
    elif value == 'Very H.':
        value = 'Exceptional'
    else:
        return value
        
    return value 