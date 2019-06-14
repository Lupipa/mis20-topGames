# README

# BackEnd - Server Python

## Líbrerias a instalar:

``` bash
# have  python enviroment ready
# install semtiment analize dependence
$ pip install -U textblob

$ python -m textblob.download_corpora

# install twitter dependence
$ pip install tweepy
```

Orden ejecución ficheros:
``` bash
# Ejecutar el archivo 
  rec3djuegos.py
# Esto nos creará un fichero 'TopGames.txt'
Abrir el fichero TopGames.txt y modificarlo si se cree necesario
# Ejecutar el archivo. Server runs in port 5000 by default
  topgames.py
# Acceder a 
  https://twitter.com/top_mes para ver los resultados
```

# Front End -Web topgames

## Build Setup

``` bash
# install framewrok VueCli
npm i -g vue-cli
# install 
# Initialize a BootstrapVue project in the directory 'my-project'
vue init bootstrap-vue/webpack-simple my-project
# Change into the directory
cd my-project
# Install dependencies
npm install
# install Vue-Router dependence
npm install vue-router
# install axios dependence
npm install axios
# install vue-tweet-embed
npm install vue-tweet-embed
# Fire up the dev server with HMR
npm run dev

# build for production with minification
npm run build
```

=======
# mis20-topGames
Proyecto para la asignatura de Modelaje de la Interacción Social 2.0
