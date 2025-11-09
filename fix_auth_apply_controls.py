#!/usr/bin/env python3
"""
Fix authentication flow to properly call applyEditControls() and fix syntax errors.
"""

import re
from pathlib import Path

def fix_auth_flow(file_path):
    """Fix authentication flow to call applyEditControls after setting isEditModeEnabled."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix 1: Add applyEditControls() call after isEditModeEnabled = (userRole !== 'viewer');
    pattern1 = r"(isEditModeEnabled = \(userRole !== 'viewer'\);)\s*// Apply controls after next renderconsole\.log\(`✅ Logged in as \$\{user\.email\} \(\$\{userRole\}\)`\);"
    replacement1 = r"\1\n                applyEditControls();\n                console.log(`✅ Logged in as ${user.email} (${userRole})`);"
    content = re.sub(pattern1, replacement1, content)
    
    # Fix 2: Add applyEditControls() call after isEditModeEnabled = false;
    pattern2 = r"(isEditModeEnabled = false;)\s*// Apply controls after next renderconsole\.log\('👁️ Viewing as guest \(read-only\)'\);"
    replacement2 = r"\1\n                applyEditControls();\n                console.log('👁️ Viewing as guest (read-only)');"
    content = re.sub(pattern2, replacement2, content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Fixed {file_path.name}")
        return True
    else:
        print(f"⏭️  No changes needed for {file_path.name}")
        return False

def main():
    # Get all bracket HTML files
    bracket_files = list(Path('.').glob('Bracket_*.html'))
    
    if not bracket_files:
        print("❌ No bracket files found!")
        return
    
    print(f"Found {len(bracket_files)} bracket files")
    print("=" * 60)
    
    updated_count = 0
    for file_path in sorted(bracket_files):
        if fix_auth_flow(file_path):
            updated_count += 1
    
    print("=" * 60)
    print(f"\n✅ Complete! Fixed {updated_count} files")
    print("\n📝 Changes made:")
    print("   ✅ Added applyEditControls() call after setting isEditModeEnabled")
    print("   ✅ Fixed syntax errors in console.log statements")
    print("   ✅ Editor/Admin users will now have proper edit access")

if __name__ == '__main__':
    main()

