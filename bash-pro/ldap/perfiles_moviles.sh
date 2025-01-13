#!/bin/bash

for i in $(cat final.temp); do
    # Separar campos usando IFS
    IFS=':' read -r _ uid _ uidNumber _ gidNumber _ homeDirectory <<< "$i"
	mkdir $homeDirectory
	cp /etc/skel/.* $homeDirectory
	chown -R $uidNumber:$gidNumber $homeDirectory
echo "dn:uid=$uid,ou=people,dc=megainfo209,dc=com" >> modify.ldif
echo "changetype: modify" >> modify.ldif
echo "replace: homeDirectory" >> modify.ldif
echo "homeDirectory: $homeDirectory" >> modify.ldif
echo "" >> modify.ldif
done
