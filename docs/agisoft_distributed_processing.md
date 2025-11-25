# Agisoft Distributed Processing

The following instructions are for processing on a single PC, no networking. To distribute across multiple PC's other steps need to be implemented which are not covered here.

## Steps
Step 0 - Get IP Address using CMD 'ipconfig', copy and paste the value adjacent to 'IPv4 Address' into next step.

Step 1 - Create a server file with the following contents and save as server.bat

<pre>"C:/Program Files/Agisoft/Metashape Pro/metashape-server.exe" --server 10.136.51.10 --control 10.136.51.10
  
pause</pre>

Step 2 - Create a node file with the following contents and save as node.bat

<pre>"C:\Program Files\Agisoft\Metashape Pro\metashape.exe" --node --host 10.136.51.10 --root D:\_RPA_Processing\Stage2\WECW010026
  
pause</pre>

Step 3 - In the following order double click on 

1. server.bat (The following will display)

<img src="https://github.com/berlinbabel/aerial_workflow/blob/main/img/server.png"/>
   
2. node.bat (The following will display)
<img src="https://github.com/berlinbabel/aerial_workflow/blob/main/img/node.png"/>

Step 4 - Open the following app C:\Program Files\Agisoft\Metashape Pro\monitor.exe

Step 5 - Enter
1. Host name:(IP Address)
2. Port: 5840
3. Hit Connect

Step 6 - Agisoft monitor will look something like this

<img src="https://github.com/berlinbabel/aerial_workflow/blob/main/img/agisoft_monitor.png"/>
