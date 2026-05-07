import sys, re

with open('/Users/castro/LP-dev/index.html', 'r') as f:
    html = f.read()

# Replace the HTML numbers
html = re.sub(r'>10<', '>14+<', html)
html = re.sub(r'>100<', '>5<', html)
html = re.sub(r'>50<', '>Thousands<', html)
html = re.sub(r'>1000<', '>4.9★<', html)

# Remove the JS counter logic to prevent it from overwriting the new static strings
js_start = html.find('const trustSection = document.getElementById(\'trust\');')
if js_start != -1:
    js_end = html.find('// 3. Global Reveal Animations', js_start)
    if js_end != -1:
        # Just remove that entire block
        html = html[:js_start] + html[js_end:]

with open('/Users/castro/LP-dev/index.html', 'w') as f:
    f.write(html)
print("Trust numbers updated.")
