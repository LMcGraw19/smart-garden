# To set up Raspberry Pi to send and receive over LoRa  

Connect the LoRa Hat to the Raspberry Pi, All pins are used.  

Connect the Raspberry Pi to a monitor and a power source and boot up the Raspberry Pi (Depending on the monitor, keyboard and mouse can wither be connected to monitor or the Raspberry Pi itself).  

Connect Pi to wifi or ethernet  

Open a terminal  

Ensure that SPI master driver is enabled (default disabled). To do this in the terminal   

`sudo raspi-config`

It will be option 3, you can also enable SSH and can connect to the Raspberry Pi this way instead.  

Once done finish and enter into terminal  

`wget https://codeload.github.com/dragino/rpi-lora-tranceiver/zip/master` 

Then unzip   

`unzip master`  

Go into folders to make  

`cd rpi-lora-tranceiver-master/dragino_lora_app`

`Make`

Depending on permissions, sudo might have to be used to execute step 9.    

To run the sender   

`sudo ./dragino_lora_app sender`  
![Picture1](https://user-images.githubusercontent.com/78489501/116412506-aa0ef100-a82e-11eb-8d4d-0c87c388ba4d.png)

To run the receiver  

`sudo ./dragino_lora_app rec` 
![Picture2](https://user-images.githubusercontent.com/78489501/116412988-1a1d7700-a82f-11eb-9941-56a0f6c4dd07.png)

This is between two Raspberry Pis.

# To set up the T-Beam to send to the Raspberry Pi.  

For a simple string message being sent, Download the ”SmartGarden.ino” and “images.h” files  

  

Make sure the relevant drivers are installed to allow the T-Beam to have a sketch written to it.   

https://blog.bachi.net/?p=8434  

As ESP32 is not an Arduino Board you will need to install esp32 platform.  

https://github.com/espressif/arduino-esp32/blob/master/docs/arduino-ide/boards_manager.md  

Once installed, Select the correct Board, the one used in this example is TTGO T1.  

Make sure the relevant packages are installed through the Library Manager  

LoRa by sandeepmistry  

Adafruit SSD1306 by Adafruit  

ESP8266 and ESP32 OLED driver for SSD1306 displays by ThingPulse, Fabrice Weinberg  

Upload sketch to the T-Beam, it will start sending packets once uploaded. To view, use the Serial Monitor found in Tools.  
![Picture3](https://user-images.githubusercontent.com/78489501/116412995-1b4ea400-a82f-11eb-9266-7bd82dfd1816.png)


Once the T-Beam is running, run the receiver code on the Raspberry Pi.  
![Picture4](https://user-images.githubusercontent.com/78489501/116412998-1be73a80-a82f-11eb-9f10-723ee3a6b4cc.png)


# Edit main file to convert lora packet to .json 

In rpi-lora-tranceiver-master/dragino_lora_app go into the main.c file 

`nano main.c `

At the top of the file under the #include add 

`#include <python2.7/Python.h>`


Go down the file to the function void receivepacket(). Under the numerous printf statements (Which can be removed if wished) and insert: 

  
`FILE *fptr;`

`fptr = fopen("program.txt","a+");`

`if(fptr == NULL)`
`{` 
    `printf("Error!");` 
    `exit(1);`              
`}`
`char *p;` 

`p = strtok(message, "\n :");` 

`while(p != NULL)` 
`{` 
    `fprintf(fptr,"%s ",p);` 
    `p= strtok(NULL, "\n :");` 
`}` 

`fclose(fptr);`  

`Py_Initialize();` 

`PyObject* PyFileObject = PyFile_FromString("pyFile.py", "r");` 

`PyRun_SimpleFileEx(PyFile_AsFile(PyFileObject), "pyFile.py", 1);` 

`//PyRun_SimpleString("print('This is a test to check Python')");` 

`Py_Finalize();`

Then exit and save the file. 

Now create a new python file called pyFile 

`Nano pyFile.py`

And now paste in the following code: 

`import json` 
`import os` 
`import re`

`with open ("program.txt", "rt") as myfile:` 
    `for myline in myfile:` 
        `release = re.sub(r"(?<=\d)\s+", "\n", myline)` 
`#print(release)` 
`#myfile.close()`

`with open("program2.txt", "w") as f:` 
    `f.write(release)` 
`f.close()`

`filename = "program2.txt"`
`dict1 = {}`
`with open(filename) as fh:` 
    `for line in fh:` 
          `command, description = line.strip().split(None,1)`
           `dict1[command] = description.strip()`

`with open('testData.json','w') as json_file:` 
     `json.dump(dict1, json_file)`

Save and exit the file. 

Last to edit is the Makefile which compiles the files 

`nano Makefile` 

in the section ‘dragino_lora_app: main.o’ after $(CC) add 

`-I/usr/include/python2.7`  

Make sure this is before the main.o. 

After main.o add 

`-lpython2.7`

Save and exit. 

  
Compile and then run LoRa receiver 

`make` 

`sudo ./dragino_lora_app rec` 


