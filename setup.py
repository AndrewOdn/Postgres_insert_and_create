from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

requirements = ["psycopg2>=2.9.3"]

setup(
    name="PyPostgresIn",
    version="0.0.1",
    author="Odnodvortsev Andrew",
    author_email="fastpeaple@gmail.com",
    description="A package to easy insert/create table in Postgres",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/AndrewOdn/PyPostgresIn",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    python_requires=">=3.6",
)