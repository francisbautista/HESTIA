import datetime  # Importing the datetime library
import telepot   # Importing the telepot library
from telepot.loop import MessageLoop    # Library function to communicate with telegram bot
import RPi.GPIO as GPIO     # Importing the GPIO library to use the GPIO pins of Raspberry pi
from time import sleep      # Importing the time library to provide the delays in program

now = datetime.datetime.now() # Getting date and time

GPIO.setmode(GPIO.BOARD)            #Set GPIO to pin numbering
PIR = 11                             #Assign pin 8 to PIR                          #Assign pin 10 to LED
GPIO.setup(PIR, GPIO.IN)            #Setup GPIO pin PIR as input


def handle(msg):
    chat_id = msg['chat']['id'] # Receiving the message from telegram
    command = msg['text']   # Getting text from the message

    print ('Received:')
    print(command)

    # Comparing the incoming message to send a reply according to it
    if command == '/hi':
        bot.sendMessage (chat_id, str("Hi! MakerPro"))
    elif command == '/time':
        bot.sendMessage(chat_id, str("Time: ") + str(now.hour) + str(":") + str(now.minute) + str(":") + str(now.second))
    elif command == '/date':
        bot.sendMessage(chat_id, str("Date: ") + str(now.day) + str("/") + str(now.month) + str("/") + str(now.year))
    else:
        bot.sendMessage(chat_id, "Whatever")


# Insert your telegram token below
bot = telepot.Bot('1550414528:AAGq2XfHNjt45dzglVIbErxuPiYUgFqHBdo')
print (bot.getMe())

# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, handle).run_as_thread()
print ('Listening....')

while 1:
    sleep(10)

def main():
    print ("Sensor initializing . . .")
    time.sleep(2)                       #Give sensor time to startup
    print ("Active")
    print ("Press Ctrl+c to end program")

    try:
        while True:
            camera.wait_recording(1)
            if GPIO.input(pir) == True:      #If PIR pin goes high, motion is detected
                print ("Motion Detected!")
                time.sleep(5)
                if GPIO.input(pir) == True:
                    print ("A lot of motion detected! Recording video.")        
                    capture_video()
                print ("Resetting")                        #Turn off LED
        time.sleep(0.1)

    except KeyboardInterrupt:           #Ctrl+c
        pass                              #Do nothing, continue to finally
            
    finally:
        GPIO.cleanup()                    #reset all GPIO
        print ("Program ended")

def capture_video():
    GPIO.output(led, True)
    now = datetime.now().time()
    now = now.strftime("%H:%M:%S")

    camera.wait_recording(30)
    capture_image()    
    stream.copy_to(now + 'motion.h264')
    GPIO.output(led, False)  

def capture_image():
    now = datetime.now().time()
    now = now.strftime("%H:%M:%S")
    camera.capture(now + 'image.jpg', use_video_port=True)
  
if __name__== "__main__":
  main()