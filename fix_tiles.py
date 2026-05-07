import re

with open('/Users/castro/LP-dev/index.html', 'r') as f:
    html = f.read()

# We need to find the bounds of the coaching section
idx = html.find('id="coaching"')
end_idx = html.find('id="about"', idx)
section = html[idx:end_idx]

p1 = '<div style="padding: 24px 0;"><p style="font-family: \'Inter\', sans-serif; font-size: 15px; color: #555; line-height: 1.6;">Discover the root cause behind your fatigue, weight, and mood — and the natural path to all-day energy, a clear head, and a body that finally works with you.</p></div>'
p2 = '<div style="padding: 24px 0;"><p style="font-family: \'Inter\', sans-serif; font-size: 15px; color: #555; line-height: 1.6;">Advanced testing and biomarker analysis that goes beyond the standard bloodwork. We build a complete picture of what\'s driving your symptoms and map out a personalized plan — so nothing gets missed and nothing is guessed.</p></div>'
p3 = '<div style="padding: 24px 0;"><p style="font-family: \'Inter\', sans-serif; font-size: 15px; color: #555; line-height: 1.6;">Your body changes. Your plan does too. We review your data, track how you\'re feeling, and adjust as you progress — consistent support at every stage, not just at the start.</p></div>'

c1 = '>→ Book Your Free Call<'
c2 = '>→ Get Started<'
c3 = '>→ Learn More<'

# The paragraphs and CTAs are currently a mix of p1, p2, p3 and c1, c2, c3.
# Let's replace them systematically.
# We will split the section by titles.
# There are 9 cards total (3 variants).
# Since they are ordered Card1, Card1, Card1, Card2, Card2, Card2, Card3, Card3, Card3 in the DOM,
# we can just find the blocks starting from the title up to the end of the button container.

def fix_card(title, correct_p, correct_c, section):
    # Find all occurrences of the title
    parts = section.split(title)
    new_section = parts[0]
    for i in range(1, len(parts)):
        part = parts[i]
        
        # In this part, we need to replace the paragraph and the CTA.
        # The paragraph starts with <div style="padding: 24px 0;"> and ends with </div>
        # Actually it's safer to regex match the p1/p2/p3.
        part = part.replace(p1, correct_p)
        part = part.replace(p2, correct_p)
        part = part.replace(p3, correct_p)
        
        part = part.replace(c1, correct_c)
        part = part.replace(c2, correct_c)
        part = part.replace(c3, correct_c)
        
        new_section += title + part
    return new_section

section = fix_card('1. Clarity Call</h3>', p1, c1, section)
section = fix_card('2. Initial Wellness Review</h3>', p2, c2, section)
section = fix_card('3. Ongoing Care & Adaptation</h3>', p3, c3, section)

html = html[:idx] + section + html[end_idx:]

with open('/Users/castro/LP-dev/index.html', 'w') as f:
    f.write(html)
print("Tiles fixed successfully.")
