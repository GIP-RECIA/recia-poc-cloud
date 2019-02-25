#!/usr/bin/env bash
GITCONFIG_VOLUME=

if [[ -f "$HOME/.gitconfig" ]]; then
  GITCONFIG_VOLUME="-v ${HOME}/.gitconfig:/root/.gitconfig"
fi

docker run -ti --rm \
    --network nginx-proxy -e VIRTUAL_HOST=docs.recia-env.test -e VIRTUAL_PORT=8000 \
    $GITCONFIG_VOLUME \
    -v $(pwd):/docs \
    squidfunk/mkdocs-material $@