#!/bin/bash

sudo mkdir /mnt/HD
sudo mkdir /mnt/HD/TMP
sudo systemctl enable fstrim.timer

git config --global user.name "VitorTz"
git config --global user.email "vitor.ftz@outlook.com"

sudo pacman -S --needed --noconfirm git base-devel

git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
cd ..

yay -Syu --noconfirm spotify stacer discord visual-studio-code-bin android-studio gimp firefox alacritty ttf-jetbrains-mono
sudo pacman -R firedragon firedragon-extension-plasma-integration octopi kate

mv alacritty.yml ~/.config/alacritty

git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.11.2
mv config.fish ~/.config/fish
mkdir -p ~/.config/fish/completions; and ln -s ~/.asdf/completions/asdf.fish ~/.config/fish/completions

fish

asdf plugin add java
asdf plugin add kotlin
asdf plugin add dart

asdf install java openjdk-20
asdf install kotlin 1.8.0
asdf install dart latest

asdf global dart latest
asdf global java openjdk-20
asdf global kotlin 1.8.0
