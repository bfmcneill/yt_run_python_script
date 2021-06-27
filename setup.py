from setuptools import setup, find_packages

setup(name='pycmd',
      version='1.0',
      description='python command line app',
      packages=find_packages(
        where = 'src',
        # include = ['pkg*',],
        # exclude = ['additional',]
    ),
      package_dir={'':'src'},
      entry_points={
        'console_scripts': [
            'pycmd = pycmd.cli.entrypoint:cli',
        ],
        },
        install_requires=[
          'requests==2.25.1',
      ],
     )