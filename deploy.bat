@echo off

echo === Завантаження Python-залежностей ===
python -m pip install --upgrade pip
pip install -r client/requirements.txt

echo === Компіляція коду Arduino ===
mkdir deploy
arduino-cli compile --fqbn arduino:avr:uno server/server.ino
copy server\server.ino.arduino.avr.uno.hex deploy\

echo === Деплой бінарних файлів ===
copy client\client.py deploy\
echo Бінарні файли задеплоєні в папку deploy.

echo === Завантаження коду на Arduino ===
arduino-cli upload -p COM3 --fqbn arduino:avr:uno server/server.ino

echo === Запуск тестів ===
python client/client.py

pause
