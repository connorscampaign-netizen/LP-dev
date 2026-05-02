const conditions = [
  "[PLACEHOLDER] Condition 1",
  "[PLACEHOLDER] Condition 2",
  "[PLACEHOLDER] Condition 3",
  "[PLACEHOLDER] Condition 4",
  "[PLACEHOLDER] Condition 5",
  "[PLACEHOLDER] Condition 6",
];

export default function ConditionBanner() {
  return (
    <div className="bg-accent overflow-hidden py-3">
      <div className="marquee-track flex whitespace-nowrap">
        {/* Duplicate content for seamless loop */}
        {[...conditions, ...conditions].map((condition, i) => (
          <span
            key={i}
            className="inline-flex items-center gap-3 mx-6 text-sm font-medium text-white"
          >
            <svg
              width="6"
              height="6"
              viewBox="0 0 6 6"
              fill="currentColor"
              className="flex-shrink-0"
            >
              <circle cx="3" cy="3" r="3" />
            </svg>
            {condition}
          </span>
        ))}
      </div>
    </div>
  );
}
