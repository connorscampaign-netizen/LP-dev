import re

reviews_data = [
    {
        "category": "Gut & GI Issues",
        "quote": "After doing the detailed bloodwork, things finally made more sense. I felt lighter, less bloated, and much sharper. A 95% improvement in my health.",
        "author": "Kelly F."
    },
    {
        "category": "Hashimoto's, Hormones & Brain Fog",
        "quote": "After years of seeing doctors who ran minimal labs and gave little explanation, this was the first time everything was laid out clearly. Genuinely life-changing.",
        "author": "Hannah K."
    },
    {
        "category": "Weight, Joint Pain & Brain Fog",
        "quote": "I've lost 30 pounds and feel like I've come to a much better place. I no longer feel foggy, forgetful, or like I'm in a slump.",
        "author": "Kerry M."
    },
    {
        "category": "Postpartum Depletion & Hormones",
        "quote": "I feel healthier, stronger, and more like myself again. The care felt genuine, thorough, and rooted in true wellness — not quick fixes.",
        "author": "Kimberley B."
    },
    {
        "category": "Gut Issues & Hormone Imbalances — 7 Years",
        "quote": "For over seven years I struggled, knowing something was wrong but never finding the right plan. They gave me back my time and freedom — and a map for a hopeful future.",
        "author": "MnS H."
    },
    {
        "category": "Fatigue & Low Mood",
        "quote": "Before this program, all I ever knew was exhaustion, moodiness, and low energy. The protocol they developed has helped me create a lifestyle shift I'll carry with me forever.",
        "author": "Paulina"
    },
    {
        "category": "Sleep, Energy & Stubborn Weight",
        "quote": "I finally began sleeping soundly, my energy improved dramatically, and I lost 12 pounds. This program has truly transformed my overall health.",
        "author": "Chantel"
    },
    {
        "category": "Depression, Weight Gain & No Energy",
        "quote": "Within one week I felt energy I never felt before. I feel I have control over my life again — and I couldn't say that before I started.",
        "author": "Stephanie J."
    },
    {
        "category": "Bloating, Hormones & Weight",
        "quote": "I feel amazing, I dropped weight, I'm no longer bloated, my hormones are great and I have energy. I'll be 55 soon and I am THRIVING.",
        "author": "Allyson L."
    },
    {
        "category": "Digestive Issues, Lactose Intolerance & Fatigue",
        "quote": "I lost 10 pounds in the first six weeks and my energy completely came back. I'd been so fatigued I had forgotten how good it feels to have normal energy.",
        "author": "Josh P."
    },
    {
        "category": "Hormones, Hair Loss & Menopause",
        "quote": "My hair stopped coming out in clumps. I got my sense of smell back. I had energy and woke up ready for the day — for the first time in years.",
        "author": "Karen C."
    },
    {
        "category": "Joint Pain, Inflammation & Sleep",
        "quote": "The pain in my hands reduced by over 70%. I haven't taken blood pressure medication in eight weeks. This is the best investment I could have made in my health.",
        "author": "Oldy O."
    },
    {
        "category": "Autoimmune, Thyroid & Gut Health",
        "quote": "None of my endocrinologists ever discussed leaky gut or the connection to my thyroid. I've lost 25 pounds, eliminated joint pain, and finally feel healthy.",
        "author": "Lisa F."
    },
    {
        "category": "Chronic Hives, Anxiety & Exhaustion",
        "quote": "Three weeks in, my chronic hives stopped — after three years. I wasn't bloated, I wasn't tired. Things changed in less than two months, after years of feeling defeated.",
        "author": "Brittany C."
    },
    {
        "category": "Acid Reflux, Gut Pain & Low Energy",
        "quote": "Before I struggled with constipation, diarrhea, and severe acid reflux. Now I have more energy, sleep better, and no leg aches. This transformed my daily life.",
        "author": "Susan P."
    },
    {
        "category": "Acid Reflux, Cholesterol & Fatigue",
        "quote": "The biggest win is that I no longer need my acid reflux medication. I feel better, I understand my body more clearly, and I finally have a plan I can stick with.",
        "author": "Kathy F."
    }
]

