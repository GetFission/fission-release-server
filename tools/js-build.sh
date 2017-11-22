#!/bin/bash

set -e

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" # This loads nvm

nvm use v8.9.1

npm install
npm run build
echo "Build complete installed"
