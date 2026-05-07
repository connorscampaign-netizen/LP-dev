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

with open('/Users/castro/LP-dev/index.html', 'r') as f:
    html = f.read()

idx = html.find('id="reviews"')
end_idx = html.find('id="faq"', idx)
if end_idx == -1: end_idx = len(html)
section = html[idx:end_idx]

original_quote = "After years of minimal labs and little explanation, this was the first time everything was laid out clearly. Genuinely life-changing."
original_author = "Hannah K. · Hashimoto's & Hormones"

# We have 3 occurrences of framer-95qcoa (for the 3 breakpoints)
def replace_container(match):
    block = match.group(0)
    new_blocks = []
    for r in reviews_data:
        new_block = block
        
        # Replace quote
        new_block = new_block.replace(original_quote, r['quote'])
        
        # Replace author
        author_str = f"{r['author']} · {r['category']}"
        new_block = new_block.replace(original_author, author_str)
        
        new_blocks.append(new_block)
    
    return "".join(new_blocks)

# Use regex to find and replace the 3 framer-95qcoa blocks
# Since it's a huge block, we'll find its boundaries explicitly
# Wait, let's just find the entire block string and do replace.
blocks = []
start = 0
while True:
    s_idx = section.find('<div class="framer-95qcoa"', start)
    if s_idx == -1: break
    
    # We know the block ends right before </div></div></section> OR </div></div></div>
    # Actually, the block is exactly what is matched by `<div class="framer-95qcoa"...` up to the end of its closing div.
    # We can use our earlier knowledge: the next block is either another ssr-variant or section end.
    # Let's count open/close divs.
    depth = 0
    e_idx = s_idx
    while e_idx < len(section):
        if section[e_idx:e_idx+4] == '<div':
            depth += 1
            e_idx += 4
        elif section[e_idx:e_idx+6] == '</div>':
            depth -= 1
            e_idx += 6
            if depth == 0:
                break
        else:
            e_idx += 1
            
    block = section[s_idx:e_idx]
    blocks.append(block)
    start = e_idx

print(f"Found {len(blocks)} blocks")

new_section = section
for block in set(blocks): # Use set in case they are identical
    new_blocks = []
    for r in reviews_data:
        new_block = block
        new_block = new_block.replace(original_quote, r['quote'])
        author_str = f"{r['author']} · {r['category']}"
        new_block = new_block.replace(original_author, author_str)
        new_blocks.append(new_block)
        
    combined_blocks = "".join(new_blocks)
    new_section = new_section.replace(block, combined_blocks)

html = html[:idx] + new_section + html[end_idx:]

with open('/Users/castro/LP-dev/index.html', 'w') as f:
    f.write(html)

print("Imported all 16 reviews")
