# Install Script - Generated by WinLibre Package Creator 1.0.0

# Imports
from wpkg import installer

# Execute remote file for installation
installer.install('nsis','http://winlibrepacman.brinkster.net/downloads/7za.exe',['7-Zip','1.0'])

# We're done. About as simple as an install script can get. Definitely not an
# ideal package because the binaries aren't packaged inside however this may
# be required for some packages.
