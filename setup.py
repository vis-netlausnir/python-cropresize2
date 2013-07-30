from setuptools import setup, find_packages
from pkg_resources import require, DistributionNotFound
import os

def is_installed(package_name):
    try:
        require(package_name)
    except DistributionNotFound:
        return False
    else:
        return True

try:
    filename = os.path.join(os.path.dirname(__file__), 'README')
    description = file(filename).read()
except:
    description = ''

# We want to allow either PIL or Pillow as a dependency.  Because we can't
# write an `install_requires` declaration that installs either, we make
# Pillow a dependency at run time if both are missing.
install_requires = ['Pillow'] 
if is_installed('PIL') or is_installed('Pillow'):
    install_requires = []

version = '0.1.7a'

setup(name='cropresize2',
      version=version,
      description="crop and resize an image without doing the math yourself",
      long_description=description,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='image',
      author='Jeff Hammel, Vlad Frolov',
      author_email='k0scist@gmail.com, frolvlad@gmail.com',
      url='http://pypi.python.org/pypi/cropresize2',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      crop-resize = cropresize2:main
      """,
      )
