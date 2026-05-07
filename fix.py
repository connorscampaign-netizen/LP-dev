import re

with open('/Users/castro/LP-dev/index.html', 'r') as f:
    html = f.read()

# 1. Fix the Hero H1
def create_spans(text):
    spans = []
    for char in text:
        if char == ' ':
            spans.append('<span style="display:inline-block;opacity:0.001;filter:blur(6px);transform:translateX(0px) translateY(0px) scale(1.4) rotate(0deg) skewX(0deg) skewY(0deg)">&nbsp;</span>')
        else:
            spans.append(f'<span style="display:inline-block;opacity:0.001;filter:blur(6px);transform:translateX(0px) translateY(0px) scale(1.4) rotate(0deg) skewX(0deg) skewY(0deg)">{char}</span>')
    return '<span style="white-space:nowrap">' + ''.join(spans) + '</span>'

new_hero_html = create_spans("Get to the Root Of Your Health")

# Find the H1 and replace its content
# The H1 starts with <h1 class="framer-text framer-styles-preset-bo0tsp" ...>
html = re.sub(
    r'(<h1 class="framer-text framer-styles-preset-bo0tsp"[^>]*>)(.*?)(</h1>)',
    lambda m: m.group(1) + new_hero_html + m.group(3),
    html,
    flags=re.DOTALL
)

# 2. Fix the missed About text B
html = re.sub(
    r'My coaching blends physical training and mental strategies,[^<]*helping athletes build strength and confidence to overcome their limits\.',
    'Where conventional medicine looks for disease and prescribes a pill, we look for dysfunction and restore balance.',
    html
)

# 3. Fix the missed About text C
html = re.sub(
    r'Turn every milestone into a victory through personalized coaching\.',
    'Our team of 5 practitioners works with members globally to uncover hidden triggers and create customized, data-driven protocols.',
    html
)

# 4. Remove Remix Badge
html = re.sub(r'<div id="__framer-badge-container">.*?</div>', '', html, flags=re.DOTALL)

# 5. Fix leftover "Perform" and "coaching" etc.
html = re.sub(r'<title>Perform — Design Reference[^<]*</title>', '<title>Live Wellness</title>', html)
html = html.replace('coaching plan you need', 'protocol you need')

# 6. Add CSS for animations
css_fixes = """
<style>
/* Hover on Header Links */
.framer-WMwAn a:hover .framer-text {
  color: var(--token-ad96cd96-c832-459f-bb48-2ba796f3179b) !important;
  opacity: 0.9 !important;
}

/* Hover on CTAs */
.framer-cd2Kv {
  transition: transform 0.3s ease, filter 0.3s ease, box-shadow 0.3s ease !important;
}
.framer-cd2Kv:hover {
  transform: translateY(-4px) !important;
  filter: brightness(1.1) !important;
  box-shadow: 0 8px 20px rgba(0,0,0,0.15) !important;
}

/* Spin arrow on CTA hover */
.framer-cd2Kv .framer-1qw1xy7, .framer-cd2Kv .framer-1ustco3 {
  transition: transform 0.4s ease-in-out !important;
}
.framer-cd2Kv:hover .framer-1qw1xy7, .framer-cd2Kv:hover .framer-1ustco3 {
  transform: rotate(360deg) scale(1.1) !important;
}

/* Ensure the hero text animation keyframes are there */
@keyframes heroTextReveal {
  from { opacity: 0; filter: blur(6px); transform: translateY(10px) scale(1.2); }
  to { opacity: 1; filter: blur(0px); transform: none; }
}

.hero-animated-text {
  animation: heroTextReveal 0.6s ease-out forwards;
}
</style>
"""
if "/* Hover on Header Links */" not in html:
    html = html.replace('</head>', css_fixes + '\n</head>')

with open('/Users/castro/LP-dev/index.html', 'w') as f:
    f.write(html)

print("Fixes applied successfully.")
