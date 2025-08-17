[app]

# Application information
title = Madurai Mess
package.name = madurai_mess
package.domain = org.madurai
version = 0.1.0  # Using semantic versioning

# Source configuration
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt,ttf

# Additional directories to include
source.include_dirs = assets,data

# Orientation and display
orientation = portrait
fullscreen = 0
resizable = 1  # Allow window resizing on desktop

# Graphics settings
requirements = python3,kivy==2.1.0,pillow,requests
android.archs = arm64-v8a

# Android SDK configuration
android.sdk = 30
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.build_tools_version = 32.0.0

# App assets
icon.filename = %(source.dir)s/assets/icon.png
presplash.filename = %(source.dir)s/assets/presplash.png
presplash.color = #FFFFFF  # Neutral white background

# Permissions (add if needed)
# android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

# Build optimization
android.no_main_fragment = 1  # Optional: Disable main fragment for some optimizations

# Debugging
log_level = 1  # info level logging
log_filter = *:I

# Uncomment if you encounter build issues:
# p4a.branch = master
# p4a.local_recipes = ./p4a-recipes
# android.accept_sdk_license = True

# Packaging options
# android.aab = 1  # Uncomment to build Android App Bundle
