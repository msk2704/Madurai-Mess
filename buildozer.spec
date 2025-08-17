[app]
# (str) Title of your application
title = Madurai Mess

# (str) Package name
package.name = madurai_mess

# (str) Package domain (reverse domain notation)
package.domain = org.madurai

# (str) Source code directory
source.dir = .

# (list) File extensions to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.69

# (str) Application orientation (portrait/landscape)
orientation = portrait

# (int) Fullscreen mode (0 = windowed, 1 = fullscreen)
fullscreen = 0

# App icon and presplash
icon.filename = assets/madurai_logo.png
presplash.filename = assets/madurai_logo.png

# (list) Python requirements
requirements = python3,kivy

# Limit to one architecture for faster builds
android.archs = arm64-v8a

# (str) Android SDK version to use
android.sdk = 30  # or the version you are targeting

# Android API settings
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.build_tools_version = 30.0.3 

# Logging level (0=debug, 1=info, 2=warning, 3=error)
log_level = 2

# (Optional) Uncomment if build issues arise
# p4a.branch = master
