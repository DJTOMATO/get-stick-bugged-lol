import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='get-stick-bugged-lol',
    version='1.0.2',
    author='n0spaces',
    description="'Get stick bugged' video generator v2",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='git+https://github.com/DJTOMATO/get-stick-bugged-lol',
    packages=setuptools.find_packages(),
    package_data={'gsbl': ['media/*.*']},
    entry_points={'console_scripts': ['gsbl=gsbl.__main__:main']},
    install_requires=['pylsd-nova==1.2.1', 'numpy==1.24.3', 'Pillow<=9.5.0', 'moviepy==1.0.3'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
