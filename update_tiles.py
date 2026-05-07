import sys
import re

with open('/Users/castro/LP-dev/index.html', 'r') as f:
    html = f.read()

idx = html.find('id="coaching"')
end_idx = html.find('id="about"', idx)

if idx == -1 or end_idx == -1:
    print("Could not find coaching section bounds")
    sys.exit(1)

section = html[idx:end_idx]

# 1. Add subtitle to "How It Works"
section = section.replace(
    '<h2 class="framer-text framer-styles-preset-skc7t7" data-styles-preset="R1WMv4dLC">How It Works</h2></div>',
    '<h2 class="framer-text framer-styles-preset-skc7t7" data-styles-preset="R1WMv4dLC">How It Works</h2></div><div style="margin-top: 16px; margin-bottom: 48px; text-align: center; width: 100%; max-width: 800px; margin-left: auto; margin-right: auto;"><p style="font-family: \'Inter\', sans-serif; font-size: 18px; color: #555; line-height: 1.6;">No guesswork, no pressure, and no one-size-fits-all plans. Just a clear, structured process — built around you.</p></div>'
)

# 2. Remove $59/month
section = section.replace('>$59/month<', '><')

# 3. Replace Titles and Subtitles
section = section.replace(
    'Basic</h3>',
    '1. Clarity Call</h3><p style="font-size: 14px; font-weight: 600; color: #7a9e7e; margin-top: 8px;">Free · 15 Minutes</p>'
)
section = section.replace(
    'Standard</h3>',
    '2. Initial Wellness Review</h3><p style="font-size: 14px; font-weight: 600; color: #7a9e7e; margin-top: 8px;">Your Foundation</p>'
)
section = section.replace(
    'Premium</h3>',
    '3. Ongoing Care & Adaptation</h3><p style="font-size: 14px; font-weight: 600; color: #7a9e7e; margin-top: 8px;">You\'re Never Left to Figure It Out Alone</p>'
)

# 4. Replace the Features blocks sequentially
paras = [
    '<div style="padding: 24px 0;"><p style="font-family: \'Inter\', sans-serif; font-size: 15px; color: #555; line-height: 1.6;">Discover the root cause behind your fatigue, weight, and mood — and the natural path to all-day energy, a clear head, and a body that finally works with you.</p></div>',
    '<div style="padding: 24px 0;"><p style="font-family: \'Inter\', sans-serif; font-size: 15px; color: #555; line-height: 1.6;">Advanced testing and biomarker analysis that goes beyond the standard bloodwork. We build a complete picture of what\'s driving your symptoms and map out a personalized plan — so nothing gets missed and nothing is guessed.</p></div>',
    '<div style="padding: 24px 0;"><p style="font-family: \'Inter\', sans-serif; font-size: 15px; color: #555; line-height: 1.6;">Your body changes. Your plan does too. We review your data, track how you\'re feeling, and adjust as you progress — consistent support at every stage, not just at the start.</p></div>'
]

features_pattern = r'<div class="framer-1u4zatd" data-framer-name="Features">.*?<div class="framer-1az1nvs-container"'
def features_repl(m):
    # This function is called for every match. We use a global counter to cycle through paragraphs.
    global feat_idx
    p = paras[feat_idx % 3]
    feat_idx += 1
    return p + '<div class="framer-1az1nvs-container"'

feat_idx = 0
section = re.sub(features_pattern, features_repl, section, flags=re.DOTALL)

# 5. Replace the CTA text sequentially
ctas = [
    '→ Book Your Free Call',
    '→ Get Started',
    '→ Learn More'
]

def cta_repl(m):
    global cta_idx
    c = ctas[cta_idx % 3]
    cta_idx += 1
    return '>{}<'.format(c)

cta_idx = 0
section = re.sub(r'>Get in touch<', cta_repl, section)

html = html[:idx] + section + html[end_idx:]

with open('/Users/castro/LP-dev/index.html', 'w') as f:
    f.write(html)

print("Tiles updated successfully.")
