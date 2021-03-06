import setuptools

setuptools.setup(name='nose2-cov',
                 version='1.0a4',
                 description='nose2 plugin for coverage reporting, including subprocesses and multiprocessing',
                 long_description=open('README.txt').read().strip(),
                 author='Meme Dough',
                 author_email='memedough@gmail.com',
                 url='http://bitbucket.org/memedough/nose2-cov/overview',
                 py_modules=['nose2_cov'],
                 install_requires=['nose2>=0.1',
                                   'cov-core>=1.6'],
                 license='MIT License',
                 zip_safe=False,
                 keywords='nose2 cover coverage',
                 classifiers=['Development Status :: 4 - Beta',
                              'Intended Audience :: Developers',
                              'License :: OSI Approved :: MIT License',
                              'Operating System :: OS Independent',
                              'Programming Language :: Python',
                              'Programming Language :: Python :: 2.4',
                              'Programming Language :: Python :: 2.5',
                              'Programming Language :: Python :: 2.6',
                              'Programming Language :: Python :: 2.7',
                              'Programming Language :: Python :: 3.0',
                              'Programming Language :: Python :: 3.1',
                              'Topic :: Software Development :: Testing'])
