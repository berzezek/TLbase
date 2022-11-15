from setuptools import setup, find_packages

# Load the README file.
with open(file="README.md", mode="r") as readme_handle:
    long_description = readme_handle.read()

setup(

    # Define the library name, this is what is used along with `pip install`.
    name='tlgroup-department',

    # Define the author of the repository.
    author='Berzezek',

    # Define the Author's email, so people know who to reach out to.
    author_email='wknduz@gmail.com',

    # Define the version of this library.
    # Read this as
    #   - MAJOR VERSION 0
    #   - MINOR VERSION 1
    #   - MAINTENANCE VERSION 0
    version='0.1.0',

    packages=find_packages(),

    # Here is a small description of the library. This appears
    # when someone searches for the library on https://pypi.org/search.
    description='SPA application with rest api server',

    # I have a long description but that will just be my README
    # file, note the variable up above where I read the file.
    long_description=long_description,


    # Here is the URL where you can find the code, in this case on GitHub.
    url='',

    # These are the dependencies the library needs in order to run.
    install_requires=[
        'asgiref==3.5.2',
        'Django==4.1.2',
        'django-cors-headers==3.13.0',
        'django-extensions==3.2.1',
        'django-shell-plus==1.1.7',
        'djangorestframework==3.14.0',
        'Faker==15.1.1',
        'mysqlclient==2.1.1',
        'python-dateutil==2.8.2',
        'pytz==2022.5',
        'six==1.16.0',
        'sqlparse==0.4.3',
    ],

    # Here are the keywords of my library.
    keywords='department hierarchy APIs',

    # # here we specify any package data.
    # package_data={

    #     # And include any files found subdirectory of the "td" package.
    #     "td": ["app/*", "templates/*"],

    # },

    # I also have some package data, like photos and JSON files, so
    # I want to include those as well.
    include_package_data=True,

    # Here I can specify the python version necessary to run this library.
    python_requires='>=3.8',

    # Additional classifiers that give some characteristics about the package.
    # For a complete list go to https://pypi.org/classifiers/.
    classifiers=[

        # I can say what phase of development my library is in.
        'Development Status :: 3 - Alpha',

        # Here I'll add the audience this library is intended for.
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Technical preview',

        # Here I'll define the license that guides my library.
        'License :: OSI Approved :: MIT License',

        # Here I'll note that package was written in English.
        'Natural Language :: English',

        # Here I'll note that any operating system can use it.
        'Operating System :: OS Independent',

        # Here I'll specify the version of Python it uses.
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',

        # Here are the topics that my library covers.
        'Topic :: Testing',

    ]
)

