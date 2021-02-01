README.TXT VERSION

- Projet Cloud Computing -
* M1 IOT - H3Hitema *

_Notes informatives_
1-/ Tout a été reformulé et non copié/collé, pour m'assurer de bien comprendre ce qui est demandé /
2-/ Il a été réalisé tardivement, des suites de soucis avec l'ordinateur principal utilisé habituellement (surface) comme noté dans slack /


| Présentation |

Je suis un ML Engineer Junior dans une entreprise, qui travaille sur le vaccin du covid. Je présenterai ici une mini pipeline data, une problématique pertinente, la collecte de données, ainsi que le développement d'une API et d'un paquetage Docker. Ce projet sera accompagné d'une documentation claire et explicite. 

| Livrables | 

* Un rapport PDF (4 pages minimum) sur l'élaboration technique et les différentes étapes
* Un repo git (public) avec un README.md (peut servir de documentation) 
* Un lien vers l'application hébergée sur la VM ou sur un cloud (ex : Heroku, aws..)
* Un lien vers le projet sur le gsheet

| Contraintes |

* Data de 15 colonnes minimum, dont une étant une date, et 3 catégorielles
* Exposer une problématique claire (objectif du modèle, situation métier..)
* Documentation impeccable du doc, commentaires et docstring
* +1,5 si la data n'a pas été traitée en cours

_Rappel_

Docstring = "In programming, a docstring is a string literal specified in source code that is used, like a comment, to document a specific segment of code. Unlike conventional source code comments, or even specifically formatted comments like Javadoc documentation, docstrings are not stripped from the source tree when it is parsed and are retained throughout the runtime of the program. This allows the programmer to inspect these comments at run time, for instance as an interactive help system, or as metadata." (Wikipédia)

Aide à la docstring : https://www.python.org/dev/peps/pep-0257/

| Dataset : Pfizer Vaccine Tweets |
Contexte : Collecte des tweets récents à propos du vaccin (contre le covid-19) de Pfizer & BioNTech

Nombre de colonnes : 16

Colonnes principales :
* Les colonnes sur le commentateur :
    * user_name : Nom du Co
    * user_location : Lieu de vie du Co
    * user_description : "Biographie" du Co
    * user_created : Date de création du compte du Co
    * user followers : Nombre d'abonnés du Co
    * user_friends : Nombre d'amis du Co

_Co = commentateur_

* Les colonnes sur le tweet :
    * date : Date du tweet
    * text : Texte du tweet
    * hashtags : Les hashtags utilisés pour le tweet
    * source : Plateforme sur laquelle le tweet a été posté (iPhone, Web app..)
    * retweets : Nombre de retweets