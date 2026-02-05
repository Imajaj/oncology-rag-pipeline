from setuptools import setup, find_packages

setup(
    name="oncology-rag-pipeline",
    version="1.0.0",
    author="Ajaj Ahmed",
    #author_email="ajaj1417@gmail.com",
    description="RAG pipeline for oncology EHR extraction and clinical trial matching",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Imajaj/oncology-rag-pipeline",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Healthcare Industry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8",
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.30.0",
        "sentence-transformers>=2.2.2",
        "faiss-cpu>=1.7.4",
        "rank-bm25>=0.2.2",
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "pyyaml>=6.0",
    ],
)
