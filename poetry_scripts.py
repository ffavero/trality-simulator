import subprocess


def generate_setup():
    cmd = ["poetry2setup", ">", "setup.py"]
    subprocess.run(cmd)
