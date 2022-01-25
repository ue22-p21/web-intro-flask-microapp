# propos

Une minuscule petite app en Flask pour démontrer les aller-retour entre navigateur et serveur

# comment s'en servir

* mettre des '.png' dans le dossier `microapp/static/images`

* lancer le serveur

  ```
  pip install Flask
  export FLASK_APP=microapp
  export FLASK_ENV=development
  flask run
  ```

  à ce stade ce terminal est bloqué, laissez-le tourner

* ouvrez dans un navigateur <http://localhost:5000/>

* choisissez une image
* utilisez la souris pour délimiter un rectangle (appuyez dans un coin, relâchez dans le coin opposé)  
  la position de la souris est affichée pendant ce temps
* la surface du rectangle choisi est affichée à la fin de la sélection

# les points intéressants

## nommage

* on choisit d'appeler notre appli flask `microapp`, c'est arbitraire comme nom
* on choisit d'implémenter le modèle de données (ici des images) dans le module
  `model.py`, ici aussi c'est arbitraire mais ça reflète une pratique courante
* pareil pour les vues dans `views.py`
* les images sont repérées par leur *id* qui est dérivé du nom de fichier
  sans l'extension
* pour impliquer un calcul fait *server-side*, on a choisi de calculer la surface d'un
  rectangle délimité entre les deux points du drag souris; c'est arbitraire bien sûr

## URLs

on a implémenté (vérifiez depuis votre browser)

* http://localhost:5000/ pour la liste des images
* http://localhost:5000/image/foo pour la page qui affiche l'image dont l'*id* est 'foo'
  et donc dans le fichier `foo.png`
* http://localhost:5000/api/image/area/foo/100/100/200/200 renvoie une chaine JSON (parce
  que c'est dans l'API) dans laquelle le serveur a calculé la surface entre (100, 100) et
  (200, 200)

c'est grâce au dernier point d'entrée que le code JavaScript redemande au serveur de faire
un calcul, mais sans rafraichir toute la page...

## templates

dans les templates html, on trouve par exemple

```
{% for id in ids %}
  <li><img src="{{id}}">
{%  endfor %}
```

ça marche en deux temps:

* on appelle `render_template` (qui fait partie de Flask) avec par exemple

  ```python
  return render_template("images.html", ids=images.ids())
  ```

  ce qui donne son sens au `ids` dans `{% for id in ids %}`; au moment de remplir le
  template pour en faire une vraie page, `render_template` va vraiment itérer sur l'objet
  Python référencé par `ids`

* dans les templates on peut aussi écrire des `if`, ou référencer directement une
  variable; par exemple

  ```python
  render_template("image.html", id=id, image=image)
  ```

  est utilisé dans le template dans

  `{% if image %}`

  et

  `<h1>this is the page for image {{id}}</h1>`


## imports

notre code est donc **entièrement dans le package `microapp`**

donc quand on a besoin par exemple d'importer `model.py`, on a le choix

* on peut écrire

  `from microapp.model import something`
* ou encore

  `from .model import something` depuis un autre module du package `microapp`

* mais par contre, **ça ne fonctionne pas si on fait**

  `from model import something`

# liens utiles

* le tutorial flask est vraiment trop compliqué pour démarrer

* j'ai trouvé cette page (en français pour une fois) plutôt utile pour un démarrage rapide :

https://www.kaherecode.com/tutorial/demarrer-avec-flask-un-micro-framework-python
