# Circular Symlinks Repository

This repository demonstrates circular symbolic links that can create infinite loops when traversed.

## ⚠️ WARNING: Circular Symlinks

These symlinks create circular references that can cause infinite loops in file system traversal!

### Circular Link Examples

1. **Simple Circular**:
   - `loop1` → `loop2`
   - `loop2` → `loop1`

2. **Three-Way Circular**:
   - `circle1` → `circle2`
   - `circle2` → `circle3`
   - `circle3` → `circle1`

3. **Directory Circular**:
   - `dir1/subdir` → `../dir2`
   - `dir2/subdir` → `../dir1`

4. **Self-Reference**:
   - `self` → `self`

## Expected Circular Symlinks
1. loop1 -> loop2
2. loop2 -> loop1
3. circle1 -> circle2
4. circle2 -> circle3
5. circle3 -> circle1
6. dir1/subdir -> ../dir2
7. dir2/subdir -> ../dir1
8. self -> self

## Testing Safely
Use the provided validation script to detect circular references without causing infinite loops.
