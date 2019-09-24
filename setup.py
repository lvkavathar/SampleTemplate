from setuptools import setup, find_packages
setup(
    name="PDXLibrary",
    version="0.1",
    packages=['prediction'],
    scripts=[],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['docutils>=0.3','requests==2.21.0'],

    package_data={
        # If any package contains *.json or *.txt files, include them:
        '': ['*.json','*.txt'],
    },

    # metadata to display on PyPI
    author="Predictronics Team",
    author_email="customerservice@predictronics.com",
    description="Analytical Package from Predictronics",
    keywords="Machine Learning Anomaly Detection Prediction",
    url="https://www.predictronics.com",   # project home page, if any
    project_urls={
        "Bug Tracker": "https://github.com/pdxGithub/nodeServer/issues",
        "Documentation": "https://github.com/pdxGithub/nodeServer/issues",
        "Source Code": "https://github.com/pdxGithub/nodeServer",
    },
    classifiers=[
        'License :: Predictronics License'
    ]

    # could also include long_description, download_url, etc.
)