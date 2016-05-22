# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc
%define device tiny210
%define vendor samsung
%define vendor_pretty Samsung
%define device_pretty Tiny210
%define dcd_path ./
# Adjust this for your device
%define pixel_ratio 1.0
# We assume most devices will
%define have_modem 0
%include droid-configs-device/droid-configs.inc
