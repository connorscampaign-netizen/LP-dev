import re

with open('/Users/castro/LP-dev/index.html', 'r') as f:
    html = f.read()

idx = html.find('id="coaching"')
end_idx = html.find('id="about"', idx)

if idx == -1 or end_idx == -1:
    print("Could not find section")
    exit(1)

section = html[idx:end_idx]

# Replace Card 1
section = section.replace('></p></div><div class="framer-11cs0wh" data-framer-name="Title" style="--framer-link-text-color:rgb(122, 158, 126);--framer-link-text-decoration:underline;transform:none" data-framer-component-type="RichTextContainer"><h3 class="framer-text framer-styles-preset-pbqkq1" data-styles-preset="WJJyCc90q">1. Clarity Call</h3>', '>1</p></div><div class="framer-11cs0wh" data-framer-name="Title" style="--framer-link-text-color:rgb(122, 158, 126);--framer-link-text-decoration:underline;transform:none" data-framer-component-type="RichTextContainer"><h3 class="framer-text framer-styles-preset-pbqkq1" data-styles-preset="WJJyCc90q">Clarity Call</h3>')

# Replace Card 2
section = section.replace('>nth</p></div><div class="framer-11cs0wh" data-framer-name="Title" style="--framer-link-text-color:rgb(122, 158, 126);--framer-link-text-decoration:underline;transform:none" data-framer-component-type="RichTextContainer"><h3 class="framer-text framer-styles-preset-pbqkq1" data-styles-preset="WJJyCc90q">2. Initial Wellness Review</h3>', '>2</p></div><div class="framer-11cs0wh" data-framer-name="Title" style="--framer-link-text-color:rgb(122, 158, 126);--framer-link-text-decoration:underline;transform:none" data-framer-component-type="RichTextContainer"><h3 class="framer-text framer-styles-preset-pbqkq1" data-styles-preset="WJJyCc90q">Initial Wellness Review</h3>')

# Replace Card 3
section = section.replace('>$169/month</p></div><div class="framer-11cs0wh" data-framer-name="Title" style="--framer-link-text-color:rgb(122, 158, 126);--framer-link-text-decoration:underline;transform:none" data-framer-component-type="RichTextContainer"><h3 class="framer-text framer-styles-preset-pbqkq1" data-styles-preset="WJJyCc90q">3. Ongoing Care & Adaptation</h3>', '>3</p></div><div class="framer-11cs0wh" data-framer-name="Title" style="--framer-link-text-color:rgb(122, 158, 126);--framer-link-text-decoration:underline;transform:none" data-framer-component-type="RichTextContainer"><h3 class="framer-text framer-styles-preset-pbqkq1" data-styles-preset="WJJyCc90q">Ongoing Care & Adaptation</h3>')

# Update Card 3 CTA
# To make sure we only update Card 3's CTA, we can just replace '>→ Learn More<' with '>→ Start Here<'
section = section.replace('>→ Learn More<', '>→ Start Here<')

html = html[:idx] + section + html[end_idx:]

with open('/Users/castro/LP-dev/index.html', 'w') as f:
    f.write(html)

print("Updates applied.")
