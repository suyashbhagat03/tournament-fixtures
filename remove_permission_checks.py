#!/usr/bin/env python3
"""
Remove permission checks from edit functions to allow non-logged in users to edit.
"""

import re
from pathlib import Path

def remove_permission_checks(file_path):
    """Remove permission checks from all edit functions."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Functions that should have their permission checks removed
    functions_to_fix = [
        'selectWinner',
        'updateScore',
        'updateMatchTime',
        'startEditName',
        'saveName',
        'resetBracket',
        'showContactTooltip'
    ]
    
    for func_name in functions_to_fix:
        # Pattern: function funcName(...) { if (!isEditModeEnabled) return;
        pattern = rf'(function {func_name}\([^)]*\)\s*{{)\s*if\s*\(\s*!isEditModeEnabled\s*\)\s*return;?\s*'
        replacement = r'\1'
        content = re.sub(pattern, replacement, content)
        
        # Pattern: window.funcName = function(...) { if (!isEditModeEnabled) return;
        pattern = rf'(window\.{func_name}\s*=\s*function\([^)]*\)\s*{{)\s*if\s*\(\s*!isEditModeEnabled\s*\)\s*return;?\s*'
        replacement = r'\1'
        content = re.sub(pattern, replacement, content)
        
        # Pattern: const funcName = (...) => { if (!isEditModeEnabled) return;
        pattern = rf'(const {func_name}\s*=\s*\([^)]*\)\s*=>\s*{{)\s*if\s*\(\s*!isEditModeEnabled\s*\)\s*return;?\s*'
        replacement = r'\1'
        content = re.sub(pattern, replacement, content)
    
    # Also remove calls to applyEditControls()
    content = re.sub(r'\s*applyEditControls\(\);\s*', '', content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated {file_path.name}")
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
        if remove_permission_checks(file_path):
            updated_count += 1
    
    print("=" * 60)
    print(f"\n✅ Complete! Updated {updated_count} files")
    print("\n📝 Changes made:")
    print("   - Removed permission checks from edit functions")
    print("   - Removed applyEditControls() calls")
    print("   - Non-logged in users now have full edit access")

if __name__ == '__main__':
    main()

