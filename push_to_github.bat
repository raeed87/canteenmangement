@echo off
echo Initializing Git repository...
git init

echo Adding all files...
git add .

echo Committing files...
git commit -m "Initial commit: Canteen Management System with modern UI"

echo Setting main branch...
git branch -M main

echo Adding remote repository...
git remote add origin https://github.com/raeed87/canteenmangement.git

echo Pushing to GitHub...
git push -u origin main

echo.
echo ✅ Successfully pushed to GitHub!
echo Repository: https://github.com/raeed87/canteenmangement.git
echo.
pause