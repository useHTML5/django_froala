from setuptools import setup, find_packages

setup(
    name="django_froala",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=2.2",
        'django-libsass',
        'django-compressor',
        'django_project',
        'django-filer',
    ],
)
