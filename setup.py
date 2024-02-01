from setuptools import setup, find_packages

setup(
    name='securetkterminal',
    version='0.2.0',
    author='Scott Peterman',
    author_email='scottpeterman@gmail.com',
    description='''A comprehensive terminal emulation application built with Python, Tkinter and sv-ttk, supporting serial communication and SSH connectivity with advanced features like window resizing, font adjustment, and terminal history management.''',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/scottpeterman/securetkterminal',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'bcrypt>=4.1.2',
        'cffi>=1.16.0',
        'cryptography>=42.0.2',
        'paramiko>=3.4.0',
        'pillow>=10.2.0',
        'pycparser>=2.21',
        'PyNaCl>=1.5.0',
        'pyserial>=3.5',
        'pyte>=0.8.2',
        'sv-ttk>=2.6.0',
        'wcwidth>=0.2.13'
    ],
    entry_points={
        'console_scripts': [
            'stkterm=securetkterminal.main_ssh:run',
            'stktermserial=securetkterminal.main_serial:run',
        ],
    },
    classifiers=[
        # Classifiers help users find your project by categorizing it.
        # For a list of valid classifiers, see https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    # You can specify package data files and directories
    package_data={
        # Include any *.txt or *.rst files found in your package:
        '': ['*.txt', '*.rst'],
    },
)
