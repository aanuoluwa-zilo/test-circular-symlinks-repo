#!/bin/bash

echo "Creating circular symbolic links (use with caution!)..."

# Create directories
mkdir -p dir1 dir2

# Create simple circular symlinks
ln -sf loop2 loop1
ln -sf loop1 loop2

# Create three-way circular symlinks
ln -sf circle2 circle1
ln -sf circle3 circle2
ln -sf circle1 circle3

# Create directory circular symlinks
ln -sf ../dir2 dir1/subdir
ln -sf ../dir1 dir2/subdir

# Create self-referencing symlink
ln -sf self self

echo "Circular symlinks created (potentially dangerous!)"
echo "Current circular symlinks:"
ls -la loop1 loop2 circle1 circle2 circle3 self
ls -la dir1/subdir dir2/subdir
