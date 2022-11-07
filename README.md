# dj_shop_v_0.1

###### с директории с poetry.toml
    poetry shell
    poetry install
    

это установит все зависимости в виртуальное окружение и активирует его


###### to cteate tables
    poetry run python3 manage.py makemigrations && poetry run python3 manage.py migrate
###### to cteate admin    
    poetry run python3 manage.py createsuperuser
###### to startapp
    poetry run python3 manage.py runserver


`localhost:8000` - main
`localhost:8000/admin/` - adminka
`localhost:8000/about_us/` - aboutUs