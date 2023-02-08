from datetime import datetime
import pytz

melbourne = pytz.timezone("Australia/Melbourne")
melbourne_date = datetime.now(melbourne)

print("Melbourne:", melbourne_date.strftime('%d/%m/%Y, %H:%M:%S'))

cdmx = pytz.timezone("America/Mexico_City")
cdmx_date = datetime.now(cdmx)

print("Ciudad de México:", cdmx_date.strftime('%d/%m/%Y, %H:%M:%S'))

tijuana = pytz.timezone("America/Tijuana")
tijuana_date = datetime.now(tijuana)

print("Tijuana:", tijuana_date.strftime('%d/%m/%Y, %H:%M:%S'))
print(type(tijuana_date))
print(type(melbourne_date))
