🔐 Sistema de Autenticación con Django, JWT y Roles de Usuario

Este proyecto es un sistema de autenticación en Django que permite:

- Registro de usuarios

- Inicio de sesión con JWT (JSON Web Tokens)

- Renovación de tokens

- Asignación de roles de usuario (admin, staff, usuario normal)

- Endpoints protegidos según rol

Es una base sólida para construir aplicaciones web más grandes con Django REST Framework.

---

⚙️ Tecnologías utilizadas

- Python 3.12+
- Django 5.0.6
- Django REST Framework 3.15.1
- JWT (djangorestframework-simplejwt)

---

📦 Instalación y ejecución 

1. Clona el repositorio

```bash

git clone https://github.com/Patogol35/django-auth-jwt.git

```

2. Ingresa a la carpeta del proyecto

```bash

cd django-auth-jwt

```

3. Crea el entorno virtual

```bash

python -m venv venv

```
En Linux/Mac: 

```bash

source venv/bin/activate

```

En Windows: 

```bash

venv\Scripts\activate

```   

4. Instala las dependencias

```bash

pip install -r requirements.txt

```

5. Realiza las Migraciones

```bash

python manage.py migrate

```

6. Crea un superusuario

```bash

python manage.py createsuperuser

```

7. Ejecuta el servidor

```bash

python manage.py runserver

```

8. El servidor estará disponible en:

👉 http://127.0.0.1:8000

---

🔗 Endpoints disponibles

- Autenticación

POST	/api/auth/register/	Registro de usuario

POST	/api/auth/login/	Login con JWT (obtener access y refresh token)

POST	/api/auth/refresh/	Renovar token de acceso

GET	/api/auth/me/	Obtener perfil del usuario autenticado

- Ejemplo para registro:

POST /api/auth/register/
{
  "username": "jorge",
  "password": "123456",
  "email": "jorge@example.com"
}


- Ejemplo para login:

POST /api/auth/login/
{
  "username": "jorge",
  "password": "123456"
}


Respuesta:

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGci...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGci..."
}

- Endpoints protegidos según rol

GET	/api/admin-only/	Solo admin

GET	/api/staff-only/	Staff y admin

- Ejemplo de uso en Postman:
Agregar en Headers:

Authorization: Bearer <tu_access_token>

---

👥 Roles de usuario en Django

Superuser → tiene permisos de admin

Staff → usuario con acceso especial (pero no admin total)

Usuario normal → permisos limitados

Puedes asignar roles desde:

python manage.py createsuperuser


o en el Django Admin Panel en:

👉 http://127.0.0.1:8000/admin/

Notas importantes

Si visitas /api/ directamente, verás un 404, porque no hay endpoint definido en esa ruta.

Usa las rutas documentadas arriba (/api/auth/..., /api/admin-only/, etc.).

Puedes extender este sistema para incluir perfiles de usuario, permisos personalizados, integración con frontend (React, Vue, Angular).

---

👨‍💻 Autor

Jorge Patricio Santamaría Cherrez

Máster en Ingeniería de Software y Sistemas Informáticos
