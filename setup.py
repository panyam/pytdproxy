import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytdproxy",
    version="0.0.1",
    author="Sri Panyam",
    author_email="sripanyam@gmail.com",
    description="Python GRPC Bindings for tdproxy - A local proxy for TD Ameritrade API (including streaming API)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/panyam/pytdproxy",
    project_urls={
        "Bug Tracker": "https://github.com/panyam/pytdproxy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
