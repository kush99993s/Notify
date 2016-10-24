import os
from setuptools import setup, find_packages

setup(
  name='Notify',
  version='0.0.0.1',
  description='Notification system that will get notification if one type of notification failed',
  long_description=('NAN'),
  license='MIT',
  author='kush',
  author_email='kush99993s@gmail.com',
  packages=find_packages(exclude=['tests*']),
  include_package_data=False
)