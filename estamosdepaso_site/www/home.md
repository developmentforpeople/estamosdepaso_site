
# home

[Instalar ERPNext](/erpnext/instalar)


Bienvenidxs

- crear site
```shell
bench new-site estamosdepaso.local
```

- crear app para el site
```shell
bench new-app estamosdepaso_site
```

- instalar app al site
```shell
bench --site estamosdepaso.local install-app estamosdepaso_site
```

- developer mode on y deshabilitar cache web en local
```shell
bench --site estamosdepaso.local set-config developer_mode 1
bench --site estamosdepaso.local set-config disable_website_cache 1
```

Añadir entrada en /etc/hosts

Mirar el puerto en /frappe-bench/Procfile

Abrir navegador en 
