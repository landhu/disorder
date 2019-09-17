import sys
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass
from setuptools import setup

setup(
    name='testorder',
    version='0.1',
    author='huzq',
    author_email = 'landhu@hotmail.com',
    description = 'randrom order',
    license = 'Wangsu.com',
    py_modules = ['disorder'],
    entry_points = {
        'nose.plugins': [
            'disorder = disorder:Randomize'
            ]
        }

    )
