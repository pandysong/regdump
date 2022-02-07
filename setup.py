import setuptools
import shutil
from setuptools.command.install_scripts import install_scripts

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


class InstallScripts(install_scripts):

    def run(self):
        install_scripts.run(self)

        # Rename some script files
        for script in self.get_outputs():
            if script.endswith(".py") or script.endswith(".sh"):
                dest = script[:-3]
            else:
                continue
            print("moving %s to %s" % (script, dest))
            shutil.move(script, dest)


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
    cmdclass={
        "install_scripts": InstallScripts
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    scripts=['src/regdump.py'],
)
