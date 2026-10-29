# AI Research Terminal — Deployment guide

This bundle is a self-contained GitHub Profile README design. No GitHub Actions, API keys, font downloads, third-party image host, or JavaScript are needed.

## Files

```text
<your-profile-repository>/
├── README.md
├── SETUP.md
├── build_assets.py  # optional: regenerate all 6 SVGs
└── assets/
    ├── profile-banner-dark.svg
    ├── profile-banner-light.svg
    ├── typing-dark.svg
    ├── typing-light.svg
    ├── research-pipeline-dark.svg
    └── research-pipeline-light.svg
```

## Deploy

1. Back up your existing profile `README.md` and custom SVGs.
2. Open the **public** repository whose name exactly matches your GitHub username (for example, if your username is `Am2uocVi3t`, the repository must be `Am2uocVi3t/Am2uocVi3t`). This is the GitHub profile repository, not your portfolio repository.
3. Put `README.md`, `SETUP.md`, and the entire `assets/` folder **at its root** with the exact relative paths shown above.
4. Commit and push the files, e.g.:

   ```bash
   git add README.md SETUP.md assets/
   git commit -m "Redesign profile README as AI research terminal"
   git push
   ```

5. Visit your GitHub profile. Check it in both GitHub **light and dark** themes, on desktop and on mobile. A hard refresh or a few moments may be needed while GitHub's image proxy cache updates.

The `<picture>` elements in `README.md` use the GitHub-documented `prefers-color-scheme` technique, so each theme shows its corresponding SVG.

## Animation and fallbacks

- **Banner:** subtle CSS/SVG animation (scanning signal, pulsing graph nodes, cursor) baked into each local SVG.
- **Typing:** 4 research slogans rotate with a native SVG/CSS typewriter reveal; does not contact third-party services.
- **Research visualization:** compact four-track pipeline that keeps accepted, pending and under-review status visually distinct.
- **Accessibility:** all vital descriptions and statuses appear in actual Markdown text as well, not exclusively in SVG imagery. SVG files have accessible titles/descriptions and a `prefers-reduced-motion` fallback.
- Rendering of SVG animation can vary by browser, GitHub's image proxy, accessibility settings, or platform. If motion is disabled, the design still renders as a static visual; the actual information remains in Markdown.

## Updating your profile

- Update the **Markdown research table** whenever a decision changes. Then update the **research-pipeline-dark.svg** and **research-pipeline-light.svg** labels too; otherwise the visual may be stale.
- The README intentionally uses a static `October 29, 2026` update date, not a fake live status or visitor count. Change it when you actually update the research statuses.
- To change banner text/colors, edit both `assets/profile-banner-*.svg` files (or edit `build_assets.py` and run `python build_assets.py`). Colors and text are self-contained; keep the two themes synchronized.
- To modify rotating slogans, update the text nodes in both `assets/typing-*.svg`. Keep each line short enough to fit (recommended under ~52 characters). There are 4 timed 5-second slots in a 20-second loop.
- To remove animation, add `animation: none !important;` to the affected SVG styles or replace animated SVGs with exported PNG images.

## Troubleshooting

- **Banner missing?** Check filename capitalization and that the paths begin `./assets/` from the root README. Ensure the files are committed.
- **Wrong light/dark banner?** Check GitHub theme settings and try hard refresh. `<picture>` uses the viewer's color-scheme media preference.
- **Animation static?** Test opening the SVG directly in a modern browser. Some clients turn off SVG motion or honor `prefers-reduced-motion`. All essential content should still appear in Markdown.
- **Mobile text too small?** SVG banners scale to the screen; the README's real Markdown introduction and research table give mobile readers selectable text.

## Source notes

This bundle reproduces the research links, statuses, project descriptions, experience, toolkit and contacts supplied for the profile as of October 29, 2026. No external GitHub metrics, GitHub profile views or publication decisions are fabricated.

GitHub docs:
- https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme
- https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github
