from setuptools import setup, find_packages

setup(
    name="commonground-protocol",
    version="1.0.0",
    description="CommonGround interface for the Intelligent Internet whitepaper",
    author="Open Source Community",
    author_email="community@example.com",
    packages=find_packages(),
    install_requires=[
        "pygame>=2.5.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Games/Entertainment :: Puzzle Games",
        "Topic :: Education",
    ],
    entry_points={
        "console_scripts": [
            "commonground=main:main",
        ],
    },
)
