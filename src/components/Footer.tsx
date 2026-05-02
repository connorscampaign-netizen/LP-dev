import Image from "next/image";

export default function Footer() {
  return (
    <footer className="bg-black py-[100px_20px_60px] md:py-[100px_40px_60px]">
      <div className="mx-auto max-w-[1120px] px-5 md:px-10">
        <div className="flex flex-col md:flex-row gap-8 md:gap-[100px]">
          {/* Left: Logo + Description */}
          <div className="flex flex-col gap-4 md:max-w-sm">
            <a href="#hero" className="flex items-center gap-2">
              <Image
                src="https://framerusercontent.com/images/cdaAn72GBEIGezJT7rvyjC8LU.png?width=256&height=256"
                alt="Perform Template Logo"
                width={32}
                height={32}
                className="rounded-[50%]"
              />
              <span className="font-bold text-base text-white">Perform</span>
            </a>
            <p className="text-sm text-white/50 leading-[1.5em]">
              [PLACEHOLDER]
            </p>
            <p className="text-sm text-white/50">
              Created by{" "}
              <a
                href="https://sebadam.supply"
                target="_blank"
                rel="noopener noreferrer"
                className="text-accent hover:underline"
              >
                [PLACEHOLDER]
              </a>
            </p>
          </div>

          {/* Right: Link Columns */}
          <div className="flex flex-col sm:flex-row gap-8 sm:gap-8 md:ml-auto">
            {/* Sections Column */}
            <div className="flex flex-col gap-4">
              <span className="text-sm font-medium text-white">Sections</span>
              <a
                href="#about"
                className="text-sm text-white/50 hover:text-accent transition-colors leading-[1.5em]"
              >
                About
              </a>
              <a
                href="#coaching"
                className="text-sm text-white/50 hover:text-accent transition-colors leading-[1.5em]"
              >
                Coaching
              </a>
              <a
                href="#reviews"
                className="text-sm text-white/50 hover:text-accent transition-colors leading-[1.5em]"
              >
                Reviews
              </a>
            </div>

            {/* Socials Column */}
            <div className="flex flex-col gap-4">
              <span className="text-sm font-medium text-white">Socials</span>
              <a
                href="https://x.com"
                target="_blank"
                rel="noopener noreferrer"
                className="text-sm text-white/50 hover:text-accent transition-colors leading-[1.5em]"
              >
                Twitter
              </a>
              <a
                href="https://instagram.com"
                target="_blank"
                rel="noopener noreferrer"
                className="text-sm text-white/50 hover:text-accent transition-colors leading-[1.5em]"
              >
                Instagram
              </a>
              <a
                href="https://tiktok.com"
                target="_blank"
                rel="noopener noreferrer"
                className="text-sm text-white/50 hover:text-accent transition-colors leading-[1.5em]"
              >
                TikTok
              </a>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}
