import smtplib
from readInPersonal import PersonalData
from weather import Weather

def send_message(information, body):
    recipient = information.get('phone') + "@msg.telus.com"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(information.get('email'), information.get('password'))

        subject = "Weather Update"
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
    body = weather.get_weather_report()
    send_message(information, body)
