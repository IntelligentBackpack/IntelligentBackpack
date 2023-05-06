from setuptools import setup, find_packages

class GradleDistribution(Distribution, object):
    def __init__(self, attrs):
        attrs['name'] = os.getenv('PYGRADLE_PROJECT_NAME')
        attrs['version'] = os.getenv('PYGRADLE_PROJECT_VERSION')

setup(
    distclass=GradleDistribution,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
)