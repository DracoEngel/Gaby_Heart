"""Abre la animación del corazón azul (partículas + explosión + Gaby)."""

from pathlib import Path
import webbrowser


def main() -> None:
    html = Path(__file__).with_name("blue_heart.html").resolve()
    if not html.exists():
        raise SystemExit(f"No se encontró: {html}")
    webbrowser.open(html.as_uri())
    print("Animación abierta en el navegador.")
    print("Clic: explotar / reiniciar.")


if __name__ == "__main__":
    main()
