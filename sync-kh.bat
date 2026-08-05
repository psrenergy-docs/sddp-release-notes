@echo off
rem =====================================================================
rem  Cascateia o changelog (fonte) para a copia do knowledge_hub
rem
rem  Clique duas vezes para abrir o menu, ou use pela linha de comando:
rem     sync-kh.bat                      -> menu
rem     sync-kh.bat --apply              -> insere o que falta
rem     sync-kh.bat --apply --promote    -> tambem publica versoes ja finais
rem     sync-kh.bat --target OUTRO\CAMINHO
rem
rem  A copia do knowledge_hub e uma reescrita feita a mao, nao um render
rem  deste repositorio, entao a sincronizacao nunca sobrescreve entrada
rem  existente: ela so acrescenta o que falta e relata o resto.
rem =====================================================================

setlocal EnableExtensions
cd /d "%~dp0"
chcp 65001 >nul 2>nul
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"

set "KH=..\knowledge_hub"

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

if not exist "tools\sync_knowledge_hub.py" (
    echo.
    echo ERRO: nao achei tools\sync_knowledge_hub.py -- rode este .bat de dentro do repositorio.
    goto :fim
)
if not exist "%KH%\docs\changelog\sddp" (
    echo.
    echo ERRO: nao achei a copia em %KH%\docs\changelog\sddp
    echo Use  sync-kh.bat --target CAMINHO  se ela estiver em outro lugar.
    goto :fim
)

rem --- argumentos da linha de comando pulam o menu -----------------------
if not "%~1"=="" (
    set "FLAGS=%*"
    goto :rodar
)

rem --- menu -------------------------------------------------------------
set "TENTATIVAS=0"
:menu
echo.
echo ==========================================================
echo   Sincronizar changelog  --^>  knowledge_hub
echo ==========================================================
echo   fonte: %CD%\docs
echo   copia: %KH%\docs\changelog\sddp
echo.
echo   [1] Relatorio            ^(o que esta fora de sincronia, nao altera nada^)
echo   [2] Gerar trechos        ^(blocos prontos num arquivo, para conferir antes^)
echo   [3] Aplicar              ^(insere versoes e RCs que faltam^)
echo   [4] Aplicar + publicar   ^(idem, e troca "Upcoming release" pelo release real^)
echo   [5] Aplicar + publicar + criar arquivos novos
echo   [0] Sair
echo.
echo   3, 4 e 5 escrevem no repositorio do knowledge_hub.
echo.
set "OP="
set /p "OP=Opcao [1]: "

rem Enter, ou stdin fechado, cai no relatorio -- a opcao que nao escreve nada.
if not defined OP ( set "FLAGS=" & goto :rodar )

if "%OP%"=="1" ( set "FLAGS=" & goto :rodar )
if "%OP%"=="2" ( set "FLAGS=--snippets kh-sync-snippets.md" & goto :rodar )
if "%OP%"=="3" ( set "FLAGS=--apply" & goto :rodar )
if "%OP%"=="4" ( set "FLAGS=--apply --promote" & goto :rodar )
if "%OP%"=="5" ( set "FLAGS=--apply --promote --create-files" & goto :rodar )
if "%OP%"=="0" ( endlocal & exit /b 0 )

echo Opcao invalida.
set /a TENTATIVAS+=1
if %TENTATIVAS% GEQ 3 (
    echo Desisto depois de tres tentativas.
    goto :fim
)
goto :menu

rem --- execucao ---------------------------------------------------------
:rodar
echo.
%PY% tools\sync_knowledge_hub.py %FLAGS%
set "CODE=%ERRORLEVEL%"

echo.
if "%CODE%"=="0" echo As duas copias estao alinhadas.
if "%CODE%"=="1" echo Ainda ha diferencas -- veja as secoes acima.
if "%CODE%" GEQ "2" echo A sincronizacao terminou com erro ^(exit %CODE%^).

if exist "kh-sync-snippets.md" echo Trechos gerados: %~dp0kh-sync-snippets.md

rem --- o que mudou na copia, para voce revisar e commitar ---------------
echo %FLAGS% | findstr /C:"--apply" >nul
if not errorlevel 1 (
    where git >nul 2>nul
    if not errorlevel 1 (
        echo.
        echo -------- mudancas no knowledge_hub --------
        git -C "%KH%" status --short
        git -C "%KH%" --no-pager diff --stat
        echo.
        echo Revise e commite dentro de %KH%.
    )
)

:fim
echo.
pause
endlocal & exit /b 0
