import Navigation from "@/components/Navigation";
import Hero from "@/components/Hero";
import Trust from "@/components/Trust";
import Coaching from "@/components/Coaching";
import Testimonials from "@/components/Testimonials";
import About from "@/components/About";
import FAQ from "@/components/FAQ";
import CTA from "@/components/CTA";
import Footer from "@/components/Footer";

export default function Home() {
  return (
    <>
      <Navigation />
      <main>
        <Hero />
        <Trust />
        <Coaching />
        <Testimonials />
        <About />
        <FAQ />
        <CTA />
      </main>
      <Footer />
    </>
  );
}
