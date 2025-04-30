from setuptools import setup, find_packages

setup(
    name="time_series_analysis",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.20.0",
        "pandas>=1.3.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "statsmodels>=0.13.0",
        "scikit-learn>=1.0.0",
        "scipy>=1.7.0",
        "pywavelets>=1.2.0",  # This is the correct package name
    ],
)
