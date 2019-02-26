#!/usr/bin/env python
# Rodrigo Alfaro, 21/06/2018
# Curso Linux II
# netstream
import os
import time

# Configuracion
username = 'curso'
password = 'curso'
hostname = 'localhost'
port = 3306
dest_folder = '/home/ralf/Descargas'
not_backup = ['information_schema', 'test', 'mysql', 'performance_schema']
#
filestamp = time.strftime('%Y%m%d')
database_list_command="mysql -u%s -p%s -h %s -P %s --silent -N -e 'show databases'" % (username, password, hostname, port)
for database in os.popen(database_list_command).readlines():
        database = database.strip()
        if database in not_backup:
                continue
        filename = "%s/%s-%s.sql" % (dest_folder, filestamp, database)
        # dump + gzip command
        os.popen("mysqldump -u%s -p%s -h %s -P %s -e --opt -c %s | gzip -c > %s.gz" % (username, password, hostname, port, database, filename))
# Agregar esta linea a la tabla de cron /etc/crontab
# 0 0 * * * python /ruta/backup.py
