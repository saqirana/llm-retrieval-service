#!/bin/bash

# GitHub Push Helper Script
# This script helps you push your code to GitHub

set -e

echo "🚀 GitHub Push Helper for LLM Retrieval Service"
echo "================================================"
echo ""

# Check if git remote exists
if git remote | grep -q "origin"; then
    echo "✓ Git remote 'origin' already exists:"
    git remote -v
    echo ""
    read -p "Do you want to update the remote URL? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git remote set-url origin https://github.com/saqirana/llm-retrieval-service.git
        echo "✓ Remote URL updated"
    fi
else
    echo "Adding GitHub remote..."
    git remote add origin https://github.com/saqirana/llm-retrieval-service.git
    echo "✓ Remote added successfully"
fi

echo ""
echo "Current branch:"
git branch --show-current
echo ""

echo "Checking repository status..."
if git diff-index --quiet HEAD --; then
    echo "✓ No uncommitted changes"
else
    echo "⚠️  You have uncommitted changes:"
    git status --short
    echo ""
    read -p "Do you want to commit these changes? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        read -p "Enter commit message: " commit_msg
        git add .
        git commit -m "$commit_msg"
        echo "✓ Changes committed"
    fi
fi

echo ""
echo "Ready to push to GitHub!"
echo "Repository: https://github.com/saqirana/llm-retrieval-service.git"
echo ""
read -p "Do you want to push now? (y/n) " -n 1 -r
echo

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "Pushing to GitHub..."

    # Check if this is the first push
    if git ls-remote --exit-code origin &>/dev/null; then
        echo "Remote repository exists, pushing..."
        git push origin main
    else
        echo "First push - setting upstream..."
        git push -u origin main
    fi

    echo ""
    echo "✅ Successfully pushed to GitHub!"
    echo ""
    echo "🎉 Your repository is now live at:"
    echo "   https://github.com/saqirana/llm-retrieval-service"
    echo ""
    echo "Next steps:"
    echo "1. Visit your repository on GitHub"
    echo "2. Add a description and topics"
    echo "3. Set up GitHub Actions secrets for CI/CD"
    echo "4. Create your first release (optional)"
    echo ""
    echo "To create a release:"
    echo "  git tag -a v1.0.0 -m 'Release v1.0.0: Initial production release'"
    echo "  git push origin v1.0.0"
    echo ""
else
    echo ""
    echo "Push cancelled. When you're ready, run:"
    echo "  git push -u origin main"
    echo ""
fi

echo "📖 For more information, see GITHUB_SETUP.md"

