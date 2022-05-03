from setuptools import setup

setup(
    name="helloworld",
    version="0.0.1",
    py_modules=["helloworld"],
    install_requires=[
        'importlib-metadata; python_version >= "3.7"',
    ],
    entry_points={
        "console_scripts": ["helloworld=helloworld:main"],
    },
)
