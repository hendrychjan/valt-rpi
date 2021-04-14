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

