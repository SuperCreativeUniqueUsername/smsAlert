import smtplib
from readInPersonal import PersonalData
from weather import Weather

def send_message(information, subject ,body):
    recipient = information.get('phone') + "@msg.telus.com"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(information.get('email'), information.get('password'))
        message = f"Subject: {subject}\n\n{body}"

        server.sendmail(information.get("email"), recipient, message)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()
        
if __name__ == "__main__":
    information = PersonalData('personal')
    information.read_file()
    weather = Weather(float(information.get('X')), float(information.get('Y')))  
    #send_message(information, "Weather Report", weather.get_weather_report())
    #send_message(information, "Hourly Forecast", weather.get_hourly_forecast())
    print(weather.get_AQHI_forecast())
    #send_message(information, "AQHI Forecast", weather.get_AQHI_forecast())
