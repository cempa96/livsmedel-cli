# LivsmedelCLI

LivsmedelCLI är ett enkelt program som låter dig söka på ett livsmedels näringsinnehåll i din terminal. Datan hämtas från Livsmedelsdatabasen som tillhandahålls av Livsmedelsverket via ett API. Databasen innehåller näringsinnehåll för mer än 2400 livsmedel.

## Förhandskrav

Du behöver följande installerat på din dator:

- **Python 3.8 eller nyare**
- **pip** (Python package manager, brukar följa med Python)
- **git** (för att klona ner koden)

Istället för att använda git så kan du ladda hem koden som en ZIP-fil via **Code** -> **Download ZIP**.

### Installera förhandskrav (om du inte redan har dem)

#### macOS

Installera Homebrew om du inte har det:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Installera git och python:
```bash
brew install git python
```

#### Ubuntu/Debian

```bash
sudo apt update
sudo apt install git python3 python3-pip
```

#### Windows

1. Ladda ner och installera [Git](https://git-scm.com/download/win)
2. Ladda ner och installera [Python 3](https://www.python.org/downloads/) (se till att kryssa i "Add Python to PATH" vid installationen)

## Installation av programmet

1. **Klona repon:**
    ```bash
    git clone https://github.com/cempa96/livsmedel-cli.git
    ```
2. **Navigera till mappen:**
    ```bash
    cd livsmedel-cli
    ```
3. **Installera nödvändiga Python-moduler:**
    ```bash
    pip install requests tabulate
    ```

## Användning

Du kan köra programmet via det medföljande shell-scriptet.

### Interaktivt läge

```bash
./livsmedel.sh
```
Du blir då ombedd att skriva in ett sökord.

### Sök direkt från terminalen

```bash
./livsmedel.sh [sökord]
```
Exempel:
```bash
./livsmedel.sh fläskpannkaka
```

## Tips

- Om du får felmeddelandet "Permission denied", gör scriptet körbart:
  ```bash
  chmod +x livsmedel.sh
  ```
- Om du får felmeddelandet "command not found", testa att köra med:
  ```bash
  bash livsmedel.sh
  ```
- Om du får fel om saknade moduler, installera dem med:
  ```bash
  pip install requests tabulate
  ```

## Utökning

Det är fritt fram att utöka programmet med ytterligare funktioner. Livsmedelsverkets API har fler endpoints utöver näringsinnehåll, t.ex råvaror och ingredienser. 