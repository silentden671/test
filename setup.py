from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='package_name_my_frame_dimonlimon',
  version='1.0.0',
  author='dimonlimon',
  author_email='dimapahtusov77@gmail.com',
  description='Тут мой первый фрейм',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/silentden671',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='example python',
  project_urls={
    'Documentation': 'https://github.com/silentden671'
  },
  python_requires='>=3.7'
)
