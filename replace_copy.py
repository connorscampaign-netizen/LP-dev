import sys, re

def replace_html():
    with open('/Users/castro/LP-dev/index.html', 'r') as f:
        html = f.read()

    # 1. Colors
    html = html.replace('rgb(0, 153, 255)', 'rgb(122, 158, 126)')
    html = html.replace('#0099ff', '#7a9e7e')
    html = html.replace('rgb(245, 182, 20)', 'rgb(122, 158, 126)')
    html = html.replace('#f5b614', '#7a9e7e')

    # 2. NAV
    html = re.sub(r'>Perform<', '>Live Wellness<', html)
    html = re.sub(r'>Coaching<', '>How It Works<', html)
    html = re.sub(r'>Reviews<', '>Results<', html)
    html = re.sub(r'>Get template<', '>Book a Free Call<', html)

    # 3. HERO
    html = re.sub(r'>Experienced triathlon coach<', '>Functional Medicine · Virtual & In-Person · Coconut Creek, FL<', html)
    # Hero H1 - Level Up Your Performance
    html = re.sub(r'>Level Up Your<', '>Get to the Root Of<', html)
    html = re.sub(r'>Performance<', '>Your Health<', html)
    # Or if it's one string
    html = html.replace('Level Up Your Performance', 'Get to the Root Of Your Health')
    
    html = html.replace('Improve your triathlon performance with personalized training plans guided by an experienced coach committed to your success.', 
                        'Feeling off but told your labs are normal? Our practitioners find what conventional medicine misses.')
    html = html.replace('Start now', 'Book a Free Call')
    html = html.replace('100+ Positive Client Reviews', '4.9★ across 120 Google Reviews')

    # 4. TRUST (We must also update the JS targetMap for counters)
    html = html.replace('Years of experience', 'Years of Experience')
    html = html.replace('Athletes coached', 'Practitioners')
    html = html.replace('Races completed', 'Members Helped')
    html = html.replace('Positive reviews', 'Google Reviews')

    # Wait, the numbers in JS targetMap:
    # 10 -> 14+, 100 -> 5, 50 -> Thousands, 1000 -> 4.9★
    # The JS has: targetMap = {'10': 10, '100': 100, '50': 50, '1000': 1000}
    # It will be hard to animate 'Thousands' or '4.9★'. I will disable the JS counter for strings and just hardcode them in the HTML if possible, or modify the targetMap and let JS just set the text if it's not a pure number.
    # Actually, I'll update the targetMap in a second pass.

    # 5. COACHING
    html = html.replace('Coaching plans', 'How It Works')
    html = html.replace('Beginner Plan', 'Assessment')
    html = html.replace('Perfect for first-timers looking to build a strong foundation and cross the finish line with confidence.', 'A comprehensive intake covering your full health history, symptoms, and goals. No rushed appointments.')
    html = html.replace('Advanced Plan', 'Lab Testing')
    html = html.replace('Designed for competitive athletes aiming to shave off time and achieve new personal bests.', 'Advanced functional panels beyond standard bloodwork — hormones, thyroid, gut, nutrients, and more.')
    html = html.replace('Custom Plan', 'Your Protocol')
    html = html.replace('Tailored to your specific needs, focusing on weaknesses and optimizing your overall performance.', 'A personalised plan with ongoing practitioner support. Virtual or in-person at our Coconut Creek clinic.')

    # Remove pricing - simple way is to hide elements with $49/mo
    html = re.sub(r'<div[^>]*>\s*<p[^>]*>\$49/mo</p>\s*</div>', '', html)
    html = re.sub(r'<div[^>]*>\s*<p[^>]*>\$99/mo</p>\s*</div>', '', html)
    html = html.replace('$49/mo', '')
    html = html.replace('$99/mo', '')
    html = html.replace('Contact us', '')

    # 6. TESTIMONIALS
    html = html.replace("With the right coaching, I was able to push past my limits. I couldn't have reached my goals without the guidance and support of an experienced coach.", 
                        "After years of minimal labs and little explanation, this was the first time everything was laid out clearly. Genuinely life-changing.")
    html = html.replace('Emily Johnson, Yoga Instructor', "Hannah K. · Hashimoto's & Hormones")
    
    html = html.replace("I've never felt stronger or more prepared for a race. The training program was challenging but incredibly effective.",
                        "I've lost 30 pounds, my joint pain is gone, the brain fog lifted. As a busy mother, this program has made a real difference in how I feel every day.")
    html = html.replace('Michael Davis, Amateur Triathlete', 'Kerry M. · Gut Health & Weight')
    
    html = html.replace("The personalized plan made all the difference. I improved my times significantly and felt great throughout the entire season.",
                        "The most personalized care I've ever experienced. I feel healthier, stronger, and more like myself again.")
    html = html.replace('Sarah Wilson, Marathon Runner', 'Kimberley B. · Postpartum Recovery')

    # 7. ABOUT
    html = html.replace('I started my triathlon journey struggling with balance and technique. <span style="--framer-text-color:var(--token-bfbbf012-d3b7-4f22-a08b-2c9f0c1c5b80, rgb(153, 153, 153))" class="framer-text">Now, I guide others to achieve their full potential.</span>',
                        'Dr. Adam Dombrowski is a Naturopathic Doctor, Acupuncturist, and Wellness Speaker with 14+ years helping people reclaim their health through functional medicine.')
    html = html.replace('With years of experience competing in triathlons, I know what it takes to succeed.',
                        'Where conventional medicine looks for disease, we look for dysfunction — the subtle imbalances that leave you exhausted, foggy, or just not right, even when standard results say otherwise.')
    html = html.replace('I have helped countless athletes reach their goals.',
                        'Our team of 5 practitioners works with members virtually across the US, and in-person at our Coconut Creek, FL clinic.')
    html = html.replace('About me', 'About Dr. Adam')

    # 8. FAQ
    html = html.replace('What is included in the coaching plans?', 'What is functional medicine?')
    html = html.replace('Our coaching plans include personalized training schedules, nutritional guidance, one-on-one sessions, and regular progress assessments to ensure you reach your goals.', 
                        'We look at root causes rather than managing symptoms — using advanced lab testing and personalised protocols to address why you feel the way you feel.')
    
    html = html.replace('How do I communicate with my coach?', 'How is this different from my GP?')
    html = html.replace('You can communicate with your coach via our dedicated messaging platform, weekly video calls, and email. We ensure you have constant support throughout your journey.',
                        'GPs identify and treat disease. We work in the space before disease — imbalances in hormones, gut, thyroid, and nutrients that affect how you feel but fall outside standard thresholds.')
    
    html = html.replace('Can I change my plan later?', 'Do I need to be in Florida?')
    html = html.replace('Yes, you can upgrade or downgrade your plan at any time. Just reach out to your coach, and they will help adjust your training schedule accordingly.',
                        "No. We're fully virtual across the US. In-person is available at our Coconut Creek, FL clinic.")
    
    html = html.replace('What if I get injured?', 'How long until I see results?')
    html = html.replace('If you get injured, your coach will modify your plan to accommodate your recovery. We prioritize your health and will work with you to safely return to training.',
                        'Most members notice real improvements within 60–90 days.')
    
    html = html.replace('Do I need special equipment?', 'What conditions do you work with?')
    html = html.replace('Basic triathlon gear is required, such as a bike, helmet, running shoes, and swim gear. Your coach can provide recommendations based on your budget and goals.',
                        'Thyroid dysfunction, hormonal imbalance, gut issues, fatigue, brain fog, weight resistance, autoimmunity, and more.')
    
    html = html.replace('How long are the training plans?', "What's the first step?")
    html = html.replace('Our training plans typically range from 12 to 24 weeks, depending on the race distance and your current fitness level. Custom plans can be adjusted to fit your timeline.',
                        'Book a free discovery call — no obligation.')

    # 9. CTA SECTION
    html = html.replace('Ready to elevate your performance?', 'Ready to Feel Like Yourself Again?')
    html = html.replace('Join my coaching program today and start achieving your triathlon goals.', "Book a free discovery call and find out what's really going on.")
    html = html.replace('Get Started', 'Book a Free Call')

    # 10. FLOATING BADGE
    # Hide the remix template badge
    html = re.sub(r'<a[^>]*href=\"https://framer.website/remix\?url=[^\"]*\"[^>]*>.*?</a>', '', html)

    # 11. FOOTER
    html = html.replace('Triathlon coach dedicated to helping you achieve your personal best.', 'Functional Medicine. Real Results.')
    html = html.replace('© 2024 Perform. All rights reserved.', '© 2026 Live Wellness. All rights reserved.')

    with open('/Users/castro/LP-dev/index.html', 'w') as f:
        f.write(html)
    print("Replacements executed successfully.")

replace_html()
