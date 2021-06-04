#Scan ports for vulnerabilites

#Import modules
import socket
import subprocess
import os
from datetime import datetime, time
import time

#Create a function to facilitate scan
def CheckPort(host, port):
    s=socket.socket()
    try:
        s.connect((host,port))
    except:
        return False
    else:
        return True

#Create a new file and delete previous file if it exists
#Need to update file path
if os.path.exists("C:/Users/kyle/Documents/PythonFiles/PortScanResults.txt"):
    os.remove("C:/Users/kyle/Documents/PythonFiles/PortScanResults.txt")
#Open the file and write to it
xfile = open("C:/Users/kyle/Documents/PythonFiles/PortScanResults.txt", "a+")

#Prompt the user
host = input("Hello! I am at your service. Please provide an IP address to scan: ")
FirstPort = int(input('OK, I am ready. Please provide the port number you would like me to start with: '))
LastPort = int(input('One last request. What is the last port number you would like me to scan: '))
CheckRange = range(FirstPort, LastPort+1, 1)

#Get the time
CurrentTime = datetime.now()
dt_string = CurrentTime.strftime("%m/%d/%Y %H:%M:%S")
start = time.time()

#Verify host is alive
command_line = (["ping -n 1 "], host)
PingResult = subprocess.Popen(command_line,stdout=subprocess.PIPE).communicate()[0]
StatusCheck = str(PingResult)
#Print the status check
if (StatusCheck.find("unreachable") != -1):
    print(host, "is unreachable. Will now abort scan.")
    PrintIt = [host, "is unreachable.  The scan was aborted at", dt_string, "\n"]
    WriteIt = ' '.join(PrintIt)
    xfile.write(WriteIt)
    xfile.close()
    exit()
elif (StatusCheck.find("Received = 0") != -1):
    print(host, "is not responding. Will now abort scan.")
    PrintIt = [host, "is not responding.  The scan was aborted at", dt_string, "\n"]
    WriteIt = ' '.join(PrintIt)
    xfile.write(WriteIt)
    xfile.close()
    exit()
elif (StatusCheck.find("could not find") != -1):
    print(host, "cannot be found. Will now abort scan.")
    PrintIt = [host, "cannot be found.  The scan was aborted at", dt_string, "\n"]
    WriteIt = ' '.join(PrintIt)
    xfile.write(WriteIt)
    xfile.close()
    exit()
elif (StatusCheck.find("Received = 1") != -1):
    print(host, "is found. Starting the scan now.")
    print("Scan is starting at: ", dt_string)
    PrintIt = [host, "is found. Starting the scan at", dt_string, "\n"]
    WriteIt = ' '.join(PrintIt)
    xfile.write(WriteIt)
else:
    print("Oh no! Something strange happened. Please try again.")
    exit()

#Let the user know you are on it
print("Take a load off and rest assured I am starting the scan now.")

#Check the ports
for x in CheckRange:
    if CheckPort(host,x):
        print("Port ", x, " is open")
        CheckIt = ["Port", str(x), " is open", "\n"]
        WriteIt = ' '.join(CheckIt)
        xfile.write(WriteIt)
    else:
        print('Port', x, ' is closed.')
        CheckIt = ["Port", str(x), "is closed.", "\n"]
        WriteIt = ' '.join(CheckIt)
        xfile.write(WriteIt)

#Finish the scan and notify user
FinishTime = time.time()
print("Scan is finished. Port range", FirstPort, " - ", LastPort, " has been scanned.")
TotalTime = FinishTime - start
CurrentTime = datetime.now()
dt_string = CurrentTime.strftime("%m/%d/%Y %H:%M:%S")
print("The scan was completed at: ", dt_string)
print("The scan took:", "%.2f" % TotalTime, "seconds.")
FinishIt = ["The scan was completed at: ", str(dt_string), "\n"]
FinalVar = ' '.join(FinishIt)
xfile.write(FinalVar)
FinishIt = ["Total scan time:", "%.2f" % TotalTime, "seconds.", "\n"]
FinalVar = ' '.join(FinishIt)
xfile.write(FinalVar)
xfile.close()








