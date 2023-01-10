#!/usr/bin/env python3
#code by @runbibot -> ShadowyCryptoTrader.Jan 2023.
from setuptools import setup

setup(
    name="tradingviewaccess",
    version="1.1.0",
    packages=[],
    install_requires=['requests', 'apscheduler', 'websocket-client', 'urllib3', 'tzlocal<3.0']
)

