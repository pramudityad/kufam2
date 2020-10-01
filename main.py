import openweather as op
import database as db

# sunrise, sunset = op.today_sunset_sunrise()
# forecast_weather = op.today_weather()
def data_training():
	training_in, training_out = db.getTrainData()
	return training_in, training_out
# print(type(sunrise))
# print(type(sunset))
# print(type(forecast_weather))

# print(training_in)
# print(training_out)
# data_training()
# db.savetoDB(33.7,46.8,9.4)
