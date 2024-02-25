# Instalar Python 3 usando Winget
winget install --id=Python.Python.3.12 -e

Write-Output "Python3 se ha instalado correctamente, se esperará 10 segundos para asegurar la correcta instalación"

# Esperar un momento para asegurarse de que la instalación se complete
Start-Sleep -Seconds 10

# Instalar las dependencias de Python usando pip
$pythonPath = (Get-Command python).Source
$pipPath = Join-Path (Split-Path $pythonPath) "Scripts\pip.exe"

$packages = @("pandas", "matplotlib", "numpy", "openpyxl", "xlrd", "xlwt")
foreach ($package in $packages) {
    & $pipPath install $package
}
