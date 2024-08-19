@echo off
setlocal

rem Get the directory of the batch file
set "batch_dir=%~dp0"

rem Run pins.exe from the parent directory
start "" "%batch_dir%..\pins.exe"

rem Run the Python script from the same directory as the batch file
python "%batch_dir%python_script.py"

rem Optional: Pause to see output (remove if not needed)
pause
