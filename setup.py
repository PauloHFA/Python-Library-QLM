from setuptools import setup, find_packages

setup(
    name='my_quantum_lib',  # Nome do pacote
    version='0.1.0',  # Versão do pacote
    author='Nome',  #Nossos nomes
    author_email='algumemailquevamosdecidir@example.com',  #e-mail
    description='Uma biblioteca para programação quântica com implementação de portas quânticas e algoritmos.',  # Descrição do pacote
    long_description=open('README.md').read(),  # Ler a descrição longa de um arquivo README
    long_description_content_type='text/markdown',  # Tipo de conteúdo do README
    url='https://github.com/seunome/my_quantum_lib',  # URL ainda vamos subir
    packages=find_packages(),  # Encontra automaticamente os pacotes
    classifiers=[
        'Programming Language :: Python :: 3',  # Compatibilidade com Python 3
        'License :: OSI Approved :: MIT License',  # Ainda não existe
        'Operating System :: OS Independent',  # Compatibilidade com sistemas operacionais
    ],
    python_requires='>=3.6',  # Requisitos de versão do Python
)
