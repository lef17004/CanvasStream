import multiprocessing
import os

def run_script(script_path):
    os.system(f"python3 {script_path}")

if __name__ == "__main__":
    script1_path = "GameApp/server.py"  # Replace with the actual path to script1.py
    script2_path = "CanvasApp/server.py"  # Replace with the actual path to script2.py

    process1 = multiprocessing.Process(target=run_script, args=(script1_path,))
    process2 = multiprocessing.Process(target=run_script, args=(script2_path,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Both scripts have completed.")
