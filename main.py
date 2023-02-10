import subprocess
import sys

def check_pip_install():
    completed_pip_process=subprocess.run([sys.executable, "-m", "pip","--version"], capture_output=True)
    if(completed_pip_process.returncode != 0):
        print("You need to install pip")
        user_response = input("do you want to install pip  ? y/n: ")
        if(user_response == "y"):
            subprocess.check_call([sys.executable, "-m", "ensurepip", "--upgrade"])
    else:
        print("pip version detected : " + str(completed_pip_process.stdout).split(" ")[1])

def check_venv_install():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", "virtualenv"])

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def create_virtual_env():
    install("toml")

if __name__=="__main__":
    check_pip_install()
    check_venv_install()
