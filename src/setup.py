'''
Created on 30-Sep-2016

@author: Asawari.Vaidya
'''
from setuptools import setup


setup(
    name='Paysafe',
    version=1.0,

    author='Opus Consulting Solutions Pvt. Ltd.',
    author_email='deepak.agarwal@opusconsulting.com',
    description=('This document provides the release details of the Python SDK for Paysafe API' ),
    license='Opus Consulting Solutions Pvt. Ltd.',
    packages=["utils","bin","PythonPaysafeSDK","PythonPaysafeSDK/CardPayments","PythonPaysafeSDK/CustomerVault","PythonPaysafeSDK/common", "PythonPaysafeSDK/DirectDebit", "PythonPaysafeSDK/ThreeDSecure"],
    include_package_data=True,
    zip_safe=False,
    py_modules = ['PythonPaysafeSDK','HTMLTestRunner','bin','utils'],     
)
