from setuptools import setup, find_packages

setup(
    version='1.0',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
)