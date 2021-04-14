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