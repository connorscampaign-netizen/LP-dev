import Image from "next/image";

const plans = [
  {
    title: "Basic",
    price: "$59/month",
    features: [
      "[PLACEHOLDER]",
      "[PLACEHOLDER]",
      "[PLACEHOLDER]",
    ],
    image:
      "https://framerusercontent.com/images/87gay2vNzBvNe0zvqN4sc7qlKtw.png?width=1024&height=1024",
  },
  {
    title: "Standard",
    price: "$99/month",
    features: [
      "[PLACEHOLDER]",
      "[PLACEHOLDER]",
      "[PLACEHOLDER]",
    ],
    image:
      "https://framerusercontent.com/images/87gay2vNzBvNe0zvqN4sc7qlKtw.png?width=1024&height=1024",
  },
  {
    title: "Premium",
    price: "$169/month",
    features: [
      "[PLACEHOLDER]",
      "[PLACEHOLDER]",
      "[PLACEHOLDER]",
    ],
    image:
      "https://framerusercontent.com/images/87gay2vNzBvNe0zvqN4sc7qlKtw.png?width=1024&height=1024",
  },
];

function CheckIcon() {
  return (
    <svg width="16" height="17" viewBox="0 0 16 17" fill="none">
      <path
        d="M13.5 4.5L6 12L2.5 8.5"
        stroke="currentColor"
        strokeWidth="1.5"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}

function ArrowIcon() {
  return (
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
  );
}

export default function Coaching() {
  return (
    <section id="coaching" className="py-[100px_20px_40px] md:py-[100px_40px_40px] bg-gray-light">
      <div className="mx-auto max-w-[1120px] px-5 md:px-10">
        {/* Heading */}
        <h2 className="font-[family-name:var(--font-manrope)] text-[24px] md:text-[36px] lg:text-[52px] font-bold leading-[1.2em] tracking-tight text-black text-center mb-12 md:mb-16">
          [PLACEHOLDER]
        </h2>

        {/* Pricing Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {plans.map((plan, i) => (
            <div
              key={i}
              className="bg-white rounded-3xl overflow-hidden flex flex-col"
            >
              {/* Card Image */}
              <div className="relative aspect-[4/3] overflow-hidden">
                <Image
                  src={plan.image}
                  alt="[PLACEHOLDER]"
                  fill
                  className="object-cover"
                />
              </div>

              {/* Card Content */}
              <div className="p-5 flex flex-col gap-2.5 flex-1">
                <div className="flex flex-col gap-2">
                  <h3 className="font-[family-name:var(--font-manrope)] text-base md:text-lg font-bold text-black">
                    {plan.title}
                  </h3>
                  <span className="font-[family-name:var(--font-manrope)] text-[28px] md:text-[40px] font-bold text-accent leading-[1.2em]">
                    {plan.price}
                  </span>
                </div>

                {/* Features */}
                <ul className="flex flex-col gap-2.5 my-2">
                  {plan.features.map((feature, j) => (
                    <li key={j} className="flex items-start gap-2.5 text-sm text-gray-dark leading-[1.5em]">
                      <span className="text-accent mt-0.5 flex-shrink-0">
                        <CheckIcon />
                      </span>
                      {feature}
                    </li>
                  ))}
                </ul>

                {/* CTA */}
                <a
                  href="#contact"
                  className="mt-auto inline-flex items-center justify-center gap-2 h-10 px-5 rounded-3xl border border-white/50 text-sm font-medium text-black hover:bg-accent hover:text-white hover:border-accent transition-all"
                >
                  [PLACEHOLDER]
                  <ArrowIcon />
                </a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
