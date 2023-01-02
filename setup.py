import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="netctrl",
    version="0.1.0",
    author="Tom Sverre Pedersen",
    author_email="tsp@dag.yt",
    description="A tool for managing network devices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/obosopennet/netctrl",
    packages=setuptools.find_packages(),
    install_requires=[
        "pynetbox",
        "netmiko",
        "jinja2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
