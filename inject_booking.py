import re

with open('/Users/castro/LP-dev/index.html', 'r') as f:
    html = f.read()

idx_about = html.find('id="about"')
idx_faq = html.find('id="faq"', idx_about)

if idx_about != -1 and idx_faq != -1:
    end_about = html.rfind('</section>', idx_about, idx_faq) + 10 # include </section>
    
    booking_html = """
<section id="booking" style="background-color: var(--token-f2a89dfc-50f9-467f-94d3-0570b6d2745e, #F9F8F6); width: 100%; display: flex; flex-direction: column; align-items: center; padding: 100px 20px;">
    <div style="max-width: 800px; width: 100%; text-align: center; margin-bottom: 40px;">
        <h2 style="font-family: 'Inter', sans-serif; font-size: 48px; font-weight: 600; color: #1a1a1a; margin-bottom: 16px; letter-spacing: -1px;">Book Your Free Clarity Call</h2>
        <p style="font-family: 'Inter', sans-serif; font-size: 18px; color: #555555; line-height: 1.6;">Choose a time below that works best for you. We'll dive into your symptoms, your goals, and how our functional medicine approach can help you get back to feeling like yourself.</p>
    </div>
    <div style="width: 100%; max-width: 1000px; background: #ffffff; border-radius: 24px; box-shadow: 0 12px 32px rgba(0,0,0,0.06); padding: 20px; overflow: hidden; min-height: 700px;">
        <iframe src="https://api.bigboost.marketing/widget/booking/rnhZBwjvyPJEU4BrHlTF" style="width: 100%; border:none; overflow: hidden; min-height: 650px;" scrolling="no" id="3G26qYwzpdQblR9WYQoG_1778032224773"></iframe><br><script src="https://api.bigboost.marketing/js/form_embed.js" type="text/javascript"></script>
    </div>
</section>
"""
    
    html = html[:end_about] + booking_html + html[end_about:]
    
    with open('/Users/castro/LP-dev/index.html', 'w') as f:
        f.write(html)
    print("Booking section injected successfully.")
else:
    print("Could not find boundaries!")

