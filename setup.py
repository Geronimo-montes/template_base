from setuptools import find_packages, setup

PROJECT_NAME ="Project"
setup(
    name=f"{PROJECT_NAME}",
    version="1.0.0",
    description="Project Template",
    author="...",
    license="MIT",
    install_requires=[],

    packages=find_packages("src"),
    package_dir={"":"bin"},

    package_data={
        f"{PROJECT_NAME}": ["data/*.*"]
    },
)
