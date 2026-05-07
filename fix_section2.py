import re

with open('/Users/castro/LP-dev/index.html', 'r') as f:
    html = f.read()

# 1. Fix the intro text
html = html.replace('From beginners to seasoned pros, I create custom plans</span>', 'Dr. Adam Dombrowski is a Naturopathic Doctor creating customized protocols</span>')
html = html.replace(' tailored to help you unlock your full potential and succeed in races.', ' tailored to help you uncover hidden dysfunction and achieve optimal health.')

# 2. Fix the trust grid counters
# We will use regex to find the spans and the labels.
# The structure is roughly: <span ...>0<!-- -->+</span> ... <p ...>Years of Experience</p>
# We can replace all 0<!-- -->+ with a placeholder, but it's better to just regex the whole block or do it by finding labels.

def replace_counter(html, label, new_label, new_value):
    # Find the label
    idx = html.find(label)
    if idx == -1: return html
    
    # We need to look backwards from the label to find the span containing the number
    # It looks like: <span ...>VALUE</span> ... <p ...>LABEL</p>
    # We search backwards for `<span ` and `</span>`
    span_end = html.rfind('</span>', 0, idx)
    span_start = html.rfind('<span ', 0, span_end)
    
    if span_start != -1 and span_end != -1:
        # The content of the span is between span_start and span_end + 7
        span_html = html[span_start:span_end + 7]
        # Replace whatever value is inside the span with new_value
        new_span_html = re.sub(r'(>)(.*?)(</span>)', r'\g<1>' + new_value + r'\3', span_html)
        
        # Also remove opacity:0 to make sure it's visible
        new_span_html = new_span_html.replace('opacity:0;transition:opacity 0.5s ease-in-out', 'opacity:1')
        
        # Replace the span in the html
        html = html[:span_start] + new_span_html + html[span_end + 7:]
        
        # Now update the label
        idx = html.find(label) # find again because length changed
        html = html[:idx] + html[idx:].replace(label, new_label, 1)
        
    return html

html = replace_counter(html, 'Years of Experience', 'Years of Experience', '14+')
html = replace_counter(html, 'Practitioners', 'Practitioners', '5')
html = replace_counter(html, 'Race strategies', 'Members Helped', 'Thousands')
html = replace_counter(html, 'Training hours', '120 Google Reviews', '4.9★')

# Do it again for the ssr-variants! The HTML probably has duplicates of these for SSR vs Client.
# Let's just run it multiple times until it doesn't find any.
for _ in range(5):
    html = replace_counter(html, 'Years of Experience', 'Years of Experience', '14+')
    html = replace_counter(html, 'Practitioners', 'Practitioners', '5')
    html = replace_counter(html, 'Race strategies', 'Members Helped', 'Thousands')
    html = replace_counter(html, 'Training hours', '120 Google Reviews', '4.9★')

# We also need to fix opacity:0 for the "14+" and "4.9★" that were ALREADY updated by my previous script 
# but might still have opacity:0!
html = html.replace('opacity:0;transition:opacity 0.5s ease-in-out', 'opacity:1')

# Write back
with open('/Users/castro/LP-dev/index.html', 'w') as f:
    f.write(html)
print('Done!')