template = """<div class="framer-1ifa1g" data-framer-name="Testimonial"><div class="framer-1x4g0g6" data-framer-name="Body"><div data-framer-component-type="SVG" data-framer-name="Stars Vector" style="image-rendering:pixelated;flex-shrink:0" class="framer-mrj9wp" aria-hidden="true"><div class="svgContainer" style="width:100%;height:100%;aspect-ratio:inherit"><svg style="width:100%;height:100%;"><use href="#svg12214099448"/></svg></div></div><div style="margin-top:-8px; margin-bottom:-8px;"><p style="font-family:'Inter', sans-serif; font-size:16px; font-weight:600; color:#7a9e7e; text-align:center;">{category}</p></div><div class="framer-nkurqb" data-framer-name="Testimonial Text" style="--framer-link-text-color:rgb(122, 158, 126);--framer-link-text-decoration:underline;transform:none" data-framer-component-type="RichTextContainer"><p class="framer-text framer-styles-preset-pbqkq1" data-styles-preset="WJJyCc90q" style="--framer-text-alignment:center">{quote}</p></div></div><div class="framer-e02ltn" data-framer-name="Author" style="--extracted-r6o4lv:var(--token-1b7bb1c4-3a89-4ec2-aee2-16abaf604d08, rgb(0, 0, 0));--framer-link-text-color:rgb(122, 158, 126);--framer-link-text-decoration:underline;transform:none" data-framer-component-type="RichTextContainer"><p class="framer-text framer-styles-preset-1yhjbal" data-styles-preset="Iz6fkU9FB" style="--framer-text-alignment:center;--framer-text-color:var(--extracted-r6o4lv, var(--token-1b7bb1c4-3a89-4ec2-aee2-16abaf604d08, rgb(0, 0, 0)))">{author}</p></div></div>"""

generated_nodes = []
for r in reviews_data:
    node = template.replace('{quote}', r['quote']).replace('{author}', r['author']).replace('{category}', r['category'])
    generated_nodes.append(node)

with open('/Users/castro/LP-dev/pristine_authors.txt', 'r') as f:
    pristine_authors = f.read()

master_container = '<div class="framer-95qcoa" data-framer-name="Testimonials">' + "".join(generated_nodes) + pristine_authors + '</div>'

with open('/Users/castro/LP-dev/index.html', 'r') as f:
    html = f.read()

idx = html.find('id="reviews"')
end_idx = html.find('id="faq"', idx)
if end_idx == -1: end_idx = len(html)
section = html[idx:end_idx]

start_idx = 0
while True:
    m_idx = section.find('<div class="framer-1grwh1j" data-framer-name="Container">', start_idx)
    if m_idx == -1: break
    
    inner_start = section.find('<div class="framer-95qcoa"', m_idx)
    
    # We must find the EXACT end of the framer-1grwh1j container, which is right before the NEXT ssr-variant or section end
    depth = 0
    e_idx = inner_start
    while e_idx < len(section):
        if section[e_idx:e_idx+4] == '<div':
            depth += 1
            e_idx += 4
        elif section[e_idx:e_idx+6] == '</div>':
            depth -= 1
            e_idx += 6
            if depth == 0:
                # We have found the end of the last block inside framer-1grwh1j. Wait! No!
                # If we start from inner_start (which is <div class="framer-95qcoa"), when depth == 0, we found the end of framer-95qcoa!
                # But wait, there are MULTIPLE framer-95qcoa inside framer-1grwh1j right now because my previous script injected 16 of them!
                # So finding depth == 0 will only skip ONE framer-95qcoa!
                pass
        else:
            e_idx += 1
            
# A better way to find the bounds is: we know framer-1grwh1j ends with </div></div></div> (or similar) before the next <div class="ssr-variant"
# Let's find the next <div class="ssr-variant" or the end of the section
    next_ssr = section.find('<div class="ssr-variant"', inner_start)
    if next_ssr == -1:
        # Last variant in the section
        end_of_container = section.rfind('</div></section>', inner_start)
        if end_of_container == -1: end_of_container = len(section)
        # But wait, framer-1grwh1j is wrapped in an ssr-variant, then <section>, then <div>, etc.
        # Just find the last </div> before next_ssr
    
    if next_ssr != -1:
        end_of_content = section.rfind('</div>', inner_start, next_ssr)
        # Actually, framer-1grwh1j is wrapped in:
        # <div class="ssr-variant ..."><section ...><div class="framer-1grwh1j">
        # So right before next_ssr, we have </div></section></div>
        # So the content inside framer-1grwh1j ends exactly at </div></div></section></div> or similar
        pass

# Since regex is risky with so much HTML, let's just use re.sub with DOTALL to replace EVERYTHING between <div class="framer-1grwh1j" data-framer-name="Container"> and the next </div></section>
# Wait, framer-1grwh1j is inside <section>. The section ends with </section>.
# So the content of framer-1grwh1j ends right before </section>.
# Let's see: <div class="framer-1grwh1j"> CONTENT </div></section>
# Therefore, CONTENT is what we want to replace.
    break

# New approach for safe replacement:
# The section has 3 occurrences of `<div class="framer-1grwh1j" data-framer-name="Container">`
# And 3 occurrences of `</section>`
# For each occurrence, we replace everything between them with our `master_container` + `</div>` (to close framer-1grwh1j)
pattern = r'(<div class="framer-1grwh1j" data-framer-name="Container">)(.*?)(</div></section>)'
def repl(m):
    return m.group(1) + master_container + m.group(3)

section = re.sub(pattern, repl, section, flags=re.DOTALL)

html = html[:idx] + section + html[end_idx:]

with open('/Users/castro/LP-dev/index.html', 'w') as f:
    f.write(html)

print("Marquee fixed properly!")
