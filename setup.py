import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="node_events",
    version="0.6.8",
    author="Miraculous Owonubi",
    author_email="omiraculous@gmail.com",
    description="A minor rewrite of the NodeJS EventEmitter in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='Apache-2.0',
    url="https://github.com/miraclx/node_events.py",
    packages=['node_events'],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
)
