FROM odoo:17

# Passer en root pour installer les paquets
USER root

# Installer les dépendances système (optionnel selon besoins)
RUN apt-get update && apt-get install -y \
    git \
    nano \
    && rm -rf /var/lib/apt/lists/*

# Installer html2text avec pip
RUN pip3 install html2text

RUN pip3 install wkhtmltopdf
# Installer les dépendances pour imprimer des PDF
RUN apt-get update && apt-get install -y \
xfonts-75dpi \
xfonts-base \
fontconfig \
libfreetype6-dev \
libjpeg-dev \
libxrender1 \
libxext6 \
libfontconfig1 \
libx11-6 \
libxrender1 \
libxtst6 \
xfonts-utils \
xfonts-encodings \
xfonts-scalable

# Installer numpy avec pip
RUN pip3 install numpy

# Installer numpy avec pip
RUN pip3 install numpy-financial

# Installer les dépendances système
RUN apt-get update && \
    apt-get install -y wget gnupg && \
    echo "deb http://apt.postgresql.org/pub/repos/apt jammy-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O- | gpg --dearmor -o /usr/share/keyrings/postgresql.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/postgresql.gpg] http://apt.postgresql.org/pub/repos/apt jammy-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    apt-get update && \
    apt-get install -y python3-pip gcc libpq-dev && \
    pip3 install --no-cache-dir pandas openpyxl

# Revenir à l'utilisateur Odoo
USER odoo

# Créer le répertoire des modules personnalisés
RUN mkdir -p /mnt/extra-addons

# Copier les modules personnalisés dans le conteneur (si présents)
COPY ./addons /mnt/extra-addons