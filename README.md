# Example Package

Steps to generate the wheel file:

python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel

Steps to install the wheel file:

pip install path/to/wheel/file

Calling the entry point:

REGISTERED_ENTRY_POINT_NAME Aargs
Example: pjp-mip "FOO" 5


Notes:

Extra arguments:

install_requires=[
   'A>=1',
   'B>=2'
]
