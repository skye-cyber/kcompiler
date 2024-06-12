from setuptools import find_namespace_packages, setup

setup(
    name='Kcompiler',
    version='1.0.0',
    author="Wambua aka Bullet Angel",
    packages=find_namespace_packages(include=['*']),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    entry_points={
        'console_scripts': [
            "krun=compiler:main",
            "kcompiler=compiler:main",
            "compile=compiler:main",
            "kotlin_compiler=compiler:main",
            "compile_kotlin=compiler:main"
        ],
    },

    python_requires='>=3',
    install_requires=[],

    include_package_data=True,
    package_data={},

    license="MIT",
    keywords=['kotlin_compiler', "compile_kotlin", "compile", "run_kotlin"],

    classifiers=[
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
