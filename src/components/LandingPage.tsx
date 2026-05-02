"use client";

import Navigation from "@/components/Navigation";
import Hero from "@/components/Hero";
import ConditionBanner from "@/components/ConditionBanner";
import Trust from "@/components/Trust";
import Coaching from "@/components/Coaching";
import Testimonials from "@/components/Testimonials";
import About from "@/components/About";
import FAQ from "@/components/FAQ";
import CTA from "@/components/CTA";
import Footer from "@/components/Footer";
import ExitIntentPopup from "@/components/ExitIntentPopup";
import { usePageView } from "@/hooks/usePageView";
import type { LpConfig } from "@/lib/lpConfig";

interface LandingPageProps {
  config: LpConfig;
}

export default function LandingPage({ config }: LandingPageProps) {
  usePageView();

  return (
    <>
      <Navigation />
      <main>
        <Hero
          preheading={config.preheading}
          headline={config.headline}
          headlineAccent={config.headlineAccent}
          subheadline={config.subheadline}
          ctaLabel={config.ctaLabel}
        />
        <ConditionBanner />
        <Trust />
        <Coaching />
        <Testimonials />
        <About />
        <FAQ />
        <CTA />
      </main>
      <Footer />
      <ExitIntentPopup />
    </>
  );
}
