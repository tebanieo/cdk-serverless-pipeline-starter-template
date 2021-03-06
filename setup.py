import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="serverless_pipeline",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "serverless_pipeline"},
    packages=setuptools.find_packages(where="serverless_pipeline"),

    install_requires=[
        "aws-cdk.core",
        "aws-cdk.aws_s3",
        "aws-cdk.aws_ssm",
        "aws-cdk.aws_codebuild",
        "aws-cdk.aws_codepipeline",
        "aws-cdk.aws_codepipeline_actions",
        "aws-cdk.aws_cloudformation",
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
