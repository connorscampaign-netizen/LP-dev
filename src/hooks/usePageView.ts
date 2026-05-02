"use client";

import { useEffect } from "react";

declare global {
  interface Window {
    posthog?: {
      capture: (event: string, properties?: Record<string, unknown>) => void;
    };
  }
}

export function usePageView(path?: string) {
  useEffect(() => {
    const pagePath = path || window.location.pathname;

    if (typeof window !== "undefined" && window.posthog) {
      window.posthog.capture("$pageview", {
        $current_url: window.location.href,
        $pathname: pagePath,
      });
    }
  }, [path]);
}
