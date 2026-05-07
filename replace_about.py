import re

with open('/Users/castro/LP-dev/index.html', 'r') as f:
    html = f.read()

idx = html.find('id="about"')
end_idx = html.find('id="faq"', idx)
if end_idx == -1: end_idx = len(html)
section = html[idx:end_idx]

p1 = "Live Wellness is a Florida-based functional medicine practice led by Dr. Adam Dombrowski and Dr. Krista Imre — with 1,000+ members helped and a team devoted to one thing: finding the root cause and fixing it naturally."
p2 = "Unlike conventional care, every plan is built around your bloodwork, your symptoms, and your life — with a team that stays by your side until you feel the difference."
p3 = "We help you reclaim your energy, balance your hormones, heal your gut, and feel like yourself again — through advanced testing, personalized plans, and ongoing support every step of the way."

# Find all paragraphs in the section
# We will use re.finditer to get their spans
matches = list(re.finditer(r'(<p class="framer-text[^>]*>)(.*?)(</p>)', section))

if len(matches) >= 3:
    # We replace the content of the first 3 matches
    # Since we are replacing, we process from right to left to not mess up indices
    for i, match in reversed(list(enumerate(matches[:3]))):
        start = match.start(2)
        end = match.end(2)
        if i == 0:
            content = p1
        elif i == 1:
            content = p2
        elif i == 2:
            content = p3
        
        section = section[:start] + content + section[end:]

    html = html[:idx] + section + html[end_idx:]

    with open('/Users/castro/LP-dev/index.html', 'w') as f:
        f.write(html)
    print("Replaced all 3 paragraphs successfully.")
else:
    print("Could not find 3 paragraphs!")

