#!/usr/bin/env python3
"""
Add permission check to updateMatchTime in all brackets
"""

import os

BRACKET_FILES = [
    'Bracket_Snooker.html',
    'Bracket_FIFA25.html',
    'Bracket_Foosball.html',
    'Bracket_Carrom_Doubles.html',
    'Bracket_Carrom_Singles.html',
    'Bracket_TableTennis_Doubles.html',
    'Bracket_TableTennis_Singles.html'
]

OLD_CODE = """        window.updateMatchTime = function(roundIdx, matchIdx, value) {
            allRoundsData[roundIdx][matchIdx].time = value;
            saveToFirebase();
        };"""

NEW_CODE = """        window.updateMatchTime = function(roundIdx, matchIdx, value) {
            if (!isEditModeEnabled) return; // Check edit permission
            allRoundsData[roundIdx][matchIdx].time = value;
            saveToFirebase();
        };"""

def fix_bracket(filepath):
    print(f"Fixing: {os.path.basename(filepath)}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if OLD_CODE in content:
        content = content.replace(OLD_CODE, NEW_CODE)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✅ Added permission check to updateMatchTime\n")
    else:
        print(f"  ⚠️  Already fixed or pattern not found\n")

def main():
    base_path = '/Users/sbhagat/Insports'
    
    print("🔧 Adding permission check to updateMatchTime...\n")
    
    for filename in BRACKET_FILES:
        filepath = os.path.join(base_path, filename)
        if os.path.exists(filepath):
            try:
                fix_bracket(filepath)
            except Exception as e:
                print(f"  ❌ Error: {e}\n")
        else:
            print(f"❌ File not found: {filename}\n")
    
    print("✅ All brackets updated!")

if __name__ == '__main__':
    main()

