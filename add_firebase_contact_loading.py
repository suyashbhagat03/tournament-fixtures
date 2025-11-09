#!/usr/bin/env python3
"""
Add Firebase contact loading code to all bracket files.
"""

import re
from pathlib import Path

def add_contact_loading(file_path):
    """Add Firebase contact loading function to bracket file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Find where to insert (after loadFromFirebase function, before selectWinner)
    # Look for the line with "// Initialize on load" or "loadFromFirebase();"
    pattern = r'(// Initialize on load\s+loadFromFirebase\(\);)'
    
    firebase_contact_code = r'''\1
        
        // Load contact information from Firebase
        function loadContactsFromFirebase() {
            if (!isFirebaseConfigured || !db) {
                // Use initial hardcoded contacts
                contactInfo = initialContactInfo;
                return;
            }
            
            const contactsRef = ref(db, `contacts/${SPORT_KEY}`);
            
            // Check if contacts exist in Firebase
            get(contactsRef).then((snapshot) => {
                if (snapshot.exists()) {
                    // Load from Firebase
                    contactInfo = snapshot.val();
                    console.log('✅ Contacts loaded from Firebase');
                } else {
                    // First time - upload initial contacts to Firebase
                    set(contactsRef, initialContactInfo).then(() => {
                        contactInfo = initialContactInfo;
                        console.log('✅ Initial contacts uploaded to Firebase');
                    }).catch((error) => {
                        console.error('Error uploading contacts:', error);
                        contactInfo = initialContactInfo;
                    });
                }
            }).catch((error) => {
                console.error('Error loading contacts:', error);
                contactInfo = initialContactInfo;
            });
        }
        
        // Load contacts on page load
        loadContactsFromFirebase();'''
    
    content = re.sub(pattern, firebase_contact_code, content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated {file_path.name}")
        return True
    else:
        print(f"⏭️  Pattern not found in {file_path.name}")
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
        if add_contact_loading(file_path):
            updated_count += 1
    
    print("=" * 60)
    print(f"\n✅ Complete! Updated {updated_count} files")

if __name__ == '__main__':
    main()
