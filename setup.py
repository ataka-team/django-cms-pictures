from setuptools import setup, find_packages

version = "0.0.0"

setup(
    name = 'django-cms-pictures',
    version = version,
    description = 'Django CMS Pictures Plugins',
    author = 'Pablo Saavedra',
    author_email = 'pablo.saavedra@treitos.com',
    url = 'http://github.com/psaavedra/django-cms-pictures',
    packages = find_packages(),
    package_data={
        'cms_pictures_polaroid': [
            'templates/cms_pictures_polaroid/*.html',
        ],
        'cms_pictures_slider': [
            'templates/cms_pictures_slider/*.html',
        ],
    },
    zip_safe=False,
    install_requires=[
        "django-cms>=2.1",
    ]

    download_url= 'https://github.com/psaavedra/django-cms-pictures/zipball/master',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description=file('README').read(),
    license=file('MIT_License.txt').read(),
    keywords = "django cms polaroid slider photos pictures",
)
