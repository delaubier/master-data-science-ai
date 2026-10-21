url_wikipedia <- "https://fr.wikipedia.org/"
url_filmographie <- "wiki/Filmographie_de_Louis_de_Funès"
url <- str_c(url_wikipedia, url_filmographie)
data_html <- read_html(url)

data_html |> 
  html_elements('#mw-content-text >
                div.mw-content-ltr.mw-parser-output >
                ul:nth-child(14) >
                li:nth_child(11)') |>
  html_text()

data_html |> 
  html_elements('#mw-content-text >
                div.mw-content-ltr.mw-parser-output >
                ul:nth-child(14) >
                li:nth_child(11) >
                i >
                a') |>
  html_attrs()

data_html |>
  html_elements(xpath = "//div[@id='mw-content-text']") |>
  html_text()

## Exercice 2
# Combien de tableaux sont présents sur cette page ?
data_html <- read_html('https://fr.wikipedia.org/wiki/Coupe_du_monde_de_football_2018#')

# ou 
tableCM <- data_html |> html_table()

# Scraper la table du classement final et afficher les équipes ayant atteint les 8ème de finale
tableCM[[92]] |> 
  select(2, 14) |>
  filter(`Progression CM`!="Premier tour")

# Construire une table qui contient les buteurs de la coupe du monde dans une colonne et le nombre de buts marqués dans une autre.
tableCM[[94]] |>
  select("Joueur", `Buts marqués`)
