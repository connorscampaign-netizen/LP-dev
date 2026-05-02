import Image from "next/image";

const stats = [
  { value: "[PLACEHOLDER]", label: "Years of experience" },
  { value: "[PLACEHOLDER]", label: "Athletes coached" },
  { value: "[PLACEHOLDER]", label: "Race strategies" },
  { value: "[PLACEHOLDER]", label: "Training hours" },
];

export default function Trust() {
  return (
    <section id="trust" className="py-[100px_20px_40px] md:py-[100px_40px_40px] bg-white">
      <div className="mx-auto max-w-[1120px] px-5 md:px-10">
        {/* Top Part: Image + Heading */}
        <div className="flex flex-col lg:flex-row items-center gap-8 md:gap-16 mb-16 md:mb-24">
          {/* Image */}
          <div className="w-full lg:w-1/2 relative rounded-2xl overflow-hidden aspect-[5/3]">
            <Image
              src="https://framerusercontent.com/images/gp4mvRHplWrG6CPCDPe7gBqSKI.png?width=1024&height=1024"
              alt="[PLACEHOLDER]"
              fill
              className="object-cover"
            />
          </div>

          {/* Text */}
          <div className="w-full lg:w-1/2 flex flex-col gap-6">
            <h2 className="font-[family-name:var(--font-manrope)] text-[24px] md:text-[36px] lg:text-[52px] font-bold leading-[1.2em] tracking-tight text-black">
              [PLACEHOLDER]{" "}
              <span className="text-gray-dark">
                [PLACEHOLDER]
              </span>
            </h2>
          </div>
        </div>

        {/* Trust Grid */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-8 md:gap-16">
          {stats.map((stat, i) => (
            <div key={i} className="flex flex-col items-center text-center gap-2">
              <span className="font-[family-name:var(--font-manrope)] text-[36px] md:text-[52px] lg:text-[72px] font-bold text-accent leading-[1.2em]">
                {stat.value}
              </span>
              <span className="text-sm md:text-base text-gray-dark leading-[1.5em]">
                {stat.label}
              </span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
