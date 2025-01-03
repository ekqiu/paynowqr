from setuptools import setup, find_packages

setup(
    name='PayNowQR',
    version='0.2',
    packages=find_packages(),
    install_requires=["qrcode[pil]"],
    description='A simple python library to generate PayNow QR codes in Singapore',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Evan Khee",
    author_email="evankhee@ymail.com",
    url="https://github.com/ekqiu/paynowqr",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)