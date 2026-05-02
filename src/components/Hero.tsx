"use client";

interface HeroProps {
  preheading?: string;
  headline?: string;
  headlineAccent?: string;
  subheadline?: string;
  ctaLabel?: string;
}

export default function Hero({
  preheading = "[PLACEHOLDER]",
  headline = "[PLACEHOLDER]",
  headlineAccent = "[PLACEHOLDER]",
  subheadline = "[PLACEHOLDER]",
  ctaLabel = "[PLACEHOLDER]",
}: HeroProps) {
  return (
    <section
      id="hero"
      className="relative min-h-screen flex items-center justify-center overflow-hidden"
    >
      {/* Video Background */}
      <div className="absolute inset-0 z-0">
        <video
          autoPlay
          muted
          loop
          playsInline
          className="absolute inset-0 w-full h-full object-cover"
        >
          <source
            src="https://videos.pexels.com/video-files/3129671/3129671-uhd_2560_1440_30fps.mp4"
            type="video/mp4"
          />
        </video>
        <div className="absolute inset-0 bg-black/50" />
      </div>

      {/* Content */}
      <div className="relative z-[1] mx-auto max-w-[1120px] px-5 md:px-10 py-[120px_20px] md:py-[120px_40px] flex flex-col items-center text-center gap-8 md:gap-16">
        {/* Preheading */}
        <span className="text-sm md:text-base text-white/70 tracking-wide uppercase">
          {preheading}
        </span>

        {/* H1 */}
        <h1 className="font-[family-name:var(--font-manrope)] text-[24px] md:text-[54px] lg:text-[72px] font-bold leading-[1.2em] tracking-tight text-white max-w-3xl">
          {headline}
          <br />
          <span className="text-accent">{headlineAccent}</span>
        </h1>

        {/* Paragraph */}
        <p className="text-base md:text-[20px] text-white/70 leading-[1.5em] max-w-[544px]">
          {subheadline}
        </p>

        {/* CTA Button */}
        <a
          href="#contact"
          className="inline-flex items-center gap-4 h-10 md:h-12 px-5 md:px-6 rounded-3xl bg-accent text-white text-sm font-medium hover:bg-accent-hover transition-colors"
        >
          {ctaLabel}
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
