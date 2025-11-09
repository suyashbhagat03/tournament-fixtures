#!/usr/bin/env python3
"""
Add applyEditControls() call to the end of renderBracket function
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

def fix_bracket(filepath):
    print(f"Fixing: {os.path.basename(filepath)}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to find the end of renderBracket function
    old_code = """            const finalMatch = allRoundsData[totalRounds - 1]?.[0];
            if (finalMatch?.winner) {
                document.getElementById('champion-name').textContent = finalMatch.winner;
                document.getElementById('final-score').textContent = finalMatch.score1 && finalMatch.score2 ? `${finalMatch.score1} - ${finalMatch.score2}` : '';
                document.getElementById('final-section').classList.add('show');
            } else {
                document.getElementById('final-section').classList.remove('show');
            }
        }"""
    
    new_code = """            const finalMatch = allRoundsData[totalRounds - 1]?.[0];
            if (finalMatch?.winner) {
                document.getElementById('champion-name').textContent = finalMatch.winner;
                document.getElementById('final-score').textContent = finalMatch.score1 && finalMatch.score2 ? `${finalMatch.score1} - ${finalMatch.score2}` : '';
                document.getElementById('final-section').classList.add('show');
            } else {
                document.getElementById('final-section').classList.remove('show');
            }
            // Apply edit controls after rendering
            applyEditControls();
        }"""
    
    if old_code in content:
        content = content.replace(old_code, new_code)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✅ Fixed!\n")
    else:
        print(f"  ⚠️  Pattern not found or already fixed\n")

def main():
    base_path = '/Users/sbhagat/Insports'
    
    print("🔧 Adding applyEditControls() calls to renderBracket...\n")
    
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

