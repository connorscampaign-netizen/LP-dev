export default function Hero() {
  return (
    <section
      id="hero"
      className="min-h-[800px] min-h-screen flex items-center justify-center pt-12"
    >
      <div className="mx-auto max-w-[1120px] px-5 md:px-10 py-[120px_20px] md:py-[120px_40px] flex flex-col items-center text-center gap-8 md:gap-16">
        {/* Preheading */}
        <span className="text-sm md:text-base text-gray-dark tracking-wide uppercase">
          [PLACEHOLDER]
        </span>

        {/* H1 */}
        <h1 className="font-[family-name:var(--font-manrope)] text-[24px] md:text-[54px] lg:text-[72px] font-bold leading-[1.2em] tracking-tight text-black max-w-3xl">
          [PLACEHOLDER]
          <br />
          <span className="text-accent">[PLACEHOLDER]</span>
        </h1>

        {/* Paragraph */}
        <p className="text-base md:text-[20px] text-gray-dark leading-[1.5em] max-w-[544px]">
          [PLACEHOLDER]
        </p>

        {/* CTA Button */}
        <a
          href="#contact"
          className="inline-flex items-center gap-4 h-10 md:h-12 px-5 md:px-6 rounded-3xl bg-accent text-white text-sm font-medium hover:bg-accent-hover transition-colors"
        >
          [PLACEHOLDER]
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
      </div>
    </section>
  );
}
