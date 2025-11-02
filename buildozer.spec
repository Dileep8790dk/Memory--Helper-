[app]

# (str) Title of your application
title = ToDoApp (Kivy)

# (str) Package name
package.name = todoapp

# (str) Package domain (needed for Android/iOS packaging)
package.domain = org.test

# (str) Application versioning - Set this to any version
version = 0.1

# (list) Application requirements - Must include sqlite3
requirements = python3,kivy,sqlite3

# (str) Source code where the main.py lives - Must point to your subfolder
source.dir = ToDoApp

# (list) Permissions - Required for Android
android.permissions = INTERNET
