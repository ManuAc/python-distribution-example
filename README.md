# Example Package

This is a simple example package.

Steps to generate binary:

python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel



Notes:

Extra arguments:

install_requires=[
   'A>=1',
   'B>=2'
]

https://stackoverflow.com/questions/8620789/proper-way-to-distribute-run-scripts-with-python-package?rq=1
