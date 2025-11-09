#!/bin/bash

# Start local web server for Insportsathon
echo "🚀 Starting local web server..."
echo "📂 Serving from: $(pwd)"
echo ""
echo "✅ Server running at: http://localhost:8000"
echo ""
echo "📋 Quick Links:"
echo "   • Main Dashboard:      http://localhost:8000/index.html"
echo "   • Import Contacts:     http://localhost:8000/import_contacts_initial.html"
echo "   • Contact Management:  http://localhost:8000/contact_management.html"
echo "   • User Management:     http://localhost:8000/user_management.html"
echo ""
echo "⏹  Press Ctrl+C to stop the server"
echo ""

# Start Python HTTP server
python3 -m http.server 8000

