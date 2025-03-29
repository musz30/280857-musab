from setuptools import setup, find_packages

setup(
    name='strops',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python module for various string manipulation functions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/strops',  # Update with actual URL
    packages=find_packages(),
    py_modules=['strops'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
