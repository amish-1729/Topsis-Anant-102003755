# Create complete setup.py file for Topsis-Anant-102003755 package

from setuptools import setup

setup(
    name='Topsis-Anant-102003755',
    version='1.0.0',
    description='Topsis-Anant-102003755 package',
    url='',
    author='Anant Mishra',
    author_email='amishra1577@gmail.com',
    license='MIT',
    packages=['Topsis-Anant-102003755'],
    zip_safe=False,
    install_requires = ['pandas','numpy','openpyxl','tabulate'],
    
    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],

)


