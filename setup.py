import setuptools 

with open('README.md') as f: 
  readme = f.read()

setuptools.setup(
  name='mnzipcode',
  version='0.1.24',
  author='Bekkage',
  author_email='bilguunsec@gmail.com',
  url='https://github.com/bekkage/mnzipcode',
  description='mnzipcode is a simple library for querying Mongolian zip codes.',
  package_data={
    'mnzipcode': ['data.json.bz2']
  },
  long_description_content_type= 'text/markdown',
  long_description=readme,
  keywords='mnzipcode zipcode mongolia mn zip code',
  package=['mnzipcode'],
  include_package_data=True,
)