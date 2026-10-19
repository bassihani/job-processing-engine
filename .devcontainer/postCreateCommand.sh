#!/bin/bash
set -e

# Install uv if it is not present
curl -LsSf https://astral.sh/uv/install.sh | sh

# Ensure uv is added to the PATH for the current script session
export PATH="$HOME/.local/bin:$PATH"
echo 'export PYTHONDONTWRITEBYTECODE=1' >> ~/.bashrc

# Install your dependencies
uv sync
