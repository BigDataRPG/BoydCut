import setuptools
import pathlib

HERE = pathlib.Path(__file__).parent
with open(f"{HERE}/README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BoydCut",
    version="1.0.0",
    author="Sorratat Sirirattanajakarin",
    author_email="sorratat.sirirattanajakarin@gmail.com",
    keywords = ['NLP', 'THAI', 'SENTENCE'],
    description="Thai Sentence Segmenter",
    url = 'https://github.com/BigDataRPG/BoydCut',
    download_url="https://github.com/BigDataRPG/BoydCut/archive/v_1.0.0.tar.gz",
    long_description=long_description,
    install_requires=["numpy","pandas","tensorflow","deepcut","pythainlp"],
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=["BoydCut", "BoydCut.model", "BoydCut.utility_data"],
    package_data={'BoydCut': ['model/**/*', 'utility_data/**/*']},
    classifiers=[
        "Natural Language :: Thai",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)