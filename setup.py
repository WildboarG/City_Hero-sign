#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import setuptools

setuptools.setup(
    name='cityhero',
    version='0.0.6',
    author='WildboarG',
    author_email='mm62633482@gmail.com',
    url='https://github.com/WildboarG/City_Hero-sign',
    license="MIT",
    description='Based on the script of the Erqi City Hero Infinite City sign in and collect coins',
    long_description_content_type="text/markdown",
    long_description = "test Module",
    packages=["cityhero"],
    install_requires=["requests","rich"],
    keywords=["sign", "City_Hero"],
    python_requires=">=3.6"
    )
