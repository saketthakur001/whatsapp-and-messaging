
import pywhatkit
import datetime

def send_whatsapp_message(number, message, time=None, delay=5):
  # add +91 to the number
  number = "+91" + number
  # if time is given, split it into hour and minute
  if time:
    hour, minute = time
  # else, use the current time
  else:
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 1
  # send the message with the given delay time
  pywhatkit.sendwhatmsg(number, message, hour, minute, wait_time=delay)


def send_whatsapp_message(number, message, time=None, delay=5):
#
  """Sends a WhatsApp message to a given number using PyWhatKit.

  This function uses the PyWhatKit library to send WhatsApp messages through the WhatsApp web client. It requires the user to be logged in to WhatsApp web in the default browser and to keep the phone connected to the internet. It opens WhatsApp web 15 seconds before the specified time to load the website and then sends the message with the given delay time.

  Parameters
  ----------
  number : str
    The phone number of the recipient without the country code. The function will add +91 to the number as the Indian code.
  message : str
    The message content to be sent.
  time : tuple of int, optional
    A tuple of hour and minute in 24-hour format when the message should be sent. If not given, the function will use the current time plus one minute. (default None)
  delay : int, optional
    The delay time in seconds before the message is delivered. The default value is 5 seconds. It should not be less than 4 seconds. (default 5)

  Returns
  -------
  None

  Raises
  ------
  AttributeError
    If PyWhatKit is not installed or imported correctly.
  ValueError
    If the number or message is not in string format, or if the hour or minute is not in valid range.
  Exception
    If there is any other error in sending the message.

  Examples
  --------
  >>> send_whatsapp_message("xxxxxxxx", "Hello", (11, 1), 10)
  This will send a message "Hello" to +91xxxxxxxx at 11:01 AM with a delay time of 10 seconds.

  >>> send_whatsapp_message("xxxxxxxx", "Hello")
  This will send a message "Hello" to +91xxxxxxxx at the current time plus one minute with a delay time of 5 seconds.
  
  """
# add +91 to the number
  number = "+91" + number
  # if time is given, split it into hour and minute
  if time:
    hour, minute = time
  # else, use the current time
  else:
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 1
  # send the message with the given delay time
  pywhatkit.sendwhatmsg(number, message, hour, minute, wait_time=delay)


people = {
    "saket": "8002412468",
}


if __name__ == "__main__":
    # number of the receiver
    number = people["saket"]
    # message to be sent
    message = "Hello World!"
    # time at which the message is to be sent
    # time = (12, 30)
    # send the message
    send_whatsapp_message(number, message)