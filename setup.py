from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'hs_django_admin', 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "A customizable Django admin interface with enhanced styling and system information display."

# Read version from __init__.py
def get_version():
    init_path = os.path.join(os.path.dirname(__file__), 'hs_django_admin', '__init__.py')
    with open(init_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split('=')[1].strip().strip('"\'')
    return '0.1.0'

setup(
    name='hs-django-admin',
    version=get_version(),
    description='A customizable Django admin interface with enhanced styling and system information display',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    author='Himel',
    author_email='contact@himelrana.com',
    url='https://github.com/Swe-HimelRana/hs-django-admin',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=4.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 5.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.8',
    keywords='django admin interface customization styling',
    project_urls={
        'Bug Reports': 'https://github.com/Swe-HimelRana/hs-django-admin/issues',
        'Source': 'https://github.com/Swe-HimelRana/hs-django-admin',
        'Documentation': 'https://github.com/Swe-HimelRana/hs-django-admin#readme',
    },
) 