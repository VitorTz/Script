#!/bin/bash

sudo mkdir /mnt/HD
sudo systemctl enable fstrim.timer

git config --global user.name "VitorTz"
git config --global user.email "vitor.ftz@outlook.com"

sudo pacman -S --needed --noconfirm git base-devel

git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si

yay -Syu --noconfirm
cd

yay -S --noconfirm spotify discord visual-studio-code-bin android-studio gimp firefox alacritty papirus-icon-theme

sudo pacman -R firedragon firedragon-extension-plasma-integration octopi kate

