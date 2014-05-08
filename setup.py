# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = [
    'Django',
    'Pillow',
    'isounidecode'
]

setup(
    name='django-picturefield',
    version=0.1,
    description=u'Расширение ImageField с поддержкой кирилицы в именах файлов и ограничений на размер изображения',
    long_description = open('README.rst').read(),
    keywords='imagefield, django',
    author='Ivan Morgun',
    author_email='i@proft.me',
    url='https://github.com/proft/django-picturefield',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires
)
