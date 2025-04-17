# Galeria de Cards - Django

Uma aplicação web simples feita com Django que exibe uma galeria de cards com busca por nome ou profissão. Também permite adicionar, editar e excluir cards dinamicamente.

## Funcionalidades

- Exibição de uma galeria de cards com imagem, nome e profissão.
- Campo de busca com filtro dinâmico (JavaScript).
- Cadastro de novos cards.
- Edição de cards existentes.
- Exclusão de cards.
- Organização dos arquivos estáticos (CSS e JS) de forma separada.

## Tecnologias Utilizadas

- Python 3
- Django 4
- HTML5, CSS3 e JavaScript
- SQLite (banco de dados padrão do Django)

## Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seuusuario/galeria-cards.git
   cd galeria-cards

2. **Crie e ative um ambiente virtual (opcional, mas recomendado)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
4. **Realize as migrações**
    ```bash
    python manage.py migrate
5. **Crie um superusuário (opcional, para acessar o admin)**
    ```bash
    python manage.py createsuperuser
6. **Inicie o servidor**
   ```bash
   python manage.py runserver
7. **Acesse no navegador**
   ```arduino
   http://localhost:8000/

## Estrutura de Pastas
```csharp
galeria/
├── cards/                  # Aplicação principal
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── templates/
│   │   └── cards/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── galeria/                # Projeto Django
│   ├── settings.py
│   ├── urls.py
├── media/                  # Imagens dos cards
├── db.sqlite3              # Banco de dados SQLite
└── manage.py



