"use client";

import { useState } from "react";
import Image from "next/image";

export default function Navigation() {
  const [mobileOpen, setMobileOpen] = useState(false);

  const navLinks = [
    { label: "Coaching", href: "#coaching" },
    { label: "Reviews", href: "#reviews" },
    { label: "About", href: "#about" },
    { label: "Contact", href: "#contact" },
  ];

  return (
    <nav className="fixed top-0 left-0 right-0 z-10 backdrop-blur-[4px] bg-white/15">
      <div className="mx-auto max-w-[1120px] px-5 md:px-10 flex items-center justify-between h-12">
        {/* Logo */}
        <a href="#hero" className="flex items-center gap-2">
          <Image
            src="https://framerusercontent.com/images/cdaAn72GBEIGezJT7rvyjC8LU.png?width=256&height=256"
            alt="Perform Template Logo"
            width={32}
            height={32}
            className="rounded-[50%]"
          />
          <span className="font-bold text-base text-black">Perform</span>
        </a>

        {/* Desktop Nav */}
        <div className="hidden md:flex items-center gap-8">
          {navLinks.map((link) => (
            <a
              key={link.label}
              href={link.href}
              className="text-sm text-black hover:text-accent transition-colors"
            >
              {link.label}
            </a>
          ))}
        </div>

        {/* Desktop CTA */}
        <a
          href="#contact"
          className="hidden md:flex items-center gap-2 h-10 px-5 rounded-3xl border border-white/50 text-sm font-medium text-black hover:bg-accent hover:text-white hover:border-accent transition-all"
        >
          Get template
        </a>

        {/* Mobile Hamburger */}
        <button
          onClick={() => setMobileOpen(!mobileOpen)}
          className="md:hidden flex flex-col gap-1.5 p-2"
          aria-label="Toggle menu"
        >
          <span
            className={`block w-5 h-0.5 bg-black transition-transform ${mobileOpen ? "rotate-45 translate-y-2" : ""}`}
          />
          <span
            className={`block w-5 h-0.5 bg-black transition-opacity ${mobileOpen ? "opacity-0" : ""}`}
          />
          <span
            className={`block w-5 h-0.5 bg-black transition-transform ${mobileOpen ? "-rotate-45 -translate-y-2" : ""}`}
          />
        </button>
      </div>

      {/* Mobile Menu */}
      {mobileOpen && (
        <div className="md:hidden bg-white border-t border-gray-100 px-5 py-6">
          <div className="flex flex-col gap-4">
            {navLinks.map((link) => (
              <a
                key={link.label}
                href={link.href}
                onClick={() => setMobileOpen(false)}
                className="text-base text-black hover:text-accent transition-colors"
              >
                {link.label}
              </a>
            ))}
            <a
              href="#contact"
              onClick={() => setMobileOpen(false)}
              className="inline-flex items-center justify-center gap-2 h-10 px-5 rounded-3xl border border-white/50 text-sm font-medium text-black hover:bg-accent hover:text-white hover:border-accent transition-all mt-2"
            >
              Get template
            </a>
          </div>
        </div>
      )}
    </nav>
  );
}
