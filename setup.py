from setuptools import setup, find_packages

setup(
    name="ptech_pkg_sample",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=5.1",  # Define a versão mínima do Django necessária
    ],
    description="Um pacote Django reutilizável",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/leandrocristovao/ptech_pkg_sample.git",    
    author="Leandro Cristóvão",
    author_email="leandrocristovao@gmail.com",
    license="MIT",
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
