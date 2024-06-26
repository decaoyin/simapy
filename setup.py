# Always prefer setuptools over distutils
from pathlib import Path
import shutil
from setuptools import setup, find_packages

here = Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")


# Remove build and dist folders
shutil.rmtree(Path("build"), ignore_errors=True)
shutil.rmtree(Path("dist"), ignore_errors=True)

with open('requirements.txt',encoding='utf8') as f:
    required = f.read().splitlines()

setup(
    name="simapy",
    version="4.6.1.dev2",
    author="SINTEF Ocean",
    description="Python utilities for SIMA",
    url="https://github.com/SINTEF/simapy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=["tests"]),
   install_requires=required,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
