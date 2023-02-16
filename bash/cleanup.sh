#!/bin/bash
# Remove orphans, limpa cache do pacman e yay e remove arquios temporarios

sudo pacman -R $(pacman -Qdt | awk '{print $1}') --noconfirm
sudo pacman -Scc --noconfirm && yay -Scc --noconfirm
rm -rf /mnt/HD/TMP/*

echo Done!