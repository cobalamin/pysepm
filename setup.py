from setuptools import setup,find_packages

setup(
    name='pysepm',
    version='0.1',
    description='Computes Objective Quality measures',
    author='Philipp Schmid',
    author_email='scdp@zhaw.ch',
    url='https://github.zhaw.ch/scdp/pysepm',
    license='MIT',
    install_requires=[
	    'numpy',
	    'scipy',
	    'numba',
	    'pystoi',
	    'pesq==0.0.4',
	    'SRMRpy @ https://github.com/jfsantos/SRMRpy/archive/fee009779cef96bed34db3a7e31d10f3ad1ea133.zip#egg=SRMRpy',
	],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages()
)
