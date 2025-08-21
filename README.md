🔐 Sistema de Autenticación con Django, JWT y Roles de Usuario

Este proyecto es un sistema de autenticación en Django que permite:

Registro de usuarios

Inicio de sesión con JWT (JSON Web Tokens)

Renovación de tokens

Asignación de roles de usuario (admin, staff, usuario normal)

Endpoints protegidos según rol

Es una base sólida para construir aplicaciones web más grandes con Django REST Framework.

---

⚙️ Tecnologías utilizadas

Django 5

Django REST Framework

Simple JWT

---

🚀 Instalación y Configuración

1️⃣ Clonar el repositorio

git clone https://github.com/tuusuario/django-auth-jwt.git

cd django-auth-jwt

2️⃣ Crear entorno virtual

python -m venv venv

source venv/bin/activate   # Linux / Mac

venv\Scripts\activate      # Windows

3️⃣ Instalar dependencias

pip install -r requirements.txt

4️⃣ Migrar la base de datos

python manage.py migrate

5️⃣ Crear superusuario

python manage.py createsuperuser

6️⃣ Ejecutar servidor

python manage.py runserver

---

🔑 Endpoints disponibles

👤 Autenticación

Método	Endpoint	Descripción
POST	/api/auth/register/	Registro de usuario
POST	/api/auth/login/	Login con JWT (obtener access y refresh token)
POST	/api/auth/refresh/	Renovar token de acceso
GET	/api/auth/me/	Obtener perfil del usuario autenticado

📌 Ejemplo para registro:

POST /api/auth/register/
{
  "username": "jorge",
  "password": "123456",
  "email": "jorge@example.com"
}


📌 Ejemplo para login:

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

🔒 Endpoints protegidos según rol
Método	Endpoint	Rol necesario
GET	/api/admin-only/	Solo admin
GET	/api/staff-only/	Staff y admin

📌 Ejemplo de uso en Postman:
Agregar en Headers:

Authorization: Bearer <tu_access_token>

📂 Estructura del proyecto
django-auth-jwt/
│── core/                # Proyecto principal
│   ├── settings.py      # Configuración de Django
│   ├── urls.py          # Rutas principales
│── auth_app/            # App de autenticación
│   ├── views.py         # Lógica de registro, login, perfil
│   ├── urls.py          # Rutas de auth
│   ├── serializers.py   # Serializadores DRF
│── db.sqlite3           # Base de datos
│── manage.py
│── requirements.txt

👥 Roles de usuario en Django

Superuser → tiene permisos de admin

Staff → usuario con acceso especial (pero no admin total)

Usuario normal → permisos limitados

Puedes asignar roles desde:

python manage.py createsuperuser


o en el Django Admin Panel en:
👉 http://127.0.0.1:8000/admin/

📌 Notas importantes

Si visitas /api/ directamente, verás un 404, porque no hay endpoint definido en esa ruta.

Usa las rutas documentadas arriba (/api/auth/..., /api/admin-only/, etc.).

Puedes extender este sistema para incluir perfiles de usuario, permisos personalizados, integración con frontend (React, Vue, Angular).

---

👨‍💻 Autor

Jorge Patricio Santamaría Cherrez

Máster en Ingeniería de Software y Sistemas Informáticos
