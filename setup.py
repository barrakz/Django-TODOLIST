from setuptools import setup, find_packages

setup(
    name='django-docker-project',
    version='0.0.1',

    packages=find_packages(),
    install_requires=[
        'argon2-cffi==21.3.0',
        'argon2-cffi-bindings==21.2.0',
        'asgiref==3.6.0',
        'attrs==22.2.0',
        'backports.zoneinfo==0.2.1',
        'cffi==1.15.1',
        'cmake==3.25.2',
        'colorama==0.4.6',
        'Django==4.1.5',
        'exceptiongroup==1.1.0',
        'execnet==1.9.0',
        'iniconfig==2.0.0',
        'packaging==23.0',
        'pluggy==1.0.0',
        'psycopg-binary==3.1.8',
        'psycopg2==2.9.5',
        'pycparser==2.21',
        'pytest==7.2.1',
        'pytest-django==4.5.2',
        'pytest-xdist==3.2.0',
        'sqlparse==0.4.3',
        'tomli==2.0.1',
        'tzdata==2022.7'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Framework :: Django',
    ],
)
