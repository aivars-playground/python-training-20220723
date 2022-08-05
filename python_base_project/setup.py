from setuptools import setup, find_packages

with open("README.md", encoding="UTF-8") as f:
    readme = f.read()

setup(
    name="python_base",
    version="0.1.0",
    description="Python Base Project",
    long_description=readme,
    author="Me",
    author_email="Me@example.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["click"],
    python_requires=">=3.10",
    entry_points={"console_scripts": ["python_base=python_base.__main__:main"]},
)
