# Raspberry Pi with MBP280
> This project is dedicated to the Video Aids for Learning and Teaching project by Erasmus+
## Introduction
Hi my name is Jan, and I'll show you how to make a first step into creating your own smart home. We will be using a temperature sensor to check the room temperature, I'll introduce you to Raspberry Pi, cover up the basics of using it, we will write a simple Python program that will communicate with the temperature sensor and last but not least we will configure a server on the Raspberry Pi so that you can check the temperature anywhere from your local network. 
### Prerequisites
If you want to work with me and finish up the whole project, you will need: 
- Raspberry Pi with all the accessories such as power adapter and MicroSD Card 
- A bread board 
- Four jumper wires of type male/female 
- BMP280 sensor 
and of course a laptop or PC to do all the coding.

## What is Raspberry Pi?
Raspberry Pi is a computer about the size of a credit card with a price tag as low as $5. 1st unit was brought to the public in 2012 and now it is one of the bestselling micro computers in the world. Even though it is so tiny, it still is quite powerful. The most recent model has a quad core CPU and up to 8 GB of ram. It's use scale is huge - you can use it for many interesting projects starting from IoT prototypes, robots, automating various things, security, smart home, even hi-fi audio system, all the way to machine learning, AI, as a web server or even as a retro gaming console.

Raspberry Pi consists of a bunch of little chips and connectors.  The most important are: CPU, RAM, Wi-Fi and Bluetooth module, MicroSD card slot, Ethernet connection along with 4 USB ports, audio jack, 2 micro HDMI ports, a camera and display connector, and finally a GPO connector that you can use to control electric circuits and communicate with other electronic devices. 

Unlike Arduino, Raspberry Pi has a general-purpose operating system, that is installed on the MicroSD card that I mentioned earlier. Raspbian alongside with other Linux distributions is the most commonly used operating system for a Raspberry Pi, but you can use Windows IoT Core as well. 

And how about programming the GPIO controller, that I mentioned earlier? That is easy, because the most common programming languages like Python, Java, C#, C++, C or even JavaScript have libraries for that. 

Now that you have at least a brief understanding of Raspberry Pi, let's start with the project.

## Wiring the BMP280
First of all, we need to connect the temperature sensor to the Raspberry Pi. For that we could use either the I2C or the SPI protocol. Now, how these two work, that is quite complicated and definitely far behind the scope of this video, so I won't explain it now and I will just tell you that we are going to use the I2C protocol, that will take care of all the data transferring between sensor and Raspberry Pi.

The wiring s quite simple, we need just 4 cables for that. The first one, red, provides 3.3 V that powers the sensor. Data between Raspberry Pi and sensor are exchanged through that blue cable. Orange cable is for clock, that we use to synchronize both devices and finally black cable is ground. The 3 unused pins on temperature sensor are for SPI protocol, which is the other protocol I mentioned earlier. 
![Wiring schema](https://github.com/hendrychjan/valt-rpi/blob/58ab1f2aba4dae0022ddf2c538f6615df13636ca/wiring.png)
So, pause the video, connect the cables exactly the same as the diagram shows and also - pay attention not to have the Raspberry PI upside down - that means that the ethernet and USB ports must be on the bottom - otherwise cables would be connected wrong. 

## Installing OS
Now I'll show you how to install an operating system without even having to use an external monitor. So put the MicroSD card into your computer open up a browser of your choice, and follow my steps: 
- Head over to the https://www.raspberrypi.org/ website 
- Click on "software"
- Here, select the appropriate download link to download the RPI Imager, an application, that will make the whole installing process much easier. 
- Optionally, if you are on Linux, you can use the package manager as well. 

Now, just a quick note – you will probably see me using Linux most of the time, but no worries, the process is the same on all platforms. If there are going to be any differences in the process, I’ll let you know.   
- Open up the newly installed software 
- Choose Raspberry Pi OS Lite 
- Select the MicroSD card where you want to install the OS 
- Click on "write" and just wait for it to install 

There is one last thing before we finish the installation. Open the "boot" partition, and create an empty file without an extension, named "ssh".  

And that is it. Now, remove the MicroSD card from your computer and we can head over to the next step.

## First connection
In order to communicate with Raspberry Pi, we need to connect to its terminal. Terminal is an interface between user and computer, a place where you write text commands that are then executed directly on the layer of OS.  

So, we are going to use the computer's terminal to connect to Raspberry Pi's terminal using a utility called "ssh". In order to do that, both devices have to be on the same local network. Also, we have to determine the Raspberry Pi's IP address, to let the "ssh" know where it should connect. The process of determining the IP address is different for everyone so I won’t be explaining it, but you can check out [this link](https://www.raspberrypi.org/documentation/remote-access/ip-address.md#:~:text=Using%20the%20Pi%20with%20a%20display&text=Using%20the%20terminal%20(boot%20to,reveal%20your%20Pi's%20IP%20address) for a great guide. 

