from setuptools import find_packages, setup

install_requires = [
    'requests>=2.10',
]

tests_require = [
    'pytest>=2.8.3',
    'responses>=0.5.1',
]

setup(
    name='pycoinbin',
    version='0.1',
    description='Python wrapper for Coinbin.org',
    long_description='',
    author="Adylzhan Khashtamov",
    author_email="adil.khashtamov@gmail.com",
    url='https://github.com/adilkhash/pycoinbin',

    install_requires=install_requires,
    tests_require=tests_require,
    dependency_links=[],
    extras_require={'test': tests_require},
    packages=find_packages(),
    include_package_data=True,

    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.x',
        'Programming Language :: Python :: 3.x',
    ],
    zip_safe=False,
)
