import Image from "next/image";

const contentBlocks = [
  {
    id: "about-a",
    textPart1: "[PLACEHOLDER]",
    textPart2: "[PLACEHOLDER]",
    image:
      "https://framerusercontent.com/images/o1iEuFuB1ARuwoXcEgQQTV0CYbw.png?width=2048&height=2048",
    alt: "[PLACEHOLDER]",
  },
  {
    id: "about-b",
    textPart1: "[PLACEHOLDER]",
    textPart2: "[PLACEHOLDER]",
    image:
      "https://framerusercontent.com/images/8lKQIagOcEDwIqkeNZQlhcYDmXc.png?width=1024&height=1024",
    alt: "[PLACEHOLDER]",
  },
  {
    id: "about-c",
    textPart1: "[PLACEHOLDER]",
    textPart2: "[PLACEHOLDER]",
    image:
      "https://framerusercontent.com/images/MWQJ2oXomYD1Ax98qj75iZ4owGE.png?width=1024&height=1024",
    alt: "[PLACEHOLDER]",
  },
];

export default function About() {
  return (
    <section id="about" className="py-[120px_20px] md:py-[120px_40px] bg-black">
      <div className="mx-auto max-w-[1120px] px-5 md:px-10 flex flex-col gap-12 md:gap-20">
        {contentBlocks.map((block, i) => (
          <div
            key={block.id}
            id={block.id}
            className={`flex flex-col ${i % 2 === 0 ? "md:flex-row" : "md:flex-row-reverse"} items-center gap-8 md:gap-[100px]`}
          >
            {/* Image */}
            <div className="w-full md:w-1/2 relative rounded-2xl overflow-hidden aspect-[5/3]">
              <Image
                src={block.image}
                alt={block.alt}
                fill
                className="object-cover"
              />
            </div>

            {/* Text */}
            <div className="w-full md:w-1/2 flex flex-col gap-4 max-w-[544px]">
              <p className="text-base md:text-[20px] leading-[1.5em] text-white">
                {block.textPart1}{" "}
                <span className="text-white/50">{block.textPart2}</span>
              </p>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
