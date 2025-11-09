#!/bin/bash

# 🚀 Quick Deploy Script for Insportsathon Brackets
# Run this script to deploy to Firebase Hosting

echo "=================================="
echo "🚀 Deploying Insportsathon Brackets"
echo "=================================="
echo ""

# Check if Firebase CLI is installed
if ! command -v firebase &> /dev/null
then
    echo "❌ Firebase CLI not found!"
    echo "📦 Installing Firebase CLI..."
    npm install -g firebase-tools
    if [ $? -ne 0 ]; then
        echo "❌ Installation failed. Install manually:"
        echo "   npm install -g firebase-tools"
        exit 1
    fi
fi

echo "✅ Firebase CLI found"
echo ""

# Check if logged in
echo "🔐 Checking Firebase login..."
firebase projects:list &> /dev/null
if [ $? -ne 0 ]; then
    echo "🔑 Please login to Firebase..."
    firebase login
    if [ $? -ne 0 ]; then
        echo "❌ Login failed"
        exit 1
    fi
fi

echo "✅ Logged in to Firebase"
echo ""

# Check if project is initialized
if [ ! -f "firebase.json" ]; then
    echo "⚙️  Initializing Firebase Hosting..."
    firebase init hosting --project insportsathon
    if [ $? -ne 0 ]; then
        echo "❌ Initialization failed"
        exit 1
    fi
fi

echo "✅ Project initialized"
echo ""

# Deploy
echo "🚀 Deploying to Firebase Hosting..."
firebase deploy --only hosting --project insportsathon

if [ $? -eq 0 ]; then
    echo ""
    echo "=================================="
    echo "✅ DEPLOYMENT SUCCESSFUL!"
    echo "=================================="
    echo ""
    echo "🌐 Your site is live at:"
    echo "   https://insportsathon.web.app"
    echo ""
    echo "📊 View in Firebase Console:"
    echo "   https://console.firebase.google.com/project/insportsathon/hosting"
    echo ""
    echo "🎉 Share with your team!"
    echo "=================================="
else
    echo ""
    echo "❌ Deployment failed"
    echo "See error messages above"
    exit 1
fi

