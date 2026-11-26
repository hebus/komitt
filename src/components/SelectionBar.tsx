import { useState } from "react";
import { Check, Copy, X } from "lucide-react";
import type { SelectedPR } from "../lib/slack";
import { formatClipboardHtml, formatClipboardText } from "../lib/slack";

interface Props {
  items: SelectedPR[];
  onClear: () => void;
}

type Feedback = { kind: "ok" | "error"; text: string } | null;

export function SelectionBar({ items, onClear }: Props) {
  const [feedback, setFeedback] = useState<Feedback>(null);

  function flash(next: Feedback) {
    setFeedback(next);
    setTimeout(() => setFeedback(null), 3000);
  }

  async function copy() {
    const text = formatClipboardText(items);
    try {
      // Rich text so that the links are clickable once pasted in Slack.
      await navigator.clipboard.write([
        new ClipboardItem({
          "text/html": new Blob([formatClipboardHtml(items)], { type: "text/html" }),
          "text/plain": new Blob([text], { type: "text/plain" }),
        }),
      ]);
      flash({ kind: "ok", text: "Copied" });
    } catch {
      try {
        await navigator.clipboard.writeText(text);
        flash({ kind: "ok", text: "Copied" });
      } catch {
        flash({ kind: "error", text: "Clipboard unavailable" });
      }
    }
  }

  return (
    <div className="shrink-0 flex items-center justify-between gap-3 px-4 py-2 border-t border-[var(--c-border)] bg-[var(--c-bg-subtle)]">
      <span className="text-sm text-[var(--c-text)]">
        <span className="font-semibold">{items.length}</span> selected
      </span>
      <div className="flex items-center gap-2">
        {feedback && (
          <span
            className={`text-xs ${feedback.kind === "ok" ? "text-[var(--c-green)]" : "text-[var(--c-red)]"}`}
          >
            {feedback.kind === "ok" && <Check size={12} className="inline mr-1" />}
            {feedback.text}
          </span>
        )}
        <button
          type="button"
          onClick={copy}
          className="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium rounded transition-colors bg-[var(--c-bg-inset)] hover:bg-[var(--c-border)] text-[var(--c-text)]"
        >
          <Copy size={12} />
          Copy for Slack
        </button>
        <button
          type="button"
          onClick={onClear}
          title="Clear selection"
          className="p-1.5 text-[var(--c-text-muted)] hover:text-[var(--c-text)] transition-colors"
        >
          <X size={14} />
        </button>
      </div>
    </div>
  );
}