Now, the connection itself. If you are using Linux or MacOS, the system terminal will do just fine, but if you are on Windows, you have to install a software called PuTTY – that I am going to explain momentarily. But for now, let's just open up the terminal, simply type "ssh", the hostname of target device – that is "pi" in our case – and the target IP address that you determined in the previous step. Select yes to add the host to the list of trusted hosts. The device is now trusted, so connect to it again. Now type in "raspberry", which is the default password. Now, we are connected to Raspberry Pi's terminal.

## Raspbian setup
Before we can start programming, we need to setup a few things, starting with the system update. To update the system, type in ```sudo apt update```. That will search if there are any upgrades. And as you can see, there are 30 packages ready to be upgraded, so type ```sudo apt upgrade -y``` to upgrade them. This will take some time.

When it is ready, we continue with making sure the I2C interface is enabled. That is necessary in order to communicate with the temperature sensor. So, type in ```sudo raspi-config``` and there, using the keyboard arrows, select *Interface options* -> *I2C* and here *yes* to enable the I2C interface. Now, we can close this dialog by highlighting the *finish* option using tab. 

The application that we are about to write for the temperature sensor is going to be done using the Python programming language, because there is a lot of easy-to-use libraries that will make the whole process significantly easier. Also, if you are not a programmer, Python is in my opinion the best programming language a beginner can pick. So, to check if you have Python installed, simply type ```python3 –version```. If you get a result similar to mine, that means you have Python3 installed. Why Python3 you might ask? - that's because there are 2 major versions of Python: python2 and python3. Nowadays, python2 is pretty much deprecated, but for some reason, it is set as a default version in Raspbian. So, we have type python3, to force the system to use python version 3.  

As I said a while ago, we are going to use a library that provides an easy way to communicate with the temperature sensor. To use this library, we need to install it. First, type in ```sudo apt install python3-pip``` to install pip, which is a package manager – a utility for installing libraries for Python. Here, type ```y``` for yes to approve the installation. You can verify the installation by typing ```pip3 –version```. Now, we can use pip to install the library for our temperature sensor.

## Programming
Finally – we can start programming. So, make sure you are in a home directory by typing ```cd ~```. We can start off by creating a new folder called "valt" - that is where our source code is going to be. So ```mkdir valt```, and move into that folder by typing ```cd valt```. Here, create a new python file called "sensor" using the "touch" command. ```touch sensor.py``` And, open that file with nano – a simple terminal-based text editor. ```nano sensor.py```

The programming is really simple, so have no worries. Firs, we have to import these libraries:
```python
import board 
import busio
import adafruit_bmp280
```
- "board" takes care of the GPIO pins,
- "busio" takes care of the communication that is happening on the I2C line between Raspberry Pi and the temperature sensor 
- and finally, "adafruit_bmp280" is a special library for the temperature sensor 

Next, we need to initialize the i2c interface, and create a controller for the temperature sensor, and give it the I2C we initialized on the line above. 
```python
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
```

And that's it really, now we can create an infinite loop, read the temperature and pause the loop for 2 seconds, so that the temperature is refreshed every 2 seconds.
```python
while True:
    print("Temperature: " + str(sensor.temperature) + " °C")
    time.sleep(2)
```

Dont forget to import the time library on the top.
```python
import time
```

And the programming is done – it wasnt that hard, was it? Exit "nano" by pressing *ctrl+x*, *y* to save changes and *enter* to exit. Now we can test the application:
```python3 sensor.py```
The output should be similar to this:
```
Temperature: 22.51486464 °C
Temperature: 22.54848465 °C
Temperature: 22.578992148 °C
Temperature: 22.5486 °C
Temperature: 22.54864887 °C
Temperature: 22.5458 °C
Temperature: 22.512 °C
Temperature: 22.51878456 °C
Temperature: 22.5411235 °C
Temperature: 22.5789452 °C
```

As you can see, everything works perfectly. Only, in my opinion, the measurement is too accurate, which means there is a lot of decimal places. To fix that, first stop the code execution by pressing *ctrl+c*, open up nano again, save the temperature to a variable, round it to 2 decimal places, repeat the same exit process as last time, and test the application. 
The whole ```sensor.py``` should look like so:
```python
import board
import busio
import adafruit_bmp280
import time

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

while True:
    temp = round(sensor.temperature, 2)
    print("Temperature: " + str(temp) + " °C")
    time.sleep(2)
```
Now, the output should look like following:
```
Temperature: 22.51 °C
Temperature: 22.5 °C
Temperature: 22.5 °C
Temperature: 22.5 °C
Temperature: 22.5 °C
Temperature: 22.5 °C
Temperature: 22.5 °C
Temperature: 22.51 °C
Temperature: 22.5 °C
Temperature: 22.5 °C
```