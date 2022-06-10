from setuptools import setup, find_packages

setup(
    name="rce",
    description="reddit comment extractor",
    version="0.0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6, <4",
    install_requires=[
        "click==8.1.3",
        "pmaw==2.1.3",
    ],
    extras_require={
        "dev": [
            "black",
            "jupyterlab",
            "mkdocs-material==8.2.15",
            "mkdocstrings[python]>=0.18",
            "pytest",
            "pylint",
        ]
    },
    entry_points={"console_scripts": ["pcmd=rce.cli.entrypoint:cli"]},
)
