
import subprocess

def run_command(command: str):
    try:
        result = subprocess.check_output(
            command,
            shell=True,
            stderr=subprocess.STDOUT,
            text=True
        )
        return {"success": True, "output": result}
    
    except subprocess.CalledProcessError as e:
        return {
            "success": False,
            "error": e.output
        }