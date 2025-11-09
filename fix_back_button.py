#!/usr/bin/env python3
"""
Fix back button being disabled for read-only users.
Only the reset button should be disabled, not back or print buttons.
"""

import re
from pathlib import Path

def fix_back_button(file_path):
    """Fix applyEditControls to only disable reset button, not back/print."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern to find the reset button disable logic
    old_pattern = r'''// Disable/enable reset button\s*
\s*const resetBtn = document\.querySelector\('\.controls button'\);\s*
\s*if \(resetBtn\) \{\s*
\s*resetBtn\.disabled = !enabled;\s*
\s*resetBtn\.style\.opacity = enabled \? '1' : '0\.5';\s*
\s*resetBtn\.style\.cursor = enabled \? 'pointer' : 'not-allowed';\s*
\s*\}\s*
\s*\}'''
    
    new_code = '''// Disable/enable reset button (but NOT back/print buttons)
            document.querySelectorAll('.controls button').forEach(btn => {
                // Only disable reset button, not back or print buttons
                if (btn.textContent.includes('Reset') || btn.textContent.includes('🗑️')) {
                    btn.disabled = !enabled;
                    btn.style.opacity = enabled ? '1' : '0.5';
                    btn.style.cursor = enabled ? 'pointer' : 'not-allowed';
                }
            });
        }'''
    
    content = re.sub(old_pattern, new_code, content, flags=re.MULTILINE)
    
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
        if fix_back_button(file_path):
            updated_count += 1
    
    print("=" * 60)
    print(f"\n✅ Complete! Fixed {updated_count} files")
    print("\n📝 Changes made:")
    print("   ✅ Back button is now always enabled")
    print("   ✅ Print button is now always enabled")
    print("   ❌ Only Reset button is disabled for read-only users")
    print("\n🔐 Button Access:")
    print("   ⬅️ Back button → ALWAYS ENABLED (all users)")
    print("   🖨️ Print button → ALWAYS ENABLED (all users)")
    print("   🗑️ Reset button → DISABLED for read-only users")

if __name__ == '__main__':
    main()

