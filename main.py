import subprocess
import sys
import os

def launch_scripts(script_paths):
    for script_path in script_paths:
        if sys.platform.startswith('win'):
            subprocess.Popen(['start', 'cmd', '/k', 'python', script_path], shell=True)
        elif sys.platform.startswith('darwin'):
            subprocess.Popen(['open', '-a', 'Terminal', 'python', script_path])
        elif sys.platform.startswith('linux'):
            subprocess.Popen(['x-terminal-emulator', '-e', 'python', script_path])
        else:
            print("Unsupported platform:", sys.platform)

if __name__ == "__main__":
    script_paths = ['CanvasApp/server.py', 'GameApp/server.py']  # Replace with your script paths
    launch_scripts(script_paths)
