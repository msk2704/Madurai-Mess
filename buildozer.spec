[app]
title = Madurai Mess
package.name = madurai_mess
package.domain = org.madurai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

orientation = portrait
fullscreen = 0

# App icon and presplash
icon.filename = assets/madurai_logo.png
presplash.filename = assets/madurai_logo.png

# Keep only necessary modules for now
requirements = python3,kivy

# Limit to one architecture for faster builds
android.archs = arm64-v8a

# Python-for-Android settings (these are stable defaults)
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# Helpful for debugging
log_level = 2

# (Optional) If build issues arise, uncomment:
# p4a.branch = master
