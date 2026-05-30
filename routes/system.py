from fastapi import APIRouter
from utils.command_runner import run_command

router = APIRouter()

@router.get("/uptime")
def uptime():
    return run_command("uptime")

@router.get("/disk")
def disk():
    return run_command("df -h")

@router.get("/memory")
def memory():
    return run_command("free -m")

@router.get("/user")
def user():
    return run_command("whoami")