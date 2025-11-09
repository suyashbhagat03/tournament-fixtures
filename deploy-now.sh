#!/bin/bash

# 🚀 Simple Firebase Deploy Script
# Just run: ./deploy-now.sh

echo "🚀 Deploying Insportsathon to Firebase..."
echo ""

# Check if Firebase CLI is available
if ! command -v firebase &> /dev/null; then
    echo "❌ Firebase CLI not found!"
    echo "📦 Please install it first:"
    echo "   curl -sL https://firebase.tools | bash"
    exit 1
fi

# Deploy
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
    echo "📊 View console:"
    echo "   https://console.firebase.google.com/project/insportsathon/hosting"
    echo ""
    echo "🎉 Share with your team!"
else
    echo ""
    echo "❌ Deployment failed"
    echo ""
    echo "💡 First time? Run:"
    echo "   firebase login"
fi

