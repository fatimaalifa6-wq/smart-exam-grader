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
# تأكد من إضافة أي مكتبات أخرى يستخدمها مشروعك (مثل requests أو pillow إذا لزم الأمر)
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) List of exclusions
source.exclude_exts = spec

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 24

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --public storage (False)
android.private_storage = True

# (list) The Android archs to build for
# حصر البناء على معمارية واحدة (arm64-v8a) يمنع نفاد الذاكرة ويسرع عملية البناء على سيرفرات GitHub
android.archs = arm64-v8a
