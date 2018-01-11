from setuptools import setup
from distutils.cmd import Command
import subprocess


class DjangoManagementCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.run_django_command()

    def run_django_command(self):
        subprocess.run(['django-admin.py',
                        self.django_command,
                        'e2e',
                        '--settings=test_project.settings',
                        '--pythonpath=.'])


def django_command(cmd, description):
    class command(DjangoManagementCommand):
        description = description
        django_command = cmd

    return command

setup(
    version='0.0.1',
    name='e2e',
    description='End-to-end crypto toolkit for Django',
    long_description=open('README.md').read(),
    url='https://github.com/jarcoal/django-e2e',
    author='Jared Morse',
    author_email='jarcoal@gmail.com',
    license='MIT',
    install_requires=[
        'django>=1.8',
    ],
    cmdclass={
        'test': django_command('test', 'run tests'),
        'makemigrations': django_command('makemigrations',
                                         'make migration files'),
    }
)
