import os

# Point 'python' to 'python3'
os.system("cd /usr/bin && sudo rm python && sudo ln -s /usr/bin/python3 /usr/bin/python")

flag = 0x00

# 1) apt-get update
for x in range(1, 4):
    if os.system("sudo apt-get update") == 0:
        flag = flag | 0x01
        break

# 2) Install python3-venv
for x in range(1, 4):
    if os.system("sudo apt install -y python3-venv") == 0:
        flag = flag | 0x08
        break

# 3) Install gcc-aarch64-linux-gnu
for x in range(1, 4):
    if os.system("sudo apt install -y gcc-aarch64-linux-gnu") == 0:
        flag = flag | 0x10
        break

# 4) Install python3-dev
for x in range(1, 4):
    if os.system("sudo apt install -y python3-dev") == 0:
        flag = flag | 0x20
        break

# 5) rpi-ws281x-python
for x in range(1, 4):
    if os.system("cd src/Code/Libs/rpi-ws281x-python/library && sudo python3 setup.py install") == 0:
        flag = flag | 0x02
        break

# 6) mpu6050
for x in range(1, 4):
    if os.system("cd src/Code/Libs/mpu6050 && sudo python3 setup.py install") == 0:
        flag = flag | 0x04
        break

# Check if everything was installed
if flag == 0x3F:  # 0x3F = 0x01 | 0x02 | 0x04 | 0x08 | 0x10 | 0x20
    print("\nNow the installation is successful.")
    print("\nPlease restart raspberry pi")
else:
    if (flag & 0x01) == 0x00:
        print("\napt-get update failed.")
    if (flag & 0x08) == 0x00:
        print("\npython3-venv install failed.")
    if (flag & 0x10) == 0x00:
        print("\ngcc-aarch64-linux-gnu install failed.")
    if (flag & 0x20) == 0x00:
        print("\npython3-dev install failed.")
    if (flag & 0x02) == 0x00:
        print("\nrpi-ws281x-python install failed.")
    if (flag & 0x04) == 0x00:
        print("\nmpu6050-raspberrypi install failed.")
    print("\nSome libraries have not been installed yet. Please run 'sudo python setup.py' again")