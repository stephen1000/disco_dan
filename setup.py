import setuptools

with open("readme.md", "r") as f:
    long_description = f.read()

dev_req = [
    "black>=19.10b0",
    "pylint>=2.5.3",
]

test_req = [
    "pytest>=5.4.3",
]

setuptools.setup(
    name="disco_dan",
    version="0.0.2",
    author="Stephen Lowery",
    author_email="author@example.com",
    description="Code used for a discord bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
    entry_points={"console_scripts": ["disco_dan = disco_dan.bot:start_loop"]},
    install_requires=[
        "python-dotenv==0.13.0",
        "discord.py==1.5.0",
        "google-api-python-client==1.9.3",
        "pytube3==9.6.4",
        "PyNaCl==1.4.0",
    ],
    extras_require={"dev": test_req + dev_req, "test": test_req,},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
