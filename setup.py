from setuptools import setup,find_packages

setup(
  name="PythonDoxygenExample",
  version='0.0',
  pacakges=find_packages(where='./src'),
  requires=[
    'numpy',
    'sphinx',
  ],
)
