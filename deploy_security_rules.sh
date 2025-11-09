#!/bin/bash

echo "🔒 Deploying Firebase Security Rules..."
echo ""
echo "This will secure your Firebase Database with proper role-based access control."
echo ""

# Check if Firebase CLI is installed
if ! command -v firebase &> /dev/null; then
    echo "❌ Firebase CLI not found!"
    echo ""
    echo "Install it first:"
    echo "  npm install -g firebase-tools"
    echo ""
    exit 1
fi

# Check if logged in
echo "📋 Checking Firebase login status..."
firebase projects:list &> /dev/null
if [ $? -ne 0 ]; then
    echo "❌ Not logged in to Firebase!"
    echo ""
    echo "Login first:"
    echo "  firebase login"
    echo ""
    exit 1
fi

# Deploy rules
echo "🚀 Deploying database security rules..."
firebase deploy --only database --project insportsathon

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Security rules deployed successfully!"
    echo ""
    echo "🔒 Your database is now protected:"
    echo "   • Brackets: Public read, Editor/Admin write"
    echo "   • Contacts: Authenticated read, Admin write"
    echo "   • Users: Private read, Admin write"
    echo ""
else
    echo ""
    echo "❌ Deployment failed!"
    echo ""
    echo "Manual steps:"
    echo "1. Go to: https://console.firebase.google.com/"
    echo "2. Select: Insportsathon project"
    echo "3. Click: Realtime Database → Rules tab"
    echo "4. Copy contents from: database.rules.json"
    echo "5. Click: Publish"
    echo ""
fi

