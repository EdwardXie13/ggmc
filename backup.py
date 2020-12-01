import os
import subprocess
from datetime import datetime
import time

def killMC():
  subprocessA = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
  output, error = subprocessA.communicate()
  #print(output)

  for line in output.splitlines():
    print(line)
    if 'java' in str(line):
      pid = int(line.split(None, 1)[0])
      os.kill(pid, 9)

print("backup running")
while True:
  now = datetime.now()

  currentTime = now.strftime("%H:%M:%S")
  # print(currentTime)

  currentTime = currentTime.split(':')

  if(currentTime[0] == '4' and currentTime[1] == '00' and currentTime[2] =='10'):
    print("=== backup time ===")
   
    killMC()
    print("=== server killed ===")

    os.system('git add .')
    
    date = str(now).split(' ')
    command = 'git commit -m "' + date[0] + '"'

    os.system(command)

    os.system('git push origin master') 
    print("=== done pushing ===")
    
    time.sleep(3)
    
    print("=== launching server ===")
    os.system('nohup ./launch.sh > server.out')
