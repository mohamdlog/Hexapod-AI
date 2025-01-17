import os

# Point 'python' to 'python3'
os.system("cd /usr/bin && sudo rm python && sudo ln -s /usr/bin/python3 /usr/bin/python")

flag = 0x00

# 1) Install python3-venv
for x in range(1, 4):
    if os.system("sudo apt install -y python3-venv") == 0:
        flag = flag | 0x08
        break

# 2) Install gcc-aarch64-linux-gnu
for x in range(1, 4):
    if os.system("sudo apt install -y gcc-aarch64-linux-gnu") == 0:
        flag = flag | 0x10
        break

# 3) Install python3-dev
for x in range(1, 4):
    if os.system("sudo apt install -y python3-dev") == 0:
        flag = flag | 0x20
        break

# 4) Install i2c-tools
for x in range(1, 4):
    if os.system("sudo apt install -y i2c-tools") == 0:
        flag = flag | 0x40
        break

# Check if everything was installed
if flag == 0x78:  # 0x78 = 0x08 | 0x10 | 0x20 | 0x40
    print("\nNow the installation is successful.")
    print("\nPlease restart raspberry pi")
else:
    if (flag & 0x08) == 0x00:
        print("\npython3-venv install failed.")
    if (flag & 0x10) == 0x00:
        print("\ngcc-aarch64-linux-gnu install failed.")
    if (flag & 0x20) == 0x00:
        print("\npython3-dev install failed.")
    if (flag & 0x40) == 0x00:
        print("\ni2c-tools install failed.")
    print("\nSome libraries have not been installed yet. Please run 'sudo python setup.py' again")
