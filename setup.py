from setuptools import find_packages
from setuptools import setup
from setuptools.command.install import install
from subprocess import check_call

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]


class PostInstallCommand(install):

    def run(self):
        check_call("conda install -c conda-forge fbprophet".split())
        install.run(self)

setup(
    name='package',
    version="1.0",
    description="Project Description",
    packages=find_packages(),
    install_requires=requirements,
    test_suite='tests',
    # include_package_data: to install data from MANIFEST.in
    include_package_data=True,
    scripts=['scripts/business_case_869-run'],
    cmdclass={
        "install": PostInstallCommand,
    },
    zip_safe=False)
