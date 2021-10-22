from setuptools import setup, find_packages


setup(
    name='issmoexproxy',
    version='0.0.1',
    description='IIS MOEX proxy',
    url='https://github.com/destr/issmoexproxy',
    author='destr',
    author_email='destrd@gmail.com',
    packages=find_packages(
        include=['issmoexproxy', 'issmoexproxy.*'],
        exclude=['*.tests.*']
    ),
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    license='Public',
    entry_points={
        'console_scripts': [
            'issmoexproxy = issmoexproxy:main'
        ]
    },
    classifiers=[
        'Private :: Do not Upload',  # Prevents uploading to pypi
    ]
)
