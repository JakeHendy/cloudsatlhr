import setuptools


with open("README.md") as fp:
    long_description = fp.read()

CDK_VERSION = "1.59.0"


def cdk_module(module: str) -> str:
    return f'aws-cdk.{module}=={CDK_VERSION}'


setuptools.setup(
    name="CloudsAtLHR",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "cloudsatlhr"},
    packages=setuptools.find_packages(where="source"),

    install_requires=[
        cdk_module("core"),
        cdk_module("pipelines"),
        cdk_module("aws-codebuild"),
        cdk_module("aws-codepipeline"),
        cdk_module("aws-codepipeline-actions"),
        cdk_module("aws-cloudwatch"),
        cdk_module("aws-dynamodb"),
        cdk_module("aws-events"),
        cdk_module("aws-lambda"),
        cdk_module("aws-lambda-python")
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
