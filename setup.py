import setuptools

long_describe = ''
long_describe_format = 'text/markdown'

with open('README.md','r') as readmeFile:
    long_describe = readmeFile.read()

setuptools.setup(
    name='PyRsaToolkit',
    author='MehmetYukselSekeroglu',
    version='0.1.6',
    author_email='dijital_evren@protonmail.com',
    description='Python 3.x RSA String Encrypt & Decrypt Toolkit',
    long_description=long_describe,
    long_description_content_type=long_describe_format,
    keywords='PyPi, RSA, String Encypter, RSA Toolkit',
    project_urls={
        'Bug Reports':'https://github.com/MehmetYukselSekeroglu/PyRsaToolkit/issues',
        'Source Code':'https://github.com/MehmetYukselSekeroglu/PyRsaToolkit'
    },
    url='https://github.com/MehmetYukselSekeroglu/PyRsaToolkit',
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
    install_requires=['rsa'], 
)
