import LandingPage from "@/components/LandingPage";
import { defaultLpConfig } from "@/lib/lpConfig";

export default function Home() {
  return <LandingPage config={defaultLpConfig} />;
}
