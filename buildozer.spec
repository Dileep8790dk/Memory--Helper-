[app]

# (str) Title of your application
title = ToDoApp (Kivy)

# (str) Package name
package.name = todoapp

# (str) Package domain (needed for Android/iOS packaging)
package.domain = org.test

# (str) Application versioning - FIX: Must be set (e.g., to 0.1)
version = 0.1

# (list) Application requirements - FIX: Must include sqlite3
requirements = python3,kivy,sqlite3

# (str) Source code where the main.py lives - FIX: Points to your subfolder
source.dir = ToDoApp

# (list) Permissions - Safe to include INTERNET
android.permissions = INTERNET
