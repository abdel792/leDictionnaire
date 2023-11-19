# Le dictionnaire #

* Auteurs : Abdel.
* Télécharger [version stable][1]
* Télécharger [version de développement][2]

Cette extension vous permet d'afficher la définition d'un mot saisi en utilisant le site : «https://www.le-dictionnaire.com».

Elle ajoute un item dans le menu Outils de NVDA nommé «Le dictionnaire».

Lorsque vous validez sur cet item, vous obtenez une boîte de dialogue composée des éléments suivants :

* Un champ de saisie pour saisir le mot dont vous recherchez la définition;
{: #promptToEnterSearchTerms }
* Un bouton "OK" pour afficher un message répondant au mode choisi dans les paramètres, contenant votre définition;
* Un bouton "Annuler" pour fermer la boîte de dialogue.

## Paramètres de l'extension ## {: #leDictionnaireSettings }

Dans le panneau des paramètres de l'extension, vous devriez trouver ce qui suit :

* Mode d'affichage pour les définitions du dictionnaire, qui permet de définir le mode d'affichage des définitions trouvées;
* Ce modes d'affichage propose les 3 choix suivants :
    * Afficher dans un message HTML, qui permet d'afficher la définition dans un message HTML navigable (c'est le choix par défaut);
    * Afficher dans un message simple, qui permet d'afficher la définition dans un message simple navigable, sans formatage HTML;
    * Afficher dans le navigateur par défaut, pour afficher la définition dans votre navigateur par défaut.
* Un bouton « OK » pour sauvegarder votre configuration ;
* Un bouton "Annuler" pour annuler et fermer la boîte de dialogue.
* Un bouton « Appliquer » pour appliquer votre configuration ;

## Remarques ##

* Par défaut, le geste «contrôle + Shift + F12» est affecté au script qui affiche la boîte de dialogue invitant l'utilisateur à saisir un mot en vue d'en afficher la définition;
* Un script sans geste attribué vous permet d'ouvrir le panneau des paramètres de l'extension;
* Vous pouvez attribuer de nouveaux gestes pour exécuter ces scripts dans le menu «Gestes de commandes» et plus précisément, dans la catégorie «Le dictionnaire»;
* Si vous utilisez nvda-2021.1 ou version ultérieure, vous pourrez accéder à l'aide du champ de saisie du mot à rechercher, ainsi qu'à celui du panneau des paramètres de l'extension en pressant simplement sur la touche "F1" dès que le focus sera sur l'un de ces 2 contrôles;

## Compatibilité ##

* Cette extension est compatible avec NVDA 2019.3 et au-delà.

## Changements pour la version 23.11.19 ##

* Version initiale.
  

[1]: https://github.com/abdel792/leDictionnaire/releases/download/v23.11.19/leDictionnaire-23.11.19.nvda-addon

[2]: http://cyber25.free.fr/nvda-addons/leDictionnaire-23.11.19-dev.nvda-addon
