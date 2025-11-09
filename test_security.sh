#!/bin/bash

echo "🔐 Testing Firebase Security"
echo "============================="
echo ""

echo "📋 This will test if your Firebase Security Rules are properly deployed."
echo ""

# Open Firebase Console
echo "1️⃣ Opening Firebase Console to check rules..."
open "https://console.firebase.google.com/project/insportsathon/database/insportsathon-default-rtdb/rules"

echo ""
echo "2️⃣ Check what you see in the browser:"
echo ""
echo "❌ BAD (Test Mode - INSECURE):"
echo "   {"
echo "     \"rules\": {"
echo "       \".read\": \"now < 1765045800000\","
echo "       \".write\": \"now < 1765045800000\""
echo "     }"
echo "   }"
echo ""
echo "✅ GOOD (Secure Rules):"
echo "   {"
echo "     \"rules\": {"
echo "       \"tournaments\": { ... },"
echo "       \"users\": { ... },"
echo "       \"contacts\": { ... }"
echo "     }"
echo "   }"
echo ""

read -p "Which one do you see? (bad/good): " response

if [ "$response" = "bad" ]; then
    echo ""
    echo "🚨 WARNING: Your database is in TEST MODE!"
    echo ""
    echo "Anyone can:"
    echo "  ❌ Read all data (including contacts, emails, phones)"
    echo "  ❌ Modify tournaments"
    echo "  ❌ Change user roles"
    echo "  ❌ Delete everything"
    echo ""
    echo "🔧 FIX NOW:"
    echo ""
    read -p "Deploy secure rules? (y/n): " deploy
    
    if [ "$deploy" = "y" ]; then
        echo ""
        echo "🚀 Deploying secure rules..."
        firebase deploy --only database --project insportsathon
        
        if [ $? -eq 0 ]; then
            echo ""
            echo "✅ Secure rules deployed!"
            echo ""
            echo "🧪 Test it:"
            echo "1. Open any bracket (not logged in)"
            echo "2. Open browser console (F12)"
            echo "3. Paste:"
            echo "   isEditModeEnabled = true;"
            echo "   import('https://www.gstatic.com/firebasejs/10.7.1/firebase-database.js').then(({getDatabase, ref, set}) => {"
            echo "     const db = getDatabase();"
            echo "     set(ref(db, 'tournaments/Chess/rounds/0/0/player1'), 'HACKED');"
            echo "   });"
            echo ""
            echo "4. You should see: PERMISSION_DENIED ✅"
        else
            echo ""
            echo "❌ Deployment failed!"
            echo ""
            echo "Manual steps:"
            echo "1. Copy contents from: database.rules.whitelist.json"
            echo "2. Paste in Firebase Console (already open)"
            echo "3. Click 'Publish'"
        fi
    else
        echo ""
        echo "⚠️  Your database is still INSECURE!"
        echo "   Deploy rules manually:"
        echo "   1. Copy: database.rules.whitelist.json"
        echo "   2. Paste in Firebase Console"
        echo "   3. Click 'Publish'"
    fi
elif [ "$response" = "good" ]; then
    echo ""
    echo "✅ Great! Secure rules are deployed."
    echo ""
    echo "🧪 Let's test if they work:"
    echo ""
    echo "Test 1: Console Bypass Attack (No Login)"
    echo "----------------------------------------"
    echo "1. Open any bracket (not logged in)"
    echo "2. Open browser console (F12)"
    echo "3. Paste this code:"
    echo ""
    echo "isEditModeEnabled = true;"
    echo "import('https://www.gstatic.com/firebasejs/10.7.1/firebase-database.js').then(({getDatabase, ref, set}) => {"
    echo "  const db = getDatabase();"
    echo "  set(ref(db, 'tournaments/Chess/rounds/0/0/player1'), 'HACKED').catch(err => console.log('✅ BLOCKED:', err.message));"
    echo "});"
    echo ""
    read -p "Press Enter after testing..."
    echo ""
    echo "Did you see 'PERMISSION_DENIED' error?"
    read -p "(y/n): " result1
    
    echo ""
    echo "Test 2: Viewer Role Bypass (Logged In)"
    echo "--------------------------------------"
    echo "1. Login as viewer"
    echo "2. In console, paste:"
    echo ""
    echo "userRole = 'admin';  // Try to fake admin role"
    echo "import('https://www.gstatic.com/firebasejs/10.7.1/firebase-database.js').then(({getDatabase, ref, set}) => {"
    echo "  const db = getDatabase();"
    echo "  set(ref(db, 'tournaments/Chess/rounds/0/0/player1'), 'HACKED').catch(err => console.log('✅ BLOCKED:', err.message));"
    echo "});"
    echo ""
    read -p "Press Enter after testing..."
    echo ""
    echo "Did you see 'PERMISSION_DENIED' error?"
    read -p "(y/n): " result2
    
    echo ""
    echo "📊 Security Test Results:"
    echo "========================="
    
    if [ "$result1" = "y" ] && [ "$result2" = "y" ]; then
        echo "✅ Test 1: PASSED (No login blocked)"
        echo "✅ Test 2: PASSED (Viewer blocked)"
        echo ""
        echo "🎉 Your Firebase Security is PROPERLY CONFIGURED!"
        echo ""
        echo "Summary:"
        echo "  ✅ Client-side checks can be bypassed (expected)"
        echo "  ✅ Firebase Rules block unauthorized writes (working!)"
        echo "  ✅ Roles are validated server-side (secure!)"
        echo ""
        echo "Your tournament system is secure! 🔒"
    else
        echo "⚠️ Test 1: ${result1/y/PASSED}"
        echo "⚠️ Test 2: ${result2/y/PASSED}"
        echo ""
        echo "Some tests failed. Check:"
        echo "1. Firebase Rules are deployed correctly"
        echo "2. Browser console for actual errors"
        echo "3. Firebase Console → Database → Rules tab"
    fi
else
    echo ""
    echo "Invalid response. Please run the script again."
fi

echo ""
echo "📖 For more info, see: CLIENT_VS_SERVER_SECURITY.md"

