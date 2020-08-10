import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BoydCut",
    version="0.0.4",
    author="Sorratat Sirirattanajakarin",
    author_email="sorratat.sirirattanajakarin@gmail.com",
    description="Thai Sentence Segmenter",
    url = 'https://github.com/user/reponame',
    long_description=long_description,
    install_requires=["pythainlp[ner]",
                      "pythainlp[artagger]"],
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='==3.6.10'
)