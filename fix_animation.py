import sys

with open('/Users/castro/LP-dev/index.html', 'r') as f:
    html = f.read()

js_snippet = """
<script>
document.addEventListener('DOMContentLoaded', () => {
    const targetTexts = ['14+', '5', '1000+', '4.9★'];
    // Find all spans that exactly match the target texts
    const spans = Array.from(document.querySelectorAll('span')).filter(span => targetTexts.includes(span.innerText.trim()));
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.hasAttribute('data-animated')) {
                entry.target.setAttribute('data-animated', 'true');
                animateValue(entry.target);
            }
        });
    }, { threshold: 0.5 });
    
    spans.forEach(span => observer.observe(span));
    
    function animateValue(obj) {
        const text = obj.innerText.trim();
        const targetNum = parseFloat(text.replace(/[^0-9.]/g, ''));
        const suffix = text.replace(/[0-9.]/g, '');
        const isFloat = text.includes('.');
        
        let startTimestamp = null;
        const duration = 2000;
        
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            
            const easeProgress = 1 - Math.pow(1 - progress, 4);
            let current = easeProgress * targetNum;
            
            if (!isFloat) {
                current = Math.floor(current);
            } else {
                current = current.toFixed(1);
            }
            
            obj.innerText = current + suffix;
            
            if (progress < 1) {
                window.requestAnimationFrame(step);
            } else {
                obj.innerText = text;
            }
        };
        window.requestAnimationFrame(step);
    }
});
</script>
"""

if "const targetTexts = ['14+', '5', '1000+', '4.9★'];" not in html:
    html = html.replace('</body>', js_snippet + '\n</body>')

with open('/Users/castro/LP-dev/index.html', 'w') as f:
    f.write(html)
print('Animation JS injected successfully.')
