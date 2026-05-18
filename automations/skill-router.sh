#!/usr/bin/env bash
# Reads prompt from stdin JSON, matches keywords, injects the right SKILL.md as context.

REPO="$(cd "$(dirname "$0")/.." && pwd)"
PROMPT=$(jq -r '.prompt // ""' 2>/dev/null)

# Lowercase for matching
LOWER=$(echo "$PROMPT" | tr '[:upper:]' '[:lower:]')

# Keyword sets (customize to your vocabulary)
CONTENT_KEYWORDS="content script scripts hook hooks caption captions pillar pillars post posting idea ideas weekly log video tiktok instagram reel"
BUSINESS_KEYWORDS="offer offers consulting client clients funnel revenue pricing package packages business deal sale sales"
PRODUCT_KEYWORDS="build building app product products backlog feature features code deploy launch saas tool"

match() {
  local text="$1"
  shift
  for word in "$@"; do
    if echo "$text" | grep -qw "$word"; then
      return 0
    fi
  done
  return 1
}

SKILL_FILE=""

if match "$LOWER" $CONTENT_KEYWORDS; then
  SKILL_FILE="$REPO/content/SKILL.md"
elif match "$LOWER" $BUSINESS_KEYWORDS; then
  SKILL_FILE="$REPO/business/SKILL.md"
elif match "$LOWER" $PRODUCT_KEYWORDS; then
  SKILL_FILE="$REPO/products/SKILL.md"
fi

if [ -n "$SKILL_FILE" ] && [ -f "$SKILL_FILE" ]; then
  SKILL_CONTENT=$(cat "$SKILL_FILE")
  jq -n --arg content "$SKILL_CONTENT" --arg file "$SKILL_FILE" \
    '{hookSpecificOutput: {hookEventName: "UserPromptSubmit", additionalContext: ("Loaded skill context from \($file):\n\n" + $content)}}'
fi
