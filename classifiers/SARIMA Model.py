from pandas import datetime
from pandas import read_csv
from pandas import DataFrame
from matplotlib import pyplot
import pmdarima as pm
from pmdarima.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

##### Step 1 - Data Preprocessing

### TODO 1
days = ENTER THE DATES IN MM/DD/YY format

#formate your dates accordingly
formatted_days_for_arima = []
for i in days:
  date_time_str = i
  date_time_obj = datetime.strptime(date_time_str, '%m/%d/%y')
  formatted_days_for_arima.append(str(date_time_obj.year)+"-"+str(date_time_obj.month)+"-"+str(date_time_obj.day))

  
###TODO 2
ENTER_YOUR_DATA_VALUES = list of values like [5 10 25 30] 

arima_df = pd.DataFrame(
    {'Months': formatted_days_for_arima,
     'Cases': ENTER_YOUR_DATA_VALUES
    })


arima_df.to_csv('arima_pred.csv',index=False)


##### Step 2 - Run Classifier

# load dataset
series = read_csv('arima_pred.csv', header=0, index_col=0, parse_dates=True, squeeze=True)


# Create model for forecast
smodel = pm.auto_arima(series, start_p=1, start_q=1,
                         test='adf',
                         max_p=3, max_q=3, m=12,
                         start_P=0, seasonal=True,
                         d=None, D=1, trace=True,
                         error_action='ignore',
                         suppress_warnings=True,
                         stepwise=True)

print(smodel.summary())

# Forecast
timetravel =  arima_df['Months']
n_periods = 10
fitted, confint = smodel.predict(n_periods=n_periods, return_conf_int=True,)
index_of_fc = pd.date_range(timetravel[len(timetravel)-1], periods = n_periods, freq='D')


# make series for plotting purpose
fitted_series = pd.Series(fitted, index=index_of_fc)
lower_series = pd.Series(confint[:, 0], index=index_of_fc)
upper_series = pd.Series(confint[:, 1], index=index_of_fc)

# Plot
plt.plot(series)
plt.plot(fitted_series, color='darkgreen', label="Predicted Forecast of next 10 days")
plt.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)
plt.fill_between(lower_series.index,
                 lower_series,
                 upper_series,
                 color='k', alpha=.15)

plt.title("SARIMA - Final Forecast of COVID-19")
plt.show()

