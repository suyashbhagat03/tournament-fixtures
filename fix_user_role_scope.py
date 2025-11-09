#!/usr/bin/env python3
"""
Move userRole and currentUser outside Firebase block for global access.
"""

import re
from pathlib import Path

def fix_user_role_scope(file_path):
    """Move userRole and currentUser declarations outside Firebase block."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern to find the auth variables inside Firebase block
    pattern = r'''(// Initialize Firebase
\s*let db = null;
\s*let dataRef = null;
\s*
\s*if \(isFirebaseConfigured\) \{
\s*try \{
\s*const app = initializeApp\(firebaseConfig\);
\s*db = getDatabase\(app\);
\s*dataRef = ref\(db, `tournaments/[^`]+`\);
\s*
\s*// ========================================
\s*// AUTHENTICATION & ACCESS CONTROL
\s*// ========================================
\s*const auth = getAuth\(app\);
\s*let currentUser = null;
\s*let userRole = 'viewer'; // default: read-only)'''
    
    def replace_func(match):
        # Extract the tournament name from the match
        tournament_match = re.search(r'ref\(db, `tournaments/([^`]+)`\)', match.group(0))
        tournament_name = tournament_match.group(1) if tournament_match else 'Unknown'
        
        return f'''// Initialize Firebase
        let db = null;
        let dataRef = null;
        
        // Auth variables (outside Firebase block for global access)
        let currentUser = null;
        let userRole = 'viewer'; // default: read-only
        
        if (isFirebaseConfigured) {{
            try {{
                const app = initializeApp(firebaseConfig);
                db = getDatabase(app);
                dataRef = ref(db, `tournaments/{tournament_name}`);
        
        // ========================================
        // AUTHENTICATION & ACCESS CONTROL
        // ========================================
        const auth = getAuth(app);'''
    
    content = re.sub(pattern, replace_func, content, flags=re.MULTILINE)
    
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
        if fix_user_role_scope(file_path):
            updated_count += 1
    
    print("=" * 60)
    print(f"\n✅ Complete! Fixed {updated_count} files")
    print("\n📝 Changes made:")
    print("   ✅ Moved currentUser outside Firebase block")
    print("   ✅ Moved userRole outside Firebase block")
    print("   ✅ Variables now accessible in applyEditControls()")
    print("\n🐛 Bug Fixed:")
    print("   ❌ Before: 'userRole is not defined' error")
    print("   ✅ After: userRole accessible globally")

if __name__ == '__main__':
    main()

