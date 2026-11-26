import { useCallback, useState } from "react";
import type { SelectedPR } from "../lib/slack";

/** Multi-selection of PRs/MRs, keyed by URL (numbers collide across repos). */
export function useSelection() {
  const [selected, setSelected] = useState<Map<string, SelectedPR>>(new Map());

  const toggle = useCallback((item: SelectedPR) => {
    setSelected((prev) => {
      const next = new Map(prev);
      if (next.has(item.pr.url)) next.delete(item.pr.url);
      else next.set(item.pr.url, item);
      return next;
    });
  }, []);

  const clear = useCallback(() => setSelected(new Map()), []);

  /** Drops selected items that are no longer in the data (merged, closed). */
  const prune = useCallback((liveUrls: Set<string>) => {
    setSelected((prev) => {
      let changed = false;
      const next = new Map<string, SelectedPR>();
      prev.forEach((item, url) => {
        if (liveUrls.has(url)) next.set(url, item);
        else changed = true;
      });
      return changed ? next : prev;
    });
  }, []);

  return { selected, toggle, clear, prune };
}
