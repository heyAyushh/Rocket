# Rocket

IoT Smart Home Automation 

### RPi Setup

Run these commands in terminal 

```
sudo apt-get install node-red
```

Clone this [Repo](https://github.com/heyAyushh/Rocket) to your Pi
```git clone https://github.com/heyAyushh/Rocket.git```

Setup a Startup script
	so that you don't have to run it manually and it launches on startup
    
   1. Get Root Access
   
		```
		sudo -i
		```

   2. copy the contents of [runatstartup.conf](https://github.com/heyAyushh/Rocket/blob/master/runatstartup.conf)

	 	 cp /home/pi/Rocket/runatstartup.conf /etc/init
 
    
# VOILA
    
    
    