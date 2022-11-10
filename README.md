# Safety-turn-off-RPi4
Place the file `ShutdownRPi4ByConnectPin40toPin39.py` in the home/pi/ folder

Add to the script in aгtostart. Execute commands in terminal:

`sudo nano /etc/xdg/lxsession/LXDE-pi/autostart`

Add command to file:

`python3 /home/pi/ShutdownRPi4ByConnectPin40toPin39.py`

Restat RPi

Enjoy.