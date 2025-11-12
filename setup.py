from setuptools import setup, find_packages

with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="cashier-web",
    version="0.1.0",
    author="FrogInOut",
    description="FastAPI cashier web application",
    long_description="A FastAPI web application for processing orders and calculating bills",
    long_description_content_type="text/plain",
    packages=find_packages(),
    py_modules=["app"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "cashier-web=app:app",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["static/*"],
    },
)