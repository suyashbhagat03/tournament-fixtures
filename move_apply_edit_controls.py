#!/usr/bin/env python3
"""
Move applyEditControls() function outside Firebase block.
"""

import re
from pathlib import Path

def move_apply_edit_controls(file_path):
    """Move applyEditControls function outside Firebase block."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Find and remove applyEditControls from inside the Firebase/auth block
    # It's typically after the onAuthStateChanged block
    pattern = r'\}\);\s*\n\s*\n\s*// Apply edit controls \(called after bracket renders\)\s*\n\s*function applyEditControls\(\) \{[^}]*\{[^}]*\}[^}]*\{[^}]*\}[^}]*\{[^}]*\}[^}]*\{[^}]*\}[^}]*\{[^}]*\}[^}]*\}\s*\n\s*\}'
    
    # More robust: find the entire applyEditControls function
    apply_edit_pattern = r'(// Apply edit controls \(called after bracket renders\)\s*\n\s*function applyEditControls\(\) \{(?:[^{}]|\{[^{}]*\})*\}\s*\n\s*)'
    
    # Extract the function
    apply_edit_match = re.search(apply_edit_pattern, content, re.MULTILINE | re.DOTALL)
    
    if not apply_edit_match:
        print(f"⚠️  Could not find applyEditControls in {file_path.name}")
        return False
    
    apply_edit_function = apply_edit_match.group(1)
    
    # Remove it from its current location (inside auth block)
    content = content.replace(apply_edit_function, '')
    
    # Find where to insert it (after the Firebase block ends)
    firebase_end_pattern = r"(\} else \{\s*\n\s*updateFirebaseStatus\('🔥 Not Configured', 'pending'\);\s*\n\s*\}\s*\n\s*)"
    
    firebase_end_match = re.search(firebase_end_pattern, content, re.MULTILINE)
    
    if not firebase_end_match:
        print(f"⚠️  Could not find Firebase block end in {file_path.name}")
        return False
    
    # Insert applyEditControls after the Firebase block
    insert_pos = firebase_end_match.end()
    content = content[:insert_pos] + '\n        ' + apply_edit_function + content[insert_pos:]
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Fixed {file_path.name}")
        return True
    else:
        print(f"⏭️  No changes needed for {file_path.name}")
        return False

def main():
    # Get all bracket HTML files except TableTennis_Singles (already fixed)
    bracket_files = [f for f in Path('.').glob('Bracket_*.html') 
                     if f.name != 'Bracket_TableTennis_Singles.html']
    
    if not bracket_files:
        print("❌ No bracket files found!")
        return
    
    print(f"Found {len(bracket_files)} bracket files to fix")
    print("=" * 60)
    
    updated_count = 0
    for file_path in sorted(bracket_files):
        if move_apply_edit_controls(file_path):
            updated_count += 1
    
    print("=" * 60)
    print(f"\n✅ Complete! Fixed {updated_count} files")
    print("\n📝 Changes made:")
    print("   ✅ Moved applyEditControls() outside Firebase block")
    print("   ✅ Function now accessible from renderBracket()")
    print("\n🐛 Bug Fixed:")
    print("   ❌ Before: 'applyEditControls is not defined' error")
    print("   ✅ After: Function accessible globally")

if __name__ == '__main__':
    main()

