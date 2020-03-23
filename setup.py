import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="thedarkness"
    version="0.0.1",
    author="Andrew Scholly",
    author_email="ajscholly@stevenscollege.edu",
    url="https://github.com/yourusername/yourproject",
    description="Send players on a wild adventure",
    long_description=You are the son of the dead leader of the greatest army in the universe, and must go through random rooms generated through reality to find the four parts of the staff of power in order to fix reality and bring back the GAA. Along the way, you will face dangerous enemies, who require you to use the specific weapon you have to win. You start with the sword of power and must escape when facing enemies requiring tactics and skill to stop,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
