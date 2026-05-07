import re

with open('/Users/castro/LP-dev/index.html', 'r') as f:
    html = f.read()

idx = html.find('id="coaching"')
end_idx = html.find('id="about"', idx)

if idx == -1 or end_idx == -1:
    print("Could not find section")
    exit(1)

section = html[idx:end_idx]

# Add period to the numbers
section = section.replace('>1</p></div><div class="framer-11cs0wh" data-framer-name="Title"', '>1.</p></div><div class="framer-11cs0wh" data-framer-name="Title"')
section = section.replace('>2</p></div><div class="framer-11cs0wh" data-framer-name="Title"', '>2.</p></div><div class="framer-11cs0wh" data-framer-name="Title"')
section = section.replace('>3</p></div><div class="framer-11cs0wh" data-framer-name="Title"', '>3.</p></div><div class="framer-11cs0wh" data-framer-name="Title"')

html = html[:idx] + section + html[end_idx:]

with open('/Users/castro/LP-dev/index.html', 'w') as f:
    f.write(html)

print("Dots added.")
