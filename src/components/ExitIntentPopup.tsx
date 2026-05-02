"use client";

import { useState, useEffect, useCallback } from "react";

export default function ExitIntentPopup() {
  const [visible, setVisible] = useState(false);
  const [dismissed, setDismissed] = useState(false);

  const handleMouseLeave = useCallback(
    (e: MouseEvent) => {
      if (e.clientY <= 0 && !dismissed) {
        setVisible(true);
      }
    },
    [dismissed]
  );

  useEffect(() => {
    document.addEventListener("mouseleave", handleMouseLeave);
    return () => document.removeEventListener("mouseleave", handleMouseLeave);
  }, [handleMouseLeave]);

  const handleClose = () => {
    setVisible(false);
    setDismissed(true);
  };

  if (!visible) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      {/* Backdrop */}
      <div
        className="absolute inset-0 bg-black/50 backdrop-blur-sm"
        onClick={handleClose}
      />

      {/* Popup */}
      <div className="relative z-10 bg-white rounded-3xl p-8 md:p-10 max-w-md mx-5 flex flex-col items-center text-center gap-6 shadow-2xl">
        {/* Close button */}
        <button
          onClick={handleClose}
          className="absolute top-4 right-4 w-8 h-8 flex items-center justify-center rounded-full hover:bg-gray-light transition-colors"
          aria-label="Close popup"
        >
          <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
            <path
              d="M1 1l12 12M13 1L1 13"
              stroke="#000"
              strokeWidth="1.5"
              strokeLinecap="round"
            />
          </svg>
        </button>

        {/* Icon */}
        <div className="w-14 h-14 rounded-2xl bg-accent/15 flex items-center justify-center">
          <svg
            width="28"
            height="28"
            viewBox="0 0 24 24"
            fill="none"
            stroke="#7a9e7e"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <circle cx="12" cy="12" r="10" />
            <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3" />
            <line x1="12" y1="17" x2="12.01" y2="17" />
          </svg>
        </div>

        {/* Heading */}
        <h3 className="font-[family-name:var(--font-manrope)] text-xl md:text-2xl font-bold text-black leading-[1.2em]">
          Wait — don&apos;t leave yet!
        </h3>

        {/* Body */}
        <p className="text-sm md:text-base text-gray-dark leading-[1.5em]">
          Find out what&apos;s holding your health back with our free 2-minute
          assessment.
        </p>

        {/* CTA */}
        <a
          href="#contact"
          onClick={handleClose}
          className="inline-flex items-center gap-3 h-11 px-6 rounded-3xl bg-accent text-white text-sm font-medium hover:bg-accent-hover transition-colors"
        >
          Find out what&apos;s holding your health back
          <svg
            width="16"
            height="16"
            viewBox="0 0 16 16"
            fill="none"
            className="rotate-[-45deg]"
          >
            <path
              d="M3 8h10M9 4l4 4-4 4"
              stroke="currentColor"
              strokeWidth="1.5"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          </svg>
        </a>

        {/* Dismiss link */}
        <button
          onClick={handleClose}
          className="text-xs text-gray-darker hover:text-gray-dark transition-colors"
        >
          No thanks, I&apos;ll stay stuck
        </button>
      </div>
    </div>
  );
}
