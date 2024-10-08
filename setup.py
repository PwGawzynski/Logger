from setuptools import setup, find_packages


setup(
    name="logger",
    version="0.0.18",
    packages=find_packages(),
    install_requires=[
        "colorama==0.4.6",
    ],
    author="Paweł Gawżynski && Jakub Wrona",
    author_email="pgawynski@icloud.com",
    description="Simple Logger module to log into files",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/PwGawzynski/Logger",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)
