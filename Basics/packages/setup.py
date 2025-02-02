from setuptools import setup, find_packages

setup(
    name='func_one',                   # Package name
    version='0.1.0',                     # Version number
    author='Your Name',                  # Author
    author_email='your.email@example.com', # Email
    description='A short description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),            # Discover all packages
    python_requires='>=3.1',             # Minimum Python version
)
