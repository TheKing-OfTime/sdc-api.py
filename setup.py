import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sdc_api_py",
    version="1.3.0",
    author="TheKingOfTime",
    author_email="artem.matvienko0@gmai.com",
    description="An async wrapper for Server-Discord.Com API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheKing-OfTime/sdc-api.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">= 3.7",
)