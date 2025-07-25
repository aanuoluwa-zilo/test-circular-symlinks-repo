#!/usr/bin/env python3

import os
import sys
from pathlib import Path

def detect_circular_symlinks():
    """Detect circular symlinks without causing infinite loops."""
    
    def check_circular_path(start_path, visited=None, max_depth=10):
        if visited is None:
            visited = set()
        
        if len(visited) > max_depth:
            return True, f"Max depth exceeded at {start_path}"
        
        if start_path in visited:
            return True, f"Circular reference detected: {' -> '.join(visited)} -> {start_path}"
        
        visited.add(start_path)
        
        if os.path.islink(start_path):
            target = os.readlink(start_path)
            # Resolve relative paths
            if not os.path.isabs(target):
                target = os.path.join(os.path.dirname(start_path), target)
            target = os.path.normpath(target)
            
            if os.path.exists(target):
                return check_circular_path(target, visited.copy(), max_depth)
        
        return False, None
    
    symlinks_to_check = [
        'loop1', 'loop2', 'circle1', 'circle2', 'circle3',
        'dir1/subdir', 'dir2/subdir', 'self'
    ]
    
    print("Detecting circular symlinks...")
    
    for symlink in symlinks_to_check:
        if os.path.exists(symlink) and os.path.islink(symlink):
            is_circular, message = check_circular_path(symlink)
            if is_circular:
                print(f"⚠️  {symlink}: {message}")
            else:
                target = os.readlink(symlink)
                print(f"✅ {symlink} -> {target}")
        else:
            print(f"❌ {symlink} does not exist or is not a symlink")
    
    print("\nCircular symlink detection completed!")

if __name__ == "__main__":
    detect_circular_symlinks()
