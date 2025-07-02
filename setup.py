from setuptools import setup, find_packages

setup(
    name="forex_structuring_detection",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn"
    ],
    author="Your Name",
    description="Forex Structuring Detection System",
    python_requires=">=3.7",
)