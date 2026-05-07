import re

with open('/Users/castro/LP-dev/index.html', 'r') as f:
    html = f.read()

idx = html.find('id="reviews"')
end_idx = html.find('id="faq"', idx)
if end_idx == -1: end_idx = len(html)
section = html[idx:end_idx]

# Find the start and end of the first framer-95qcoa
start_idx = section.find('<div class="framer-95qcoa"')
end_idx_95 = section.find('</div></div></section>', start_idx)

if start_idx != -1 and end_idx_95 != -1:
    print('Found block, length:', end_idx_95 - start_idx)
    block = section[start_idx:end_idx_95]
    print(block[:100], '...', block[-100:])
