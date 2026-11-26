import type { Provider, PullRequest } from "../types";
import { prPrefix } from "../types";

/** A PR/MR picked by the user, with the context needed to format it. */
export interface SelectedPR {
  pr: PullRequest;
  provider: Provider;
  /** Display name of the repository (label or owner/name). */
  repo: string;
}

function escapeHtml(text: string): string {
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

/** Rich-text version for the clipboard: pasted in Slack's composer, the links
 *  are clickable. */
export function formatClipboardHtml(items: SelectedPR[]): string {
  const lis = items.map(({ pr, provider, repo }) => {
    const label = escapeHtml(`${prPrefix(provider)}${pr.number} ${pr.title}`);
    return `<li><a href="${escapeHtml(pr.url)}">${label}</a> — ${escapeHtml(repo)} (${escapeHtml(pr.author.login)})</li>`;
  });
  return `<ul>${lis.join("")}</ul>`;
}

/** Plain-text fallback for the clipboard (apps that ignore text/html). */
export function formatClipboardText(items: SelectedPR[]): string {
  return items
    .map(
      ({ pr, provider, repo }) =>
        `• ${prPrefix(provider)}${pr.number} ${pr.title} — ${repo} (${pr.author.login})\n  ${pr.url}`,
    )
    .join("\n");
}
