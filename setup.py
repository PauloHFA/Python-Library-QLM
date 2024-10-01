from setuptools import setup, find_packages

setup(
    name='Quantum_lib',  # Nome do pacote
    version='0.1.0',  # Versão do pacote
    author='Nome',  #Nossos nomes
    author_email='paulo.henrique@gmail.com',  #e-mail
    description='Uma biblioteca para programação quântica com implementação de portas quânticas e algoritmos.',  # Descrição do pacote
    long_description=open('README.md').read(),  # Ler a descrição longa de um arquivo README
    long_description_content_type='text/markdown',  # Tipo de conteúdo do README
    url='https://github.com/PauloHFA/Python-Library-QLM',  
    packages=find_packages(),  # Encontra automaticamente os pacotes
    classifiers=[
        'Programming Language :: Python :: 3',  # Compatibilidade com Python 3
        'License :: OSI Approved :: MIT License',  # 
        'Operating System :: OS Independent',  # Compatibilidade com sistemas operacionais
    ],
    python_requires='>=3.6',  # Requisitos de versão do Python
)
