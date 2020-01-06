import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tomotracker-pkg-acodeodyssey",
    version="0.0.1",
    author="Julian Leichert",
    author_email="author@example.com",
    description="Simple Pomodoro Timer, with tracking abilities ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/acodeodyssey/tomotracker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL v3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
