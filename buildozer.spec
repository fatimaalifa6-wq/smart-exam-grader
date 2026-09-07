[app]

# (str) Title of your application
title = Teacher Assistant

# (str) Package name
package.name = smartteacher

# (str) Package domain (needed for android packaging)
package.domain = org.teacher

# (str) Source directory where the main.py file lives
source.dir = .

# (list) Source files to include (let it blank to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (version or version.regex)
version = 1.0

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 24

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --public storage (False)
android.private_storage = True
