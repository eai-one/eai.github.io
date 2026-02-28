"""
Weekly EAI blog post generator.
"""

import os
import subprocess
from datetime import datetime

TODAY = datetime.utcnow()
DATE_STR = TODAY.strftime("%Y-%m-%d")
DATE_LONG = TODAY.strftime("%B %d, %Y")
FILENAME = f"_posts/{DATE_STR}-eai-weekly.md"

PROMPT = f"""You are a technical writer for the EAI.1 Blog (eai.one), a blog about Embodied AI.

Blog posts use Jekyll with this exact frontmatter:
---
layout: post
title: "Title Here"
date: YYYY-MM-DD 00:00:00 +0900
comments: false
categories: embodied-ai <additional-relevant-categories>
---

Writing style guidelines:
- Use **bold** for key terms on first introduction
- Use numbered lists with 1️⃣ 2️⃣ 3️⃣ emoji for major sections
- Use ✅ or • for sub-points in bullet lists
- Clear, informative technical writing aimed at AI/robotics enthusiasts
- 400–600 words of body content (not counting frontmatter)
- Include: a one-paragraph intro, 2–4 key developments or concepts, and a brief forward-looking close
- Do NOT include any markdown headings (##) — use bold + numbered lists for structure instead
- Output ONLY the raw post content (frontmatter + body). No extra commentary.

---

Write a new blog post about recent developments in Embodied AI.
Today's date is {DATE_LONG}. Use {DATE_STR} in the frontmatter date field.

Pick one focused angle from the areas below — do not try to cover everything:
- Vision-Language-Action (VLA) models and robotic foundation models
- Humanoid robot deployments (Figure, 1X, Tesla Optimus, Unitree, Boston Dynamics, etc.)
- Sim-to-real transfer and robot learning techniques
- Tactile sensing, dexterity, and manipulation research
- Edge AI and on-device inference for robots
- Notable recent research papers or industry milestones

Choose a specific, descriptive title (not a generic "Weekly Update").
Pick 2–3 lowercase hyphenated category slugs after embodied-ai in the frontmatter.
Output the complete post, starting with the --- frontmatter block."""


def main():
    print(f"Generating post for {DATE_LONG}...")

    result = subprocess.run(
        ["claude", "-p", PROMPT],
        capture_output=True,
        text=True,
        check=True,
    )

    content = result.stdout.strip()

    if not content.startswith("---"):
        raise ValueError("Generated content does not start with frontmatter. Aborting.\n" + content[:200])

    os.makedirs("_posts", exist_ok=True)
    with open(FILENAME, "w", encoding="utf-8") as f:
        f.write(content + "\n")

    print(f"Saved: {FILENAME}")


if __name__ == "__main__":
    main()
