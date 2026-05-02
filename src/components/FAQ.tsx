"use client";

import { useState } from "react";

const faqItems = [
  {
    question: "[PLACEHOLDER]",
    answer: "[PLACEHOLDER]",
  },
  {
    question: "[PLACEHOLDER]",
    answer: "[PLACEHOLDER]",
  },
  {
    question: "[PLACEHOLDER]",
    answer: "[PLACEHOLDER]",
  },
  {
    question: "[PLACEHOLDER]",
    answer: "[PLACEHOLDER]",
  },
  {
    question: "[PLACEHOLDER]",
    answer: "[PLACEHOLDER]",
  },
];

function PlusMinusIcon({ isOpen }: { isOpen: boolean }) {
  return (
    <div className="relative w-4 h-4 flex-shrink-0">
      <span className="absolute top-1/2 left-0 w-full h-0.5 bg-black -translate-y-1/2" />
      <span
        className={`absolute top-0 left-1/2 w-0.5 h-full bg-black -translate-x-1/2 transition-transform duration-200 ${isOpen ? "rotate-90 opacity-0" : "rotate-0 opacity-100"}`}
      />
    </div>
  );
}

export default function FAQ() {
  const [openIndex, setOpenIndex] = useState<number | null>(null);

  return (
    <section id="faq" className="py-[100px_20px_60px] md:py-[100px_40px_60px] bg-white">
      <div className="mx-auto max-w-[800px] px-5 md:px-10">
        {/* Heading */}
        <div className="flex flex-col items-center text-center gap-4 mb-12 md:mb-16">
          <span className="text-sm text-accent font-medium uppercase tracking-wide">
            FAQ
          </span>
          <h2 className="font-[family-name:var(--font-manrope)] text-[24px] md:text-[36px] lg:text-[52px] font-bold leading-[1.2em] tracking-tight text-black">
            [PLACEHOLDER]
          </h2>
        </div>

        {/* FAQ Items */}
        <div className="flex flex-col">
          {faqItems.map((item, i) => (
            <div key={i} className="border-b border-gray-mid">
              <button
                onClick={() => setOpenIndex(openIndex === i ? null : i)}
                className="w-full flex items-center justify-between py-5 md:py-6 text-left gap-4"
              >
                <span className="text-base md:text-[20px] font-medium text-black leading-[1.3em]">
                  {item.question}
                </span>
                <PlusMinusIcon isOpen={openIndex === i} />
              </button>
              {openIndex === i && (
                <div className="pb-5 md:pb-6 text-sm md:text-base text-gray-dark leading-[1.5em]">
                  {item.answer}
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
