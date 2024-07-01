from setuptools import setup, find_packages

setup(
    name='student-attendance-tracker',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'tkinter',
        'Pillow',
        'requests',
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'start-student-attendance = main:main',  # Replace with your main entry point
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
