import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="network-tools",
    version="0.0.1",
    author="Adam Alston",
    author_email="aalston9@gmail.com",
    description="Ne",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adamalston/network-tools",
    packages=setuptools.find_packages("network-tools"),
    install_requires=[
        "scapy==2.4.2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
