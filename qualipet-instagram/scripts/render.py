#!/usr/bin/env python3
"""
Renderiza uma arte HTML em PNG na dimensão exata do formato Instagram.

Uso:
    python render.py arte.html saida.png --w 1080 --h 1080

Requer Playwright (instala automaticamente se faltar):
    pip install playwright --break-system-packages && playwright install chromium
"""
import argparse
import sys
from pathlib import Path


def render(html_path: str, out_path: str, w: int, h: int):
    from playwright.sync_api import sync_playwright

    html_file = Path(html_path).resolve()
    if not html_file.exists():
        sys.exit(f"HTML não encontrado: {html_file}")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": w, "height": h},
                                device_scale_factor=2)  # 2x = nitidez
        page.goto(html_file.as_uri())
        page.wait_for_timeout(800)  # aguarda fontes/imagens
        # garante o corte exato no elemento .canvas se existir, senão página toda
        el = page.query_selector(".canvas")
        if el:
            el.screenshot(path=out_path)
        else:
            page.screenshot(path=out_path, clip={"x": 0, "y": 0, "width": w, "height": h})
        browser.close()
    print(f"OK -> {out_path} ({w}x{h})")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("out")
    ap.add_argument("--w", type=int, default=1080)
    ap.add_argument("--h", type=int, default=1080)
    args = ap.parse_args()
    render(args.html, args.out, args.w, args.h)
