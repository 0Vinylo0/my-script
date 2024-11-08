#!/bin/bash
read -p "Maquina inicio" mv_inicio
read -p "Maquina final" mv_fin
for i in {$mv_inicio..$mv_fin}; do
    qm stop $i
done
