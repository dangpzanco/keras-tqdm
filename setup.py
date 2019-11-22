from setuptools import setup, find_packages

long_description = open('README.rst').read()
VERSION = '2.0.1'
setup(name='keras_tqdm',
      version=VERSION,
      install_requires=['tensorflow', 'tqdm'],
      author="Ben Striner",
      author_email="dangpzanco@gmail.com",
      url="https://github.com/dangpzanco/keras-tqdm",
      download_url='https://github.com/dangpzanco/keras-tqdm/tarball/v{}'.format(VERSION),
      description="Keras models with TQDM progress bars in Jupyter notebooks",
      long_description=long_description,
      keywords=['tf.keras', 'tqdm', 'progress', 'progressbar', 'ipython', 'jupyter'],
      license='MIT',
      classifiers=[
          # Indicate who your project is intended for
          'Intended Audience :: Developers',
          # Pick your license as you wish (should match "license" above)
          'License :: OSI Approved :: MIT License',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3'
      ],
      packages=find_packages())
