const testimonials = [
  {
    quote: "[PLACEHOLDER]",
    author: "[PLACEHOLDER]",
  },
  {
    quote: "[PLACEHOLDER]",
    author: "[PLACEHOLDER]",
  },
  {
    quote: "[PLACEHOLDER]",
    author: "[PLACEHOLDER]",
  },
];

function StarsIcon() {
  return (
    <div className="flex gap-1.5">
      {[...Array(5)].map((_, i) => (
        <svg
          key={i}
          width="16"
          height="16"
          viewBox="0 0 16 16"
          fill="#f5b614"
        >
          <path d="M8 1.5l1.8 3.7 4.1.6-3 2.9.7 4.1L8 11l-3.6 1.8.7-4.1-3-2.9 4.1-.6L8 1.5z" />
        </svg>
      ))}
    </div>
  );
}

export default function Testimonials() {
  return (
    <section id="reviews" className="py-[100px_20px_40px] md:py-[100px_40px_40px] bg-white min-h-[80vh] flex items-center">
      <div className="mx-auto max-w-[1120px] px-5 md:px-10 w-full">
        {/* Heading */}
        <h2 className="font-[family-name:var(--font-manrope)] text-[24px] md:text-[36px] lg:text-[52px] font-bold leading-[1.2em] tracking-tight text-black text-center mb-12 md:mb-16">
          [PLACEHOLDER]
        </h2>

        {/* Testimonial Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 md:gap-10">
          {testimonials.map((testimonial, i) => (
            <div
              key={i}
              className="bg-gray-light rounded-3xl p-5 flex flex-col gap-2"
            >
              <StarsIcon />
              <p className="text-base md:text-[20px] text-gray-dark leading-[1.5em]">
                {testimonial.quote}
              </p>
              <span className="text-sm md:text-base font-medium text-black leading-[1.5em]">
                {testimonial.author}
              </span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
