from setuptools import setup, find_packages

setup(
    name='gpmf',
    version='0.1.2',
    description='Python library to parse GPMF data',
    url='https://github.com/rkleivel/pygpmf',
    author='Roald Kleiveland',
    author_email='roald.kleiveland@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'ffmpeg-python'
    ],
    setup_requires=[
        'numpy'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
