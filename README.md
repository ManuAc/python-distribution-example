# Python distribution example

<b> Steps to generate the wheel file: <b>

Install setuptools and wheel packages and execute the next command from the project folder:

```
python3 -m pip install --user --upgrade setuptools wheel <br/>
python3 setup.py sdist bdist_wheel <br/>
```

Steps to install the wheel file: <br/>
```
pip install path/to/wheel/file <br/>
```

Calling the entry point: <br/>

```
REGISTERED_ENTRY_POINT_NAME Aargs <br/>
Example: pjp-mip "FOO" 5
```

Notes: <br/>

Extra arguments in setup.py: <br/>

```
install_requires=[
   'A>=1',
   'B>=2',
]
```
