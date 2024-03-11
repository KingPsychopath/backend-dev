@echo off
call :check_Permissions

net stop AudioEndpointBuilder /y
net stop Audiosrv /y
net start Audiosrv /y
net start AudioEndpointBuilder /y

echo Audio Restart Complete
pause

exit /b

:check_Permissions
    echo Administrative permissions required. Detecting permissions...
	echo.
    
    net session >nul 2>&1
    if %errorLevel% == 0 (
        echo Success: Administrative permissions confirmed.
		echo.
		ping 127.0.0.1 -n 6 > nul
    ) else (
        echo Failure: Current permissions inadequate.
		echo.
		pause
		exit
    )
	goto:eof
