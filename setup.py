# coding: utf-8

from setuptools import setup

setup(
    name='pandra',
    version='0.1.1',
    author='Xuzhou Qin',
    author_email='xuzhou.qin@jcdecaux.com',
    url='https://github.com/qxzzxq/pandas-cassandra',
    packages=['pandra'],
    license='MIT',
    description='Use Pandas DataFrame with Cassandra',
    keywords=['pandas', 'cassandra', 'cql'],
    install_requires=[
        'cassandra-driver',
        'pandas'
    ]
)
