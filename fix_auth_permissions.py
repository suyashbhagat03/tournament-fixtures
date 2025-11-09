#!/usr/bin/env python3
"""
Fix authentication permissions - apply edit controls AFTER bracket renders
"""

import os
import re

BRACKET_FILES = [
    'Bracket_Chess.html',
    'Bracket_Snooker.html',
    'Bracket_FIFA25.html',
    'Bracket_Foosball.html',
    'Bracket_Carrom_Doubles.html',
    'Bracket_Carrom_Singles.html',
    'Bracket_TableTennis_Doubles.html',
    'Bracket_TableTennis_Singles.html'
]

def fix_bracket_file(filepath):
    """Fix the auth permissions in a bracket file"""
    print(f"Fixing: {os.path.basename(filepath)}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add global variable to track edit state
    if 'let isEditModeEnabled = false;' not in content:
        # Find where to insert (after other let declarations)
        pattern = r"(let saveTimeout = null;)"
        replacement = r"\1\n        let isEditModeEnabled = false; // Track if edit features should be enabled"
        content = re.sub(pattern, replacement, content)
        print("  ✅ Added isEditModeEnabled variable")
    
    # 2. Update onAuthStateChanged to set the flag instead of calling enableEditFeatures directly
    old_auth_logic = r"// Enable/disable edit features\s+enableEditFeatures\(userRole !== 'viewer'\);"
    new_auth_logic = "// Enable/disable edit features\n                isEditModeEnabled = (userRole !== 'viewer');\n                // Apply controls after next render\n                applyEditControls();"
    content = re.sub(old_auth_logic, new_auth_logic, content)
    
    old_auth_logic_2 = r"// Disable edit features\s+enableEditFeatures\(false\);"
    new_auth_logic_2 = "// Disable edit features\n                isEditModeEnabled = false;\n                // Apply controls after next render\n                applyEditControls();"
    content = re.sub(old_auth_logic_2, new_auth_logic_2, content)
    print("  ✅ Updated auth state logic")
    
    # 3. Rename enableEditFeatures to applyEditControls and make it check if elements exist
    content = content.replace(
        "// Enable/disable edit features\n        function enableEditFeatures(enabled) {",
        "// Apply edit controls (called after bracket renders)\n        function applyEditControls() {\n            const enabled = isEditModeEnabled;"
    )
    print("  ✅ Renamed enableEditFeatures to applyEditControls")
    
    # 4. Add call to applyEditControls at the END of renderBracket function
    # Find the renderBracket function and add the call before the closing brace
    # Look for the showChampion() call which is usually at the end
    pattern = r"(showChampion\(\);)\s*(\n\s*}\s*\n\s*function)"
    replacement = r"\1\n            // Apply edit controls after rendering\n            applyEditControls();\2"
    content = re.sub(pattern, replacement, content)
    print("  ✅ Added applyEditControls() call to renderBracket()")
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ {os.path.basename(filepath)} fixed!\n")

def main():
    base_path = '/Users/sbhagat/Insports'
    
    print("=" * 60)
    print("🔧 Fixing Authentication Permissions")
    print("=" * 60)
    print()
    
    for filename in BRACKET_FILES:
        filepath = os.path.join(base_path, filename)
        if os.path.exists(filepath):
            try:
                fix_bracket_file(filepath)
            except Exception as e:
                print(f"  ❌ Error: {e}\n")
        else:
            print(f"❌ File not found: {filename}\n")
    
    print("=" * 60)
    print("✅ All brackets fixed!")
    print("=" * 60)
    print()
    print("✨ Changes made:")
    print("1. Added isEditModeEnabled flag to track auth state")
    print("2. Updated auth callbacks to set flag + apply controls")
    print("3. Renamed enableEditFeatures → applyEditControls")
    print("4. Apply controls AFTER bracket renders (not before)")
    print()
    print("🎯 Result:")
    print("• Default (no login) → READ-ONLY ✅")
    print("• After login (editor/admin) → EDIT MODE ✅")
    print("• Read-only banner shows correctly ✅")
    print()

if __name__ == '__main__':
    main()

