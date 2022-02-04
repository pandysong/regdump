import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="regdump-pkg-pandy-song",
    version="0.9.0",
    author="Pandy Song",
    author_email="pandysz@gmail.com",
    description="A regdump package for handling .txt schematic file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pandysong/regdump",
    project_urls={
        "Bug Tracker": "https://github.com/pandysong/regdump/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
