import re

with open('/Users/castro/LP-dev/index.html', 'r') as f:
    html = f.read()

idx = html.find('id="about"')
end_idx = html.find('id="faq"', idx)
if end_idx == -1: end_idx = len(html)
section = html[idx:end_idx]

p1_lead = "Live Wellness is a Florida-based functional medicine practice led by Dr. Adam Dombrowski and Dr. Krista Imre "
p1_sup = "— with 1,000+ members helped and a team devoted to one thing: finding the root cause and fixing it naturally."

p2_lead = "Unlike conventional care, every plan is built around your bloodwork, your symptoms, and your life "
p2_sup = "— with a team that stays by your side until you feel the difference."

p3_lead = "We help you reclaim your energy, balance your hormones, heal your gut, and feel like yourself again "
p3_sup = "— through advanced testing, personalized plans, and ongoing support every step of the way."

def format_p(lead, sup):
    return f'<strong>{lead.strip()}</strong> <span style="opacity: 0.75; font-weight: 400;">{sup.strip()}</span>'

# Find all paragraphs in the section
matches = list(re.finditer(r'(<p class="framer-text[^>]*>)(.*?)(</p>)', section))

if len(matches) >= 3:
    for i, match in reversed(list(enumerate(matches[:3]))):
        start = match.start(2)
        end = match.end(2)
        if i == 0:
            content = format_p(p1_lead, p1_sup)
        elif i == 1:
            content = format_p(p2_lead, p2_sup)
        elif i == 2:
            content = format_p(p3_lead, p3_sup)
        
        section = section[:start] + content + section[end:]

    html = html[:idx] + section + html[end_idx:]

    with open('/Users/castro/LP-dev/index.html', 'w') as f:
        f.write(html)
    print("Styled all 3 paragraphs successfully.")
else:
    print("Could not find 3 paragraphs!")

