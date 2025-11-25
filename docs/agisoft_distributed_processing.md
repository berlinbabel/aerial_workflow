# Agisoft Distributed Processing
## Steps
Step 0 - Get IP Address using CMD 'ipconfig', copy and paste the value adjacent to 'IPv4 Address' into next step.

Step 1 - Create a server file with the following contents and save as server.bat

<pre>"C:/Program Files/Agisoft/Metashape Pro/metashape-server.exe" --server 10.136.51.10 --control 10.136.51.10
  
pause</pre>

Step 2 - Create a node file with the following contents and save as node.bat

<pre>"C:\Program Files\Agisoft\Metashape Pro\metashape.exe" --node --host 10.136.51.10 --root D:\_RPA_Processing\Stage2\WECW010026
  
pause</pre>

Step 3 - In the following order double click on (1) server.bat and (2) node.bat

Step 4 - Open the following app C:\Program Files\Agisoft\Metashape Pro\monitor.exe

Step 5 - Enter
1. Host name:(IP Address)
2. Port: 5840
3. Hit Connect

Step 6 - Agisoft monitor will look something like this

Image Here 
