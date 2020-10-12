import setuptools
# root directory에서 pip install .

with open("README.md", "r" ,encoding="UTF-8") as fh :
    long_description = fh.read()

setuptools.setup(
    name='sba_api_exam',
    version='1.0',
    description='Python Distribution Utilities',
    long_description=long_description,
    author='bokyung kim',
    author_email='bo.kim0226@gmail.com',
    url='https://www.python.org/sigs/distutils-sig/',
    packages=setuptools.find_packages(),
    python_requires='>=3.7'
)
