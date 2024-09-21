from setuptools import setup

setup(
    name='fixer_demo',
    version='0.2',
    description="Fixer Service demo packages",
    url="https://github.com/MohsenVerdizadeh/fixer-demo.git",
    author="mohsen",
    author_email='mohsenverdizadehkohi@gmail.com',
    license='MIT',
    packages=['fixer'],
    install_requiers=['requests'],
    zip_safe=False
)
