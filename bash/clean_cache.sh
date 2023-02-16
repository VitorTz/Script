#!/bin/bash

cache_dir="~/.cache"
mozilla="${cache_dir}/mozilla"
wine="${cache_dir}/wine"
spotify="${cache_dir}/spotify"

dir=(mozilla wine spotify)
message="Done!"

function clean_cache {
    echo "Removendo cache de $1"
    rm -rf "$1/*"
}


clean_cache $mozilla
clean_cache $wine
clean_cache $spotify
echo ${message}
