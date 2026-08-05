@echo off
rem =====================================================================
rem  Verificador de links do SDDP release notes
rem
rem  Clique duas vezes para abrir o menu, ou use pela linha de comando:
rem     check-links.bat            -> menu
rem     check-links.bat --fix      -> comenta quebrados / descomenta os que voltaram
rem     check-links.bat --offline  -> so links internos, sem rede
rem
rem  Os ~1400 links de download do psr-inc.com so podem ser verificados
rem  logado. Use a opcao [3] do menu (ou login-psr.bat) uma vez: o Chrome
rem  abre, voce faz login, e o cookie fica salvo em .psr-cookie.
rem  NAO cole o cookie aqui dentro -- ele tem "%" e o cmd corrompe o valor.
rem =====================================================================

setlocal EnableExtensions
cd /d "%~dp0"
chcp 65001 >nul 2>nul
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"

rem --- opcoes -----------------------------------------------------------
set "JOBS=6"
set "TIMEOUT=25"
set "REPORT=link-report.md"

rem --- acha o Python ----------------------------------------------------
set "PY="
where python >nul 2>nul && set "PY=python"
if not defined PY (
    where py >nul 2>nul && set "PY=py -3"
)
if not defined PY (
    echo.
    echo ERRO: Python nao encontrado no PATH.
    echo Instale em https://www.python.org/downloads/ ^(marque "Add python.exe to PATH"^).
    goto :fim
)

if not exist "tools\check_links.py" (
    echo.
    echo ERRO: nao achei tools\check_links.py -- rode este .bat de dentro do repositorio.
    goto :fim
)

rem --- argumentos da linha de comando pulam o menu -----------------------
if not "%~1"=="" (
    set "FLAGS=%*"
    goto :rodar
)

rem --- menu -------------------------------------------------------------
:menu
echo.
echo ==========================================================
echo   Verificador de links - SDDP release notes
echo ==========================================================
if exist ".psr-cookie" (echo   cookie psr-inc.com: salvo) else (echo   cookie psr-inc.com: AUSENTE - downloads nao serao checados)
echo.
echo   [1] Verificar e gerar relatorio  ^(nao altera nada^)
echo   [2] Verificar e APLICAR          ^(comenta quebrados, descomenta os que voltaram^)
echo   [3] Login no psr-inc.com         ^(abre o Chrome e salva o cookie^)
echo   [4] Somente links internos       ^(sem rede, rapido^)
echo   [5] Testar o cookie salvo
echo   [0] Sair
echo.
set "OP="
set /p "OP=Opcao: "

if "%OP%"=="1" ( set "FLAGS=" & goto :rodar )
if "%OP%"=="2" ( set "FLAGS=--fix" & goto :rodar )
if "%OP%"=="3" goto :login
if "%OP%"=="4" ( set "FLAGS=--offline" & goto :rodar )
if "%OP%"=="5" goto :testcookie
if "%OP%"=="0" ( endlocal & exit /b 0 )
echo Opcao invalida.
goto :menu

rem --- login ------------------------------------------------------------
:login
echo.
%PY% tools\psr_login.py
if errorlevel 2 (
    echo.
    echo Falhou. Instale o Selenium com:  python -m pip install selenium
    echo Alternativa manual: crie um arquivo .psr-cookie no raiz com o valor
    echo do header Cookie: copiado do DevTools ^(F12 ^> Network^).
)
goto :fim

rem --- teste do cookie --------------------------------------------------
:testcookie
echo.
%PY% tools\psr_login.py --check
goto :fim

rem --- execucao ---------------------------------------------------------
:rodar
echo.
if not exist ".psr-cookie" if not defined PSR_COOKIE (
    echo AVISO: sem cookie, os ~1400 links de download saem como AUTH ^(nao verificados^).
    echo        Rode a opcao [3] do menu para verifica-los tambem.
    echo.
)
%PY% tools\check_links.py --jobs %JOBS% --timeout %TIMEOUT% --report "%REPORT%" %FLAGS%
set "CODE=%ERRORLEVEL%"

echo.
if "%CODE%"=="0" echo Nenhum link quebrado.
if "%CODE%"=="1" (
    echo Links quebrados encontrados - veja a secao BROKEN LINKS acima.
    echo Rode a opcao [2] do menu para comenta-los.
)
if "%CODE%" GEQ "2" echo O verificador terminou com erro ^(exit %CODE%^).
if exist "%REPORT%" echo Relatorio: %~dp0%REPORT%

:fim
echo.
pause
endlocal & exit /b 0
