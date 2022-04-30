#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ppppocr",
    version="1.0.0",
    author="duolabmeng6",
    author_email="1715109585@qq.com",
    description="PPOCR",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/duolabmeng6/ppppocr",
    packages=find_packages(where='.', exclude=(), include=('*',)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy', 'onnxruntime', 'Pillow', 'opencv-python'],
    python_requires='<3.10',
    package_data={'ppppocr': ['models/*.onnx','rec_dict/*.txt']},
    include_package_data=True,
    install_package_data=True,
    keywords="ppocr paddleOCR ppppocr",

)