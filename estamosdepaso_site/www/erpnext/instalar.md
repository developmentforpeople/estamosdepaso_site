# Setup frappe framework

## Install bench

## Bench initialize

```shell
bench init --frappe-path https://github.com/developmentforpeople/frappe --frappe-branch version-13-beta --python python3.6 --verbose bench-frappe-jaime
```

## Install ERPNext

```shell
bench get-app erpnext --branch version-13-beta https://github.com/developmentforpeople/erpnext
```

## Comenzar el bench

```shell
bench start
```

y abrir otro terminal


## Crear un sitio web

```shell
bench new-site --db-name estamosdepaso_db estamosdepaso.local
```

En modo local activaremos "developer\_mode" y "disable\_website_cache":

```shell
bench --site estamosdepaso.local set-config developer_mode 1
bench --site estamosdepaso.local set-config disable_website_cache 1
```

Habilitaremos también el scheduler (crontab):

```shell
bench --site estamosdepaso.local enable-scheduler
```

## Crear app para el sitio web

```shell
bench new-app estamosdepaso_site
```

## Instalar app en el sitio web

```shell
bench --site estamosdepaso.local install-app estamosdepaso_site
```

Añadir el sitio web local a hosts para que pueda abrirse en el navegador:

```shell
bench --site estamosdepaso.local add-to-hosts
```

Ver el puerto y abrir 

```shell
cat Procfile
```

Mira el puerto en la línea "web: bench serve --port 8005"

Abre esta url en tu navegador:

http://estamosdepaso.local:8005

Usar el usuario: Administrator
y la contraseña que usaste en el paso de crear el sitio


# Modificar el servidor web para usar Visual Studio Code para debugear

```shell
vi Procfile
```

Buscar la línea relacionada con el servidor web y comentarla:

```bash
# Comment web:... for debugging with VSC
# web: bench serve --port 8005
```

# Abrir Visual Studio Code

```shell
code apps
```

## Añadir la configuración siguiente al debugger

Visual Studio Code > Run > Open configurations

```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "bench serve --port 8005 --noreload --nothreading",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/frappe/frappe/utils/bench_helper.py",
            "args": [
                "frappe", "serve", "--port", "8005", "--noreload", "--nothreading"
            ],
            "python": "${workspaceFolder}/../env/bin/python",
            "cwd": "${workspaceFolder}/../sites",
            "env": {
                "DEV_SERVER": "1"
            },
        },
    ],
}
```