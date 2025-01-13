#!/bin/bash

# Variables iniciales
BASE_DN="dc=megainfo209,dc=com"
OU="people"
GID_NUMBER=2000
UID_NUMBER=2006

# Archivo de salida
OUTPUT_FILE="usuarios.ldif"
> "$OUTPUT_FILE"

# Leer archivo datos.txt
for LINE in $(cat datos.txt); do
    # Separar campos usando IFS
    IFS=',' read -r NOMBRE APELLIDO MAIL PHOTO USUARIO <<< "$LINE"
    
    # Crear contraseñas en formato MD5
    PASSWORD=$(slappasswd -h {MD5} -s "$USUARIO")
    
    # Generar entrada LDIF
    echo "dn: uid=$USUARIO,ou=$OU,$BASE_DN" >> "$OUTPUT_FILE"
    echo "objectClass: top" >> "$OUTPUT_FILE"
    echo "objectClass: posixAccount" >> "$OUTPUT_FILE"
    echo "objectClass: inetOrgPerson" >> "$OUTPUT_FILE"
    echo "objectClass: shadowAccount" >> "$OUTPUT_FILE"
    echo "uid: $USUARIO" >> "$OUTPUT_FILE"
    echo "sn: $APELLIDO" >> "$OUTPUT_FILE"
    echo "givenName: $NOMBRE" >> "$OUTPUT_FILE"
    echo "cn: $NOMBRE$APELLIDO" >> "$OUTPUT_FILE"
    echo "uidNumber: $UID_NUMBER" >> "$OUTPUT_FILE"
    echo "gidNumber: $GID_NUMBER" >> "$OUTPUT_FILE"
    echo "userPassword: $PASSWORD" >> "$OUTPUT_FILE"
    echo "homeDirectory: /home/$USUARIO" >> "$OUTPUT_FILE"
    echo "loginShell: /bin/bash" >> "$OUTPUT_FILE"
    echo "mail: $MAIL" >> "$OUTPUT_FILE"
    echo "jpegPhoto: < file:$(pwd)/$PHOTO" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    
    # Incrementar UID
    ((UID_NUMBER++))
done

echo "Archivo LDIF generado: $OUTPUT_FILE"
