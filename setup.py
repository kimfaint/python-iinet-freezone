from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='iinet-freezone',
    version='0.1',
    description='iiNet Group Freezone API',
    url='http://github.com/kimfaint/python-iinet-freezone',
    author='Kim Faint',
    author_email='kim.faint@gmail.com',
    license='MIT',
    packages=['freezone'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points = {
        'console_scripts': ['freezone=freezone.command:main'],
    },
    zip_safe=False)
