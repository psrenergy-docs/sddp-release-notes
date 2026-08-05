@echo off
rem =====================================================================
rem  Abre o Chrome, espera voce fazer login no psr-inc.com e salva o
rem  cookie de sessao em .psr-cookie (ignorado pelo git).
rem
rem  Depois disso o check-links.bat passa a verificar tambem os ~1400
rem  links de download.
rem
rem     login-psr.bat            -> abre o Chrome e espera o login
rem     login-psr.bat --check    -> so testa o cookie ja salvo
rem     login-psr.bat --reset    -> esquece o perfil e o cookie salvos
rem =====================================================================

setlocal EnableExtensions
cd /d "%~dp0"
chcp 65001 >nul 2>nul
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"

set "PY="
where python >nul 2>nul && set "PY=python"
if not defined PY (
    where py >nul 2>nul && set "PY=py -3"
)
if not defined PY (
    echo.
    echo ERRO: Python nao encontrado no PATH.
    goto :fim
)

%PY% tools\psr_login.py %*
if errorlevel 2 (
    echo.
    echo Instale o Selenium com:  python -m pip install selenium
)

:fim
echo.
pause
endlocal & exit /b 0
