import sys

with open('/Users/castro/LP-dev/index.html', 'r') as f:
    html = f.read()

idx = html.find('data-framer-name="H1"')
if idx != -1:
    end_idx = html.find('</h1>', idx)
    h1_html = html[idx:end_idx]
    
    # Replace white-space:nowrap
    new_h1_html = h1_html.replace('style="white-space:nowrap"', 'style="white-space:normal; display:inline-block;"')
    
    html = html[:idx] + new_h1_html + html[end_idx:]
    
    with open('/Users/castro/LP-dev/index.html', 'w') as f:
        f.write(html)
    print('Mobile header wrapping fixed!')
else:
    print('H1 not found!')

