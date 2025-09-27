import os
import os.path
from sys import platform

work_dir = "c:/path/"
new_dir = "path"
user = os.getlogin()
print(user)

print(platform)

if platform == "linux" or platform == "linux2":
    print("linux")
elif platform == "darwin":
    print("darwin")
elif platform == "win32":
    print("Windows")