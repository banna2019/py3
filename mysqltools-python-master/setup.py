from distutils.core import setup

setup(name='mysqltools-python',
      version='2.19.03.13',
      scripts=['bin/mtlsmonitor','bin/mtlsbackup','bin/mtlslog','bin/mtlsanalysis'],
      packages=['mtls'],
      maintainer='Neeky',
      maintainer_email='neeky@live.com',
      url='https://github.com/Neeky/mysqltools-python',
      install_requires=['mysql-connector-python>=8.0.12'],
      python_requires='>=3.1.*,'
      )


      
