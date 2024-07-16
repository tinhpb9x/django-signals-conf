import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='django-signals-conf',
    version='0.1',
    packages=['django_signals_conf'],
    description='The library helps configure signals for django projects faster and easier',
    long_description=README,
    author='Tinh Pham Ba',
    author_email='tinhpb9x@gmail.com',
    url='https://github.com/tinhpb9x/django-signals-conf/',
    license='MIT',
    python_requires='>3.0',
    install_requires=[
        'Django',
    ]
)
