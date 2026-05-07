import sys
import re

with open('/Users/castro/LP-dev/index.html', 'r') as f:
    html = f.read()

old_text = r'(<span style="--framer-text-color:[^"]*")( class="framer-text">)Dr\. Adam Dombrowski is a Naturopathic Doctor creating customized protocols</span> tailored to help you uncover hidden dysfunction and achieve optimal health\.'

new_text = r'\g<1>; font-weight: 700;\g<2>Chronic fatigue, weight gain, mood swings and a body that feels like it\'s working against you?</span> We combine advanced testing with natural protocols so you can feel like yourself again, <span style="font-style: italic;">without a prescription for every symptom</span>'

html, num_subs = re.subn(old_text, new_text, html)

if num_subs > 0:
    with open('/Users/castro/LP-dev/index.html', 'w') as f:
        f.write(html)
    print(f'Updated copy successfully. {num_subs} replacements made.')
else:
    print('Failed to find the text to replace.')
