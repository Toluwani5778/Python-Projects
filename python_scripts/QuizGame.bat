@echo off
title QUIZ GAME!
color 0a

 :menu
cls
echo Welcome, to ......... DA MENU!
echo ----------------------------
pause
echo From here you can........
echo ------------------------
echo.
echo 1. Start
echo 2. Info
echo 3. Exit
pause

set /p menuchoice=

if %menuchoice% == 1 goto startgame
if %menuchoice% == 2 goto info
if %menuchoice% == 3 exit
goto menu

:info
cls
title Information on the Quiz!
color 0b
pause
echo This quiz is highly awesome! Please use at your own risk! To...
echo Continue using this game...
pause
cls
goto menu

:startgame
cls
title Prepare... To start the QUIZ!
color 1a
echo Please enter your name...
echo.

set /p player=
echo.
echo Press any key to start, THE QUIZ
pause >nul
goto q1

:q1
cls
title Question 1!
cls
echo Question 1
echo ----------
echo.
echo Who created this program?
echo.
echo A) Hacker
echo B) Toluwani
echo C) Bill Gates
echo D) A random guy on youtube
echo. 
set /p ans1=

if %ans1% == a goto wr1
if %ans1% == b goto cr1
if %ans1% == c goto wr1
if %ans1% == d goto wr1
goto q1

:wr1
cls 
title You LOSE! HA ha! >:D
color 9a
echo Sorry, %player%... But you lost :'(
echo.
echo Press any key to return to the menu...
pause >nul
goto menu

:cr1
cls
title YOU ARE CORRECT! :3
color 9a
echo Congratz! You got this question, correct! Well done, %player%!
echo.
echo Press any key to continue...
pause >nul 
goto q2

:q2
cls
title Question 2!
cls
echo Question 2
echo ----------
echo.
echo Solve for x, 4x-3=13?
echo.
echo A) x=4
echo B) x=3
echo C) x=5
echo D) x equals infinity
echo. 
set /p ans2=

if %ans2% == a goto cr2
if %ans2% == b goto wr2
if %ans2% == c goto wr2
if %ans2% == d goto wr2
goto q2

:wr2
cls 
title You LOSE! HA ha! >:D
color 9a
echo Sorry, %player%... But you lost :'(
echo.
echo Press any key to return to the menu...
pause >nul
goto menu

:cr2
cls
title YOU ARE CORRECT! :3
color 9a
echo Congratz! You got this question, correct! Well done, %player%!
echo.
echo Press any key to continue...
pause >nul 
goto win

:win
cls
title Congrats, %player%! You have won!
color 0a
ping localhost -n 1
color 0b
ping localhost -n 1
color 0c
ping localhost -n 1
color 0d
ping localhost -n 1
color 0e
ping localhost -n 1
color 0f
ping localhost -n 1
color 0g
cls
echo.
echo                           Congrats, %player%! You have won!
echo.
echo Here, take this virtual cookie as a gift for completing the......
echo BEST QUIZ MADE BY YOURS TRULY! :D
echo *hands over cookie* :3
echo. 
pause
cls
echo Return to menu? (y/n)
set /p rtrn2menu=

if %rtrn2menu% == y goto menu
if %rtrn2menu% == n exit
goto win

:crash
cls
title ERROR=1 - Code has crashed!
echo WARNING: The code has crashed or is not running properly!
echo.
echo After pressing any key the code should terminate!
pause >nul
exit