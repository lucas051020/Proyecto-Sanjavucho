# 🛒 Tienda E-Commerce "Sanjavucho"

**Sanjavucho** es una plataforma web de comercio electrónico desarrollada en **Django**, diseñada para la gestión y venta de productos de tecnología, videojuegos y accesorios.
El sistema moderniza el proceso de ventas permitiendo la gestión automática de **precios mayoristas** (por volumen), control de stock y formalización de pedidos con integración a **WhatsApp**.

---

## 🔗 Enlaces
👉 [**Ver Repositorio en GitHub**](https://github.com/lucas051020/Proyecto-Sanjavucho.git)

---

## ✨ Características Principales

### 👤 Para Clientes (Frontend)
- 🛍️ **Catálogo Dinámico:** Filtrado por categorías y subcategorías.
- 🔍 **Buscador:** Búsqueda por nombre, descripción o código (SKU).
- 💰 **Precios por Volumen:** Cálculo automático de descuentos al agregar cantidad (ej: x10, x50).
- 🛒 **Carrito de Compras:** Gestión de ítems en tiempo real (Persistencia en sesión).
- 🔒 **Seguridad:** Registro, Login y gestión de "Mi Perfil" (Datos de envío).
- 📱 **Checkout:** Generación de pedido y redirección a WhatsApp para coordinar pago.

### 🛡️ Para Administradores (Backoffice)
- 📦 **Gestión de Productos:** ABM completo con soporte para imágenes múltiples.
- 📊 **Importación Masiva:** Carga de catálogos desde Excel/CSV (`django-import-export`).
- 🖨️ **Reportes:** Impresión de "Hoja de Pedido" y "Ficha de Cliente" en formato limpio.
- ❓ **FAQ:** Gestión de preguntas frecuentes dinámicas.

---

## 🛠️ Stack Tecnológico

| Área | Tecnología | Uso |
|------|------------|-----|
| **Backend** | ![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white) | Lógica del servidor |
| **Framework** | ![Django](https://img.shields.io/badge/Django-4.x-092E20?logo=django&logoColor=white) | Estructura MTV, ORM, Auth |
| **Frontend** | ![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?logo=bootstrap&logoColor=white) | Diseño responsivo y componentes |
| **DB** | ![SQLite](https://img.shields.io/badge/SQLite-Development-003B57?logo=sqlite&logoColor=white) | Base de datos (Entorno Local) |
| **Librerías** | `Pillow`, `django-import-export` | Procesamiento de imágenes y datos |

---

## 📂 Estructura del Proyecto

```bash
Proyecto-Sanjavucho/
│
├── mi_tienda/          # Configuración global (settings.py, urls.py)
│
├── tienda_app/         # Módulo Núcleo
│   ├── models.py       # Productos, Categorías, Pedidos
│   ├── views.py        # Lógica del catálogo
│   └── templates/      # HTML (Home, Detalle, FAQ)
│
├── cart/               # Módulo Carrito
│   ├── cart.py         # Lógica de sesión (Cálculo de precios)
│   └── views.py        # Agregar/Eliminar ítems
│
├── accounts/           # Módulo Usuarios
│   ├── models.py       # Perfil extendido (Profile)
│   └── views.py        # Login, Registro, Edición Perfil
│
├── pedidos/            # Módulo Checkout
│   └── views.py        # Creación de Pedido y Confirmación
│
├── static/             # CSS personalizado y JS
└── media/              # Imágenes de productos (subidas por admin)

## ⚙️ Instalación y Ejecución (Local)
- Clonar el repositorio:
git clone [https://github.com/lucas051020/Proyecto-Sanjavucho.git](https://github.com/lucas051020/Proyecto-Sanjavucho.git)
cd Proyecto-Sanjavucho
- Crear entorno virtual:
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
- Instalar dependencias:
pip install -r requirements.txt
- Migrar base de datos y correr:
python manage.py migrate
python manage.py runserver
- Acceder:
Web: http://127.0.0.1:8000/
Admin: http://127.0.0.1:8000/admin/