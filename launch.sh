#1/bin/sh
nohup java -Xms2048m -Xmx4096m -jar fabric-server-launch.jar -nogui > server.out
nohup python backup.py > backup.out
