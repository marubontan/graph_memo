from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="graph_memo",
    install_requires=required,
    entry_points={
        "console_scripts": [
            "graph_memo=graph_memo.cli:main"
        ]
    }
)
