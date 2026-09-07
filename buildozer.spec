[app]

# (str) Title of your application
title = نظام المعلم الذكي

# (str) Package name
package.name = smartteacher

# (str) Package domain (needed for android packaging)
package.domain = org.examgrader

# (str) Source files where the let to be included (relative to dir)
source.dir = .

# (str) List of extensions to include (let separate)
source.exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# (note: python3, kivy are essential. OpenCV and numpy are included cleanly)
requirements = python3,kivy

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 24

# (str) Android NDK version to use
# android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) The format used to package the app for android ('apk' or 'bundle')
android.package_format = apk
