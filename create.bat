@ECHO OFF
:: GET ARGUMENT in ARG1
set arg1=%1
set originalPath=%cd%

:: CREATE DIRECTORY USING SAME ARGUMENT
mkdir "C:/%arg1%"

:: IF ERROR GO TO EXCEPTION HANDLING BLOCK stopexec
if errorlevel 1 goto stopexec

:: ELSE CREATE FOLDER IN C Drive
cd "C:/%arg1%"

:: CREATE A NEW README.md FILE
echo "**Readme goes here**" >> README.md

:: GIT LOCAL COMMANDS
git init
git add .
git commit -m "initial commit"

:: Go back to original directory to execute github repo creation steps.
cd "C:\AutoCreateProject"

:: Run python script
python github_create_repo.py %arg1%

:: Go back to Project Folder %arg1% to push the changes
cd "C:/%arg1%"

:: Push to Github
git remote add origin https://github.com/aks16588/%arg1%.git
git push -u origin master

@Echo on
echo "New Project %arg1% created successfully."
pause
exit


:: Error handling if folder already exist
:stopexec
Echo Unable to create folder "%arg1%"
pause
exit
