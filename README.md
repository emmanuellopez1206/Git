# FastAPI and git
Repository fastAPI to practice git

# COMANDOS

## git clone
Comando para clonar un reposotorio alojado en GitHub en tu local.

## git fetch
Comando para saber si hay cambios en el repo, pero no trae los cambios al local.

## git pull
Comando para traer los cambios del repo y aplicarlos en el local.

## git status
Comando para ver los cambios que llevas en tu repo local, y el tipo de cambio.

## git add
Comando para añadir cambios que has realizado en tu repo local, y dejarlos en estado de staged.

## git restore --staged
Comando para devolver un archivo de su estado staged.

## git commit -m ""
Comando para commitear los cambios que estén en staged con un breve mensaje describiendo los cambios.

## git push
Comando para subir los cambios commiteados al repo.

## git branch -a
Comando para ver las ramas remotas y locales.

## git checkout
Comando para cambiar a otra rama.

## git checkout -b
Comando para crear otra rama a partir de la actual, y cambiar a ella.

## git push --set-upstream
Comando para subir los cambios realizados en una rama local que no existe en el repo. Crea la rama en el repo y la enlaza a la local.

## git log
Comando para ver el historial de commits detalladamente.

## git log --oneline
Comando para ver el historial de commits pero agrupados en una sola línea.

## git log --oneline -<n>
Comando para ver el historial los últimos n commits, pero agrupados en una sola línea

## git merge {branch-name}
Comando para ver mezclar la rama {branch-name} en la rama actual.

## git branch -d
Comando para eliminar una rama.

## git stash
Comando para almacenar temporalmente los cambios de mi local sin necesidad de hacer commit (los cambios deben estar en staged).

## git stash list
Comando para listar los stash.

## git stash pop
Comando para traer los cambios del último stash nuevamente al local.

## git commit --amend
Comando para cambiar el último commit por uno nuevo, ya sea para cambiar el mensaje, agregar un arhicho o el contenido de un archivo.

## git reset {commit} ó git reset ~n
Comando para retroceder en la historia de los commits a un commit específico o n commits. De esta forma se guardarán los cambios que hayan entre los commits.

## git reset --hard {commit} ó git reset --hard ~n
Comando para retroceder en la historia de los commits a un commit específico o n commits. De esta forma se eliminan las diferencias entre los commits.

## git rebase
Comando para actualizar una rama con respecto a otra. También se usa para reescribir la historia de los commits (mover, eliminar, cambiar mensaje, etc).