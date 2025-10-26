[app]

# (str) Title of your application
title = ToDoApp (Kivy)

# (str) Package name
package.name = todoapp

# (str) Package domain (needed for Android/iOS packaging)
package.domain = org.test

# (list) Application requirements
# Add 'sqlite3' here because your app uses it via 'database.py'.
requirements = python3,kivy,sqlite3

# (list) Permissions
# Note: Kivy often requires INTERNET permission even if you don't explicitly use
# networking, so it's a safe addition.
android.permissions = INTERNET
