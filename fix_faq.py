import re

with open('/Users/castro/LP-dev/index.html', 'r') as f:
    html = f.read()

# I will just write a Javascript block to dynamically fetch and insert the answers,
# or simply append the answers directly using python.

faqs = [
    {
        "q": "What is functional medicine?",
        "a": "It is a systems-biology approach that focuses on identifying and addressing the root cause of disease, rather than just suppressing symptoms."
    },
    {
        "q": "Do you accept insurance?",
        "a": "We are out-of-network with all insurance providers to ensure we can spend adequate time with you without restrictions, but we can provide a superbill for you to submit."
    },
    {
        "q": "How long until I see results?",
        "a": "Most patients notice improvements within the first 4-6 weeks, though full protocols for chronic issues typically take 3-6 months."
    },
    {
        "q": "Are labs included?",
        "a": "No, lab costs are separate. We use specialized functional testing that goes beyond standard bloodwork, and costs vary based on what your body needs."
    },
    {
        "q": "Do you prescribe medication?",
        "a": "We can, but our goal is to use targeted supplementation, lifestyle changes, and nutrition first. Medication is used only when strictly necessary."
    }
]

# The FAQ items are inside <div class="framer-l2sjy4-container">
# Let's find each "Top Part" and append an answer div inside the parent wrapper.
faq_script = """
<style>
.custom-faq-answer {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease-out, padding 0.3s ease-out, opacity 0.3s ease-out;
    opacity: 0;
    color: var(--token-356fc046-e6c8-4e69-a8b7-63514005dec6, #555);
    font-size: 16px;
    line-height: 1.5em;
    padding: 0 0;
}
.custom-faq-answer.open {
    max-height: 300px;
    opacity: 1;
    padding: 10px 0 20px 0;
}
.framer-2k822i {
    cursor: pointer;
}
</style>
<script>
document.addEventListener("DOMContentLoaded", () => {
    const answers = [
        "It is a systems-biology approach that focuses on identifying and addressing the root cause of disease, rather than just suppressing symptoms.",
        "We are out-of-network with all insurance providers to ensure we can spend adequate time with you without restrictions, but we can provide a superbill for you to submit.",
        "Most patients notice improvements within the first 4-6 weeks, though full protocols for chronic issues typically take 3-6 months.",
        "No, lab costs are separate. We use specialized functional testing that goes beyond standard bloodwork, and costs vary based on what your body needs.",
        "We can, but our goal is to use targeted supplementation, lifestyle changes, and nutrition first. Medication is used only when strictly necessary."
    ];

    const topParts = document.querySelectorAll('.framer-2k822i[data-framer-name="Top Part"]');
    topParts.forEach((topPart, index) => {
        // Append answer div
        const answerDiv = document.createElement('div');
        answerDiv.className = 'custom-faq-answer';
        answerDiv.innerText = answers[index] || "Please contact us for more information.";
        topPart.parentNode.appendChild(answerDiv);

        // Add click listener
        topPart.addEventListener('click', () => {
            const isOpen = answerDiv.classList.contains('open');
            // close all
            document.querySelectorAll('.custom-faq-answer').forEach(ans => ans.classList.remove('open'));
            document.querySelectorAll('.framer-dombwf').forEach(line => line.style.transform = 'rotate(90deg)'); // reset plus

            if (!isOpen) {
                answerDiv.classList.add('open');
                // rotate plus icon to minus
                const vLine = topPart.querySelector('.framer-dombwf');
                if (vLine) vLine.style.transform = 'rotate(0deg)';
            }
        });
    });
});
</script>
"""

html = html.replace('</body>', faq_script + '\n</body>')

with open('/Users/castro/LP-dev/index.html', 'w') as f:
    f.write(html)

print('FAQ script added.')
