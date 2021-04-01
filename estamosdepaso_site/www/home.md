
# home

[Instalar ERPNext](/frappe-erpnext/instalar)


Bienvenidxs

- crear site
bench new-site estamosdepaso.local

- crear app para el site
bench new-app estamosdepaso_site

- instalar app al site
bench --site estamosdepaso.local install-app estamosdepaso_site

- developer mode on y deshabilitar cache web en local
bench --site estamosdepaso.local set-config developer_mode 1
bench --site estamosdepaso.local set-config disable_website_cache 1

Añadir entrada en /etc/hosts

Mirar el puerto en /frappe-bench/Procfile

Abrir navegador en 
