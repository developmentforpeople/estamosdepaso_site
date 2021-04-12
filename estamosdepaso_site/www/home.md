
# Así es, estamos de paso

Lorem ipsum dolor sit amet, **consectetur** adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nec sagittis aliquam malesuada bibendum arcu. Tellus rutrum tellus pellentesque eu tincidunt. Pellentesque dignissim enim sit amet venenatis urna cursus. Luctus accumsan tortor posuere ac ut consequat semper viverra nam. Nisi lacus sed viverra tellus in. Turpis nunc eget lorem dolor sed viverra ipsum. Adipiscing bibendum est ultricies integer quis auctor. Turpis nunc eget lorem dolor sed viverra. Magna ac placerat vestibulum lectus mauris ultrices eros in cursus. Lobortis scelerisque fermentum dui faucibus in ornare quam viverra. Netus et malesuada fames ac turpis egestas maecenas.

Ut tortor **pretium viverra suspendisse**. Commodo odio aenean sed adipiscing. Sed elementum tempus egestas sed. Suscipit tellus mauris a diam maecenas sed enim ut sem. Dignissim convallis aenean et tortor at risus. Et ligula ullamcorper malesuada proin. Et ultrices neque ornare aenean. Elementum integer enim neque volutpat ac tincidunt vitae semper quis. Viverra orci sagittis eu volutpat odio facilisis mauris sit. Massa tincidunt nunc pulvinar sapien et. Feugiat pretium nibh ipsum consequat nisl vel pretium lectus quam. Enim sit amet venenatis urna cursus eget nunc. Amet dictum sit amet justo donec enim. Morbi enim nunc faucibus a pellentesque. Est velit egestas dui id ornare arcu odio. Sollicitudin tempor id eu nisl nunc mi ipsum faucibus. Scelerisque eleifend donec pretium vulputate sapien. Sagittis nisl rhoncus mattis rhoncus urna neque viverra justo. Augue eget arcu dictum varius duis at consectetur lorem donec. Cum sociis natoque penatibus et magnis dis parturient.

Cómo [Instalar ERPNext](/erpnext/instalar).

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
