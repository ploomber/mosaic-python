import setuptools

setuptools.setup(
    name="streamlit-mosaic",
    version="0.0.1",
    author="Ploomber Inc.",
    author_email="contact@ploomber.io",
    description="Mosaic for Streamlit",
    long_description="",
    long_description_content_type="text/plain",
    url="https://github.com/ploomber/streamlit-mosaic",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
