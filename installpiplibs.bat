@echo off
echo Were Now Installing Extra Libraries For SpecSend. If the stuff that comes up on screen seems confusing,
echo Don't Worry! Its just us the little helpers installing SpecSend for you.
echo Please Press any key to go on.
pause
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install boxsdk
pip install "boxsdk[jwt]"