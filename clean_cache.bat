@echo off
echo Cleaning Python cache and temporary files...

REM Eliminar directorios __pycache__ y .pytest_cache
for /d /r %%G in (__pycache__) do rd /s /q "%%G"
for /d /r %%G in (.pytest_cache) do rd /s /q "%%G"

REM Eliminar archivos con extensión .pyc y .pyo
for /r %%G in (*.pyc) do del /f /q "%%G"
for /r %%G in (*.pyo) do del /f /q "%%G"

echo Cache cleaned!
