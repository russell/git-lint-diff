from distutils.core import setup

setup(name='git-lint-diff',
      version='1.0',
      description='Run flake8 against only changed lines.',
      author='Russell Sim',
      author_email='russell.sim@gmail.com',
      install_requires=['flake8'],
      scripts=['git-lint-diff'])
