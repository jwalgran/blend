import os
import subprocess
from distutils.core import setup, Command
import setuptools

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

class RunTests(Command):
    description = "Run the unit test suite for blend."
    user_options = []
    extra_env = {}
    extra_args = []

    def run(self):
        run_tests_script_path = os.path.join(os.path.dirname(__file__), 'blend', 'run_tests.py')
        subprocess.call([run_tests_script_path])

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

setup(
    name='Blend',
    version='0.0.1',
    author='Justin Walgran',
    author_email='jwalgran@azavea.com',
    packages=['blend', 'blend.test'],
    scripts=['bin/blend'],
    url='http://github.com/azavea/blend',
    license='LICENSE.txt',
    description='A cross-platform tool for merging and processing client-side assets for a web application.',
    long_description=read('README.txt'),
    cmdclass = { 'test': RunTests },
    keywords = "javascript css html build",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Build Tools"
    ]
)