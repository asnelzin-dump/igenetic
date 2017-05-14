from setuptools import setup, find_packages

import igenetic

setup(
    name='igenetic',
    version=igenetic.__version__,
    download_url='https://github.com/asnelzin/igenetic',
    author=igenetic.__author__,
    author_email='asnelzin@gmail.com',
    packages=find_packages()
)