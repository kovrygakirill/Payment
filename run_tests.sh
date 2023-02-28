# Colors
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

BASE_DIR=backend
SETTINGS=--settings=config.settings.test

echo "${green}>>> Create test DB for project... ${reset}"
sleep 1
cd $BASE_DIR

python manage.py migrate $SETTINGS
echo "${green}>>> Migration was made${reset}"
sleep 1

echo "${green}>>> Start all tests ... ${reset}"
sleep 1
python manage.py test tests/* $SETTINGS
cd ..