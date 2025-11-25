# Agisoft Distributed Processing
## Steps
Step 1 - Create a server file with the following contents and save as server.bat

<pre>"C:/Program Files/Agisoft/Metashape Pro/metashape-server.exe" --server 10.136.51.10 --control 10.136.51.10
pause</pre>

Step 2 - Create a node file with the following contents and save as node.bat

<pre>"C:\Program Files\Agisoft\Metashape Pro\metashape.exe" --node --host 10.136.51.10 --root D:\_RPA_Processing\Stage2\WECW010026
pause</pre>
