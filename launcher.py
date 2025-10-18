import subprocess

subprocess.Popen(
    'start cmd /k "mode con: cols=120 lines=50 && python main.py"',
    shell=True
)
