Playful To-Do List (Kivy)
------------------------
Files included:
- main.py       : Kivy app entry
- database.py   : SQLite helper
- todo.kv       : Kivy UI layout
- images/bell.gif
- sounds/add.wav, done.wav, reminder.wav

How to run on desktop:
1. Install Kivy (pip install kivy)
2. From this folder run: python main.py

How to build APK with Buildozer (Linux/WSL):
1. buildozer init
2. edit buildozer.spec -> set requirements = python3,kivy,sqlite3
3. buildozer -v android debug
