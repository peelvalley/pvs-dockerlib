import setuptools
from pvs_dockerlib.__version__ import __version__
with open('README.md', 'r') as fh:
    long_description = fh.read()
setuptools.setup(
    name='pvs-dockerlib',
    version=__version__,
    author='Peel Valley Softwware',
    author_email='info@peelvalley.com.au',
    description='Custom docker client wrapper',
    keywords='docker',
    url='https://github.com/peelvalley/pvs_dockerlib',
    project_urls={
        'Bug Tracker': 'https://github.com/peelvalley/pvs_dockerlib/issues',
        'Source Code': 'https://github.com/peelvalley/pvs_dockerlib',
    },
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    install_requires=[
   'docker >= 3.7.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
