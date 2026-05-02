import Image from "next/image";

export default function CTA() {
  return (
    <section id="contact" className="relative min-h-[80vh] flex items-center justify-center overflow-hidden">
      {/* Background Image */}
      <div className="absolute inset-0">
        <Image
          src="https://framerusercontent.com/images/jvdVI7oW19QcgbXleKvE8w4qg.png?width=1456&height=816"
          alt="[PLACEHOLDER]"
          fill
          className="object-cover"
          priority
        />
        {/* Dark Overlay with radial gradient */}
        <div
          className="absolute inset-0"
          style={{
            background:
              "radial-gradient(33% 42% at 69% 59.4%, rgba(0,0,0,0) 0%, rgba(0,0,0,0.4) 100%)",
          }}
        />
        <div className="absolute inset-0 bg-black/60" />
      </div>

      {/* Content */}
      <div className="relative z-[1] mx-auto max-w-[1120px] px-5 md:px-10 py-8 flex flex-col items-center text-center gap-8">
        <h2 className="font-[family-name:var(--font-manrope)] text-[24px] md:text-[36px] lg:text-[52px] font-bold leading-[1.2em] tracking-tight text-white">
          [PLACEHOLDER]
        </h2>
        <p className="text-base md:text-[20px] text-white/70 leading-[1.5em] max-w-[544px]">
          [PLACEHOLDER]
        </p>
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
