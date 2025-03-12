# setup.py
from setuptools import setup, find_packages

setup(
    name="my-python-app",  # Package name
    version="0.1",
    packages=find_packages(),  # Automatically find all sub-packages
    install_requires=[
        # List additional dependencies here if needed
    ],
    entry_points={
        "console_scripts": [
            "my-python-app = my-python-app.main:main",  # CLI entry point (if applicable)
        ]
    },
    # Other metadata for your package
    author="Your Name",
    author_email="your-email@example.com",
    description="A simple math operations package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/my-python-app",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)

