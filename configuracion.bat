@echo off

:: echo debes estar atento para poder ingresar tu correo y tu nombre para poder ajustar el actualizador
::winget install Git.Git -e --source winget
::winget install --id=Python.Python.3.12  -e

::pip3 install pandas, matplotlib, numpy

set /p nombre= Escribe tu nombre 
set /p mail= Escribe tu correo electronico 
echo pega el token de github que puedes obtener aquí:
set /p token= https://github.com/settings/tokens 

git config --global user.name "%nombre%"
git config --global user.email "%mail%"