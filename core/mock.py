class Mock:

    country = {
        'country_name': 'Romania',
        'country_code': 'RO'
    }

    user_a = {
        'username': 'user_a',
        'email': 'some@email.com',
        'password': 'secret2'
    }

    user_b = {
        'username': 'user_b',
        'email': 'test@example.com',
        'password': 'secret'
    }

    credentials_a = {
        'username': 'user_a',
        'password': 'secret2'
    }

    credentials_b = {
        'username': 'user_b',
        'password': 'secret'
    }

    company_a = {
        'company_name': 'SC Some Company SRL',
        'employees_no': 4,
        'description': 'Lorem ipsum',
        'country': 1,
        'county': 'Bucharest',
        'city': 'Bucharest',
        'slug_name': 'some_company',
        'email': 'admin@hi.com',
        'phone': '0222999222',
        'external_link': 'www.example.com',
    }

    company_b = {
        'company_name': 'SC Other Company SRL',
        'employees_no': 9,
        'description': 'Lorem ipsum',
        'country': 1,
        'county': 'Chicago',
        'city': 'Buffalo',
        'slug_name': 'other_company',
        'email': 'test@hi.com',
        'phone': '234242343321',
        'external_link': 'www.demo.com',
    }

    company_a_edited = {
        'company_name': 'SC Changed Name SRL',
        'employees_no': 47,
        'description': 'Lorem ipsum dolor sic amet',
        'country': 1,
        'county': 'Bucharest',
        'city': 'Bucharest',
        'slug_name': 'some_company',
        'email': 'admin@hi.com',
        'phone': '000111111111',
        'external_link': 'www.example.com',
    }

    company_a_patched = {
        'slug_name': 'changed_name',
        'email': 'test@example.com'
    }

    def __init__(self):
        pass
