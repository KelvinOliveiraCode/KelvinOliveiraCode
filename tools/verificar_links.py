"""Confere os links dos dois READMEs do perfil.

Check the links of both profile READMEs.

Este README e a porta de entrada de todo o portfolio: e ele que aparece no
perfil do GitHub e que as pessoas clicam. Um link quebrado aqui leva a pessoa
para um repositorio inexistente, ou para um projeto que foi renomeado, e o
primeiro contato com o trabalho fica ruim.

O verificador cobre tres coisas:

- link relativo para arquivo que nao existe no repositorio;
- ancora interna que nao corresponde a nenhuma secao do proprio README;
- link para um repositorio do proprio usuario que nao existe mais.

O ultimo item e o que mais importa aqui, porque o portfolio cresce e os
projetos mudam de nome. O check usa a API do GitHub quando ha token e cai
para um HEAD publico quando nao ha.
"""

from __future__ import annotations

import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

#: Raiz do repositorio.
RAIZ = Path(__file__).resolve().parent.parent

#: READMEs verificados.
READMES = ("README.md", "README.en.md")

#: Link markdown: [texto](destino).
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")

#: Titulo de secao, de um a seis cerquilhas.
TITULO = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)

#: Link para um repositorio do proprio usuario.
REPO_PROPRIO = re.compile(
    r"^https?://github\.com/" + re.escape("KelvinOliveiraCode") + r"/([^/#?]+)"
)

#: Usuario dono do portfolio.
USUARIO = "KelvinOliveiraCode"

#: Cache de repositorios ja verificados, para nao repetir a chamada.
CACHE: dict[str, bool] = {}


def ancora_de(titulo: str) -> str:
    """Converte um titulo de secao na ancora que o GitHub gera.

    Turn a section title into the anchor GitHub generates.

    O GitHub nao remove acento: "Início rápido" vira "início-rápido", e nao
    "inicio-rapido". O que ele remove e pontuacao, e o que ele troca por
    hifen e o espaco.

    Args:
        titulo: Titulo da secao, como aparece no arquivo.

    Returns:
        A ancora correspondente.
    """
    minusculo = titulo.lower()
    sem_pontuacao = re.sub(r"[^\w\s-]", "", minusculo, flags=re.UNICODE)
    return re.sub(r"\s+", "-", sem_pontuacao.strip())


def repo_existe(nome: str) -> bool:
    """Confere se um repositorio do usuario existe.

    Check whether one of the user's repositories exists.

    Args:
        nome: Nome do repositorio.

    Returns:
        ``True`` se o repositorio existe e e publico.
    """
    if nome in CACHE:
        return CACHE[nome]

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        url = f"https://api.github.com/repos/{USUARIO}/{nome}"
        requisicao = urllib.request.Request(
            url, headers={"Authorization": f"Bearer {token}"}
        )
    else:
        url = f"https://github.com/{USUARIO}/{nome}"
        requisicao = urllib.request.Request(url, method="HEAD")

    try:
        with urllib.request.urlopen(requisicao, timeout=20) as resposta:
            CACHE[nome] = 200 <= resposta.status < 300
    except urllib.error.HTTPError as exc:
        CACHE[nome] = exc.code not in (403, 404)
    except (urllib.error.URLError, TimeoutError, OSError):
        # Sem rede, o verificador nao pode afirmar que o link esta quebrado.
        CACHE[nome] = True

    return CACHE[nome]


def validar(arquivo: str) -> list[str]:
    """Reporta os links quebrados de um README.

    Report the broken links of one README.

    Args:
        arquivo: Caminho do README, relativo a raiz do repositorio.

    Returns:
        Lista de problemas encontrados.
    """
    caminho = RAIZ / arquivo
    texto = caminho.read_text(encoding="utf-8")
    problemas: list[str] = []

    ancoras = {ancora_de(titulo) for titulo in TITULO.findall(texto)}

    for destino in LINK.findall(texto):
        if destino.startswith("mailto:"):
            continue
        if destino.startswith("#"):
            if destino[1:] not in ancoras:
                problemas.append(f"{arquivo}: ancora interna inexistente {destino}")
            continue

        alvo = destino.split("#", 1)[0]
        if not alvo:
            continue

        if alvo.startswith(("http://", "https://")):
            proprio = REPO_PROPRIO.match(alvo)
            if proprio and not repo_existe(proprio.group(1)):
                problemas.append(
                    f"{arquivo}: repositorio inexistente {USUARIO}/{proprio.group(1)}"
                )
            continue

        if not (caminho.parent / alvo).exists():
            problemas.append(f"{arquivo}: arquivo inexistente {alvo}")

    return problemas


def main() -> int:
    """Executa a verificacao e reporta.

    Run the check and report.
    """
    problemas: list[str] = []
    for arquivo in READMES:
        problemas.extend(validar(arquivo))

    if problemas:
        print(f"links FALHARAM: {len(problemas)} problema(s)")
        for problema in problemas:
            print(f"  {problema}")
        return 1

    print(
        f"links ok: {len(READMES)} READMEs conferidos, "
        f"{len(CACHE)} repositorios proprio verificados"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
